# -*- coding: utf-8 -*-
# @Time    : 2021/12/06
# @Author  : guanzhong.zhou
# @File    : 文库构建模块页面功能封装
import re
from datetime import datetime
import pyperclip, xlrd, yaml
from selenium.webdriver.common.keys import Keys
from PageElemens.libconstruction_ele import *
from common.all_path import wkgj_file_path, functionpageURL_path, position_in_box_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common import editYaml
from common.xlsx_excel import get_lims_for_excel, pandas_write_excel, read_excel_col
from conf.config import libconstruction_result
from data.sql_action.execute_sql_action import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class LibconstructionPage(BasePage):
    """
    文库构建页面方法封装
    """

    # 打开指定页面
    def enter_function_page(self, url):
        """
        进入指定url页面
        """
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
        self.sleep(1)

    # 获取页面提示信息
    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Submit successfully---提交成功
        sample in storage successfully---入库成功
        """

        if self.isElementExists('xpath', page_success_info):
            return self.get_text('xpath', page_success_info)
        else:
            return None

    # 新增任务单
    def add_task(self):
        """
        新建文库构建任务单
        """
        log.info("文库构建首页，点击新建按钮，进入样本待选表，新增文库构建任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()
        self.sleep(2)

        log.info("选择任务类型")
        self.click_by_js('css', task_type)
        self.sleep(0.5)
        self.clicks('css', task_type_choice)
        self.wait_loading()
        self.sleep(0.5)

        log.info("选择操作方式")
        self.click_by_js('css', operation_type)
        self.sleep(0.5)
        self.clicks('xpath', operation_type_choice)
        self.sleep(1)

        log.info("选择 实验室值班主管 ")
        self.clicks('css', select_dutySupervisors)
        self.sleep(0.5)
        self.clicks('xpath', select_dutySupervisors_choice)
        self.sleep(1)

        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()

    # excel中获取待选样本

    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        lims_id_str = get_lims_for_excel(wkgj_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()

        # 如果有未查到的样本，忽略
        if self.isElementExists('xpath', error_info):
            self.clicks('xpath', error_info)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        Screenshot(self.driver).get_img("文库构建待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")
        pageInfo = self.get_pageinfo()
        self.wait_loading()
        # 判断子sop样本数据数否需要录入
        result = self.driver.execute_script(
            'return document.getElementsByClassName("commonTaskDetail-commonTaskDetailBtn-sopSampleNumber")[0].disabled')
        if not result:
            self.clicks('css', sopSampleNumber_btn)  # 点击子sop样本数量
            self.wait_loading()
            self.clicks('css', sopSampleNumber)  # 子sop样本数量弹框中点击数量录入框
            self.input('css', sopSampleNumber_input, 10)
            self.clicks('css', sopSampleNumber_confirm)
            self.wait_loading()

        return pageInfo

    # 进入明细表或结果表
    def enter_result_list(self, ele, page):
        """
        待选表或者明细表，在进入下一节点时，获取下一节点URL地址，并写入临时数据文件中
        :param ele: 点击进入下一节点元素定位
        :param page: 下一节点页面名称
        """
        urldata = editYaml.read_yaml(functionpageURL_path)

        self.clicks('css', ele)
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()  #
        self.sleep(2)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    # 明细表入库信息、批量包装余量、录入96孔版位置
    def detail_libconstruction(self):
        """
        文库构建明细表，选择入库信息、批量包装余量、录入96孔版位置
        """
        log.info("文库构建明细表选择入库类型：余样入库")
        self.click_by_js('css', detail_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.moved_to_element('css', detail_batch_storage_type)  # 明细表批量入库类型下拉框
        self.sleep(1)
        self.click_by_js('xpath', detail_batch_storage_type_choice)  # 明细表批量入库类型下拉值,选择余样入库
        self.sleep(1)

        log.info("文库构建明细表录入批量包装余量")
        self.clicks('css', batch_remaining_sample_package_amount)  # 明细表批量包装余量
        self.sleep(0.5)
        self.clicks('css', batch_remaining_sample_package_amount_comfirm)  # 明细表批量包装余量确认
        self.sleep(0.5)

        log.info("文库构建明细表录入96孔版位置")
        self.clicks('css', col_96_well_plate_position)  # 明细表选中一条数据
        self.sleep(0.5)
        self.input('css', col_create_96_well_plate_position_input, 1)  # 录入96孔板位置
        self.sleep(0.5)
        self.clicks('css', auto_create_96_well_plate_position)  # 点击自动生成96孔板位置
        self.wait_loading()
        self.sleep(1)

    # 明细表表单数据录入
    def detail_libconstruction_form_input(self):
        log.info("文库构建明细表选择是否选择大小，进行自动计算操作")

        taskstatus = self.get_text('css', detail_task_id)  # 获取明细表任务单号
        log.info(" 根据明细表任务单号，查询数据库并录入是否选大小:否")
        sql1 = wkgj_detail_sql1.format(taskstatus[5:].strip())
        self.updata_sql(sql1)
        self.sleep(1)
        log.info(" 核酸浓度小于4.5时执行录入操作")

        consistence_amt1 = self.isElementExists('css', consistenceAmt)
        if consistence_amt1:
            consistence_amt = self.get_text('css', consistenceAmt)
            if int(float(consistence_amt)) < 4:
                sql3 = wkgj_detail_sql3.format(taskstatus[5:].strip())
                self.updata_sql(sql3)
                self.sleep(1)
        log.info("核酸总量不为500时执行录入操作")
        actualTotal_amt1 = self.isElementExists('css', actualTotalAmt)
        if actualTotal_amt1:
            actualTotal_amt = self.get_text('css', actualTotalAmt)
            if int(float(actualTotal_amt)) < 450:
                sql5 = wkgj_detail_sql5.format(taskstatus[5:].strip())
                self.updata_sql(sql5)
                self.sleep(1)

        self.refresh()  # 数据库修改【是否选大小】后刷新页面
        self.wait_loading()
        self.sleep(1)

        log.info("点击自动计算")
        self.clicks('css', detail_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.clicks('css', detail_auto_calculate)
        self.wait_loading()
        self.sleep(0.5)

        log.info(" 判断建库进入量是否有值，且是否小于50，如果小于则修改为50")
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=2300')
        self.sleep(0.5)
        ele = self.isElementExists('css', countamt)
        if ele:
            amtdata = self.get_text('css', countamt)
            remainingVolumeAmt = self.get_text('css', remaining_VolumeAmt)
            remainingTotalAmt = self.get_text('css', remaining_TotalAmt)

            print('建库进入量', amtdata)
            if int(amtdata) < 50:
                # 根据修改文库构建明细表样本进入量值，若值小于50，从数据库修改值为50
                sql4 = wkgj_detail_sql4.format(taskstatus[5:].strip())
                print(sql4)
                self.updata_sql(sql4)
            elif int(float(remainingVolumeAmt)) < 0 or int(float(remainingTotalAmt)) < 0:
                # 根据修改文库构建明细表样本进入量值，若值小于50，从数据库修改值为50
                sql4 = wkgj_detail_sql6.format(taskstatus[5:].strip())
                print(sql4)
                self.updata_sql(sql4)

        # 刷新页面
        self.refresh()
        self.wait_loading()
        self.sleep(1)

    # 明细表提交
    def detail_submit(self):
        """
        文库构建明细表，样本提交操作
        :return:
        """
        log.info("文库构建明细表样本提交")
        self.clicks('css', detail_all_choice)
        self.clicks('css', submit_btn)  # 提交按钮
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("文库构建明细表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()
        self.sleep(1)

    # 明细表入库
    def detail_into_storage(self):
        """
        文库构建明细表样本入库操作
        """
        try:
            log.info('文库构建明细表，样本入库操作')

            self.clicks('css', deposit_into_storage)  # 入库按钮
            self.sleep(0.5)
            self.clicks('css', storage_all_choice)  # 入库弹框全选按钮

            log.info('文库构建明细表，样本入库选择入库类型临时库')
            self.moved_to_element('css', target_storage_type)  # 入库弹框选择入库类型下拉框
            self.sleep(1)
            if self.isElementExists('xpath', target_storage_type_value):
                self.click_by_js('xpath', target_storage_type_value)  # 入库弹框选择入库类型下拉值（临时库）
                self.sleep(0.5)

            log.info('文库构建明细表，样本入库选择入样本盒')
            self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
            self.wait_loading()
            self.input('css', target_storage, '自动化测试用(勿删)')
            self.sleep(0.5)
            self.clicks('css', select_sample_box_search)
            self.wait_loading()
            self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
            self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
            self.sleep(0.5)

            log.info('文库构建明细表，样本入库录入盒内位置')

            taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
            lims_id = executeSql.test_select_limsdb(
                wkgj_detail_sql2.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

            lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
            nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
            res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
            print(res)
            pandas_write_excel(res, position_in_box_path)  # 把样本号和盒内位置编号写入Excel模板

            data = xlrd.open_workbook(position_in_box_path)  # 从Excel读取模板样本号和盒内位置编号
            num_list = []
            for index in range(0, len(lims_list)):
                tables = data.sheets()[0]
                # allrows = tables.nrows
                vals = tables.row_values(index)
                imp_data = '\t'.join(map(str, vals))
                num_list.append(imp_data)
            print("\n".join(map(str, num_list)))
            pyperclip.copy("\n".join(map(str, num_list)))

            # 粘贴到【批量粘贴盒内位置】文本框
            self.clicks('css', batch_copy_BoxPosition)
            self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
            self.sleep(1)
            self.clicks('css', batch_copy_BoxPosition_comfirm)
            self.sleep(0.5)
            Screenshot(self.driver).get_img("文库构建明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")

            self.clicks('css', storage_next)
            self.wait_loading()

            self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3000')
            self.sleep(0.5)
            pageInfo = self.get_text('css', sumbit_status)
            print(pageInfo)
            return pageInfo
        except Exception as info:
            print(info)

    # 结果表批量数据录入
    def ultrasonic_result_data_input(self):
        """
        文库构建结果表修改产物类型、批量数据
        """
        log.info("文库构建结果表，修改产物类型")
        self.clicks('css', result_all_choice)  # 样本列表数据全选按钮
        self.sleep(0.5)
        self.clicks('css', result_change_product_type)  # 修改产物类型
        self.sleep(0.5)
        self.clicks('css', result_change_product_type_choice)  # 修改产物类型弹框数据选择，默认选择第一条
        self.sleep(0.5)
        self.clicks('css', result_change_product_type_comfirm)  # 修改产物类型弹框数据选择，确认
        ele = self.isElementExists('css', result_change_product_type_continue_comfirm)
        print(ele)
        if ele:
            self.clicks('css', result_change_product_type_continue_comfirm)
        self.wait_loading()
        self.sleep(1)

        log.info("文库构建结果表，批量数据")
        self.clicks('css', result_batch_data)  # 批量数据按钮
        self.wait_loading()
        self.sleep(0.5)
        self.input('css', result_sample_package_amount, 1)  # 批量数据弹框，产物包装量
        self.sleep(0.5)
        self.clicks('css', result_sample_package_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', result_sample_amount_unit_choice)  # 批量数据弹框，包装单位下拉值（管 ）
        self.sleep(0.5)
        self.input('css', result_number_of_ircular_labels_printed, 1)  # 批量数据弹框，圆打印份数文本框
        self.sleep(0.5)
        self.input('css', result_number_of_rectangular_labels_printed, 1)  # 批量数据弹框，长打印份数文本框
        self.sleep(0.5)

        self.sleep(0.5)
        self.input('css', pcr_cycle, 6)  # 批量数据弹框，循环数
        self.sleep(0.5)
        self.input('css', library_volume, 10)  # 批量数据弹框，文库体积
        self.sleep(0.5)
        self.input('css', purification_concentration, 10)  # 批量数据弹框，连接后纯化体积
        self.sleep(0.5)
        self.input('css', fragment_volume, 10)  # 批量数据弹框，大小片段分离后体积μL
        self.sleep(0.5)

        self.clicks('css', result_batch_data_comfirm)  # 批量数据弹框，确认按钮
        self.sleep(0.5)
        self.clicks('css', result_save_task)
        self.wait_loading()

        # 预计富集时间

    def edit_estimated_enrichment_time(self):
        """
        预计富集时间
        """
        now_time = datetime.now()
        str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
        self.clicks('css', edit_estimated_enrichment_time)  # 预计富集时间按钮
        self.wait_loading()
        self.clicks('css', edit_estimated_enrichment_time_all_choice)  # 预计富集时间弹框全选
        self.sleep(0.5)
        self.clicks('css', batch_edit_estimated_enrichment_date)  # 预计富集时间弹框，录入时间弹框按钮
        self.sleep(0.5)
        self.input('css', estimated_enrichment_data, str_time)  # 预计富集时间弹框，时间录入文本
        self.sleep(0.5)
        self.clicks('css', estimated_enrichment_data_comfirm)  # 预计富集时间弹框，时间录入文本确认按钮
        self.sleep(0.5)
        self.clicks('css', edit_estimated_enrichment_time_comfirm)  # 预计富集时间弹框确认按钮
        self.wait_loading()
        self.sleep(0.5)

    # 结果表表单录入
    def ultrasonic_result_formdata_input(self):
        """
        文库构建结果表通过数据库进行大小片段分离后浓度、连接后纯化浓度、文库浓度、盒内位置录入
        """
        taskstatus = self.get_text('css', result_task_id)
        ##大小片段分离后浓度、连接后纯化浓度、96孔板编号、盒内位置数据库写入
        sql1 = wkgj_result_sql1.format(taskstatus[5:].strip())
        self.updata_sql(sql1)

        # 根据result_id修改文库构建‘cfdna结果扩展表’---‘fragment_consistence_amt’字段【片段分离后浓度（ng/μL）】值，即页面文库浓度ng/μL*值
        sql3 = wkgj_result_sql3.format(taskstatus[5:].strip())
        sql5 = wkgj_result_sql5.format(taskstatus[5:].strip())

        self.updata_sql(sql3)
        self.updata_sql(sql5)

        # 刷新页面
        self.refresh()
        self.wait_loading()

        self.clicks('css', result_all_choice)
        log.info(' 文库构建结果表,点击批量计算')
        self.clicks('css', result_auto_calculate)
        self.wait_loading()
        self.sleep(1)
        ele = self.isElementExists('css', result_auto_calculate_promote)
        if ele:
            self.click_by_js('css', result_auto_calculate_promote)
            self.sleep(0.5)

    # Adapter选择
    def edit_adapter(self):
        """
        Adapter选择
        """
        log.info('Adapter选择')
        self.executeJscript(
            'document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=0')
        self.sleep(0.5)
        log.info('Adapter选择,第一条执行选择操作')
        # Adapter选择,第一条执行选择操作，剩下的通过数据库操作
        self.click_by_js('css', adapter.format(1))
        self.wait_loading()
        self.clicks('xpath', adapter_choice)
        self.clicks('css', adapter_comfirm)
        self.sleep(0.5)

        log.info('Adapter选择后保存')
        self.clicks('css', result_save_task)
        self.wait_loading()
        self.sleep(0.5)

        taskstatus = self.get_text('css', result_task_id)
        # 设置Adapter(index_id )
        sql1 = wkgj_result_sql6.format(taskstatus[5:].strip())
        self.updata_sql(sql1)
        self.sleep(0.5)

        self.refresh()
        self.wait_loading()
        self.sleep(0.5)

    def goback_detail(self):
        """
        返回明细表
        """

        urldata = editYaml.read_yaml(functionpageURL_path)
        log.info('点击按钮返回明细表')
        self.click_by_js('css', goback_detail)

        self.clicks('css', goback_page_info)
        self.wait_loading()
        self.sleep(0.5)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    # 结果表提交
    def result_submit_sample(self):
        """
        结果表提交
        """
        log.info(' 文库构建结果表,点击提交')
        self.clicks('css', result_all_choice)
        self.sleep(0.5)
        self.clicks('css', result_submit)  # 提交按钮
        self.wait_loading()
        self.sleep(0.5)

        Screenshot(self.driver).get_img("文库构建结果表点击提交按钮","弹出提交确认按钮")

        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        self.wait_loading()
        self.sleep(0.5)

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """
         根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
        """
        self.add_excel_xlxs(next_step_sql, libconstruction_result, result_task_id)
        print("下一步流程写入成功")

    # 完成任务单
    def complete_task(self):
        """
        完成任务单
        """
        log.info('文库构建结果表,点击完成任务单')

        self.clicks('css', enter_result_list_btn)
        self.wait_loading()
        self.click_by_js('css', result_complete_task_btn)
        if   re.search(r'请在当前选择的SOP中选择使用的仪器', self.get_source):
            pass
        else:
            self.click_by_js('css', complete_rusult_confirm_btn)
            self.wait_loading()

            # 调用自定义截图方法
            Screenshot(self.driver).get_img("文库构建结果表点击完成任务单按钮","完成任务单成功，状态改为完成")

            taskstatus = self.get_text('css', task_status)
            print(taskstatus)

            return taskstatus

    # 文库构建任务列表查询样本所在任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(wkgj_file_path, 'lims号')

        self.clicks('css', search)
        self.sleep(0.5)
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(0.5)
        self.clicks('css', search_confirm)
        self.wait_loading()
        self.sleep(0.5)
        samples = self.findelements('xpath', sample_page_list)
        print(len(samples))
        return len(samples)
