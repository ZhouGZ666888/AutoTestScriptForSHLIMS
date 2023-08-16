# -*- coding: utf-8 -*-
# @Time    : 2022/01/24
# @Author  : guanzhong.zhou
# @File    : MGMT模块页面功能封装
import pyperclip
import xlrd,yaml
from selenium.webdriver.common.keys import Keys
from common import editYaml
from common.all_path import mgmt_file_path, functionpageURL_path, position_in_box_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common.xlsx_excel import get_lims_for_excel, pandas_write_excel, read_excel_col
from PageElemens.mgmt_ele import *
from data.sql_action.execute_sql_action import mgmt_sql1, mgmt_sql2, mgmt_sql3
from uitestframework.basepageTools import BasePage
from common.logs import log



class MGMTPage(BasePage):
    """
    MGMT页面方法封装
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

        return self.get_text('xpath', page_success_info)

    # 新增任务单
    def add_task(self):
        """
        新建MGMT任务单
        """
        log.info("MGMT首页，点击新建按钮，进入样本待选表，新增MGMT任务")
        self.clicks('css', add_task)
        self.wait_loading()
        self.wait_loading()
        self.sleep(1)

        # ("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()



    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        log.info("MGMT待选表核对lims号功能，并保存任务单号")
        lims_id_str = get_lims_for_excel(mgmt_file_path)
        # ('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()
        self.sleep(1)

        # ('选中核对后的样本，点击【加入选中样本&保存】')
        self.clicks('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MGMT待选表 ")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        self.sleep(0.5)
        return pageinfo

    # 进入明细表或结果表
    def enter_result_list(self, ele, page):
        """
        待选表或者明细表，在进入下一节点时，获取下一节点URL地址，并写入临时数据文件中
        :param ele: 点击进入下一节点元素定位
        :param page: 下一节点页面名称
        """
        urldata = editYaml.read_yaml(functionpageURL_path)

        self.clicks('css', ele)
        ('点击按钮进入{}'.format(page))
        self.wait_loading()
        self.wait_loading()
        self.sleep(2)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    def detail_mgmt_edit(self):
        """
        录入批量入库类型、自动计算
        """

        # 全选
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        log.info("录入批量入库类型")
        self.moved_to_element('css', detail_batch_storage_type)
        self.sleep(0.5)
        self.clicks('xpath', detail_batch_storage_type_choice)
        self.sleep(0.5)

        log.info("点击自动计算")
        self.clicks('css', autoComplete)
        # 判断是否有弹框提示
        ele = self.isElementExists('css', autoComplete_tip)
        if ele:
            self.clicks('css', autoComplete_tip)
        self.sleep(0.5)

        self.clicks('css', detail_save_result)
        self.wait_loading()

        log.info("设置包装余量")
        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        self.updata_sql(mgmt_sql3.format(taskstatus[5:].strip()))  # 设置包装余量
        self.sleep(0.5)
        self.refresh()
        self.wait_loading()
        self.sleep(0.5)

    def detail_sumbit(self):
        """
        明细表提交操作
        :return:样本提交状态
        """

        log.info("提交样本")
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        self.clicks('css', detail_submit_btn)
        self.wait_loading()

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MGMT明细表提交 ")

        self.clicks('css', detail_submit_comfirm)
        self.wait_loading()
        self.sleep(0.5)

    def detail_into_storage(self):
        """
        明细表入库操作
        :return:样本提交状态
        """
        log.info('MGMT明细表，样本入库操作')
        self.clicks('css', detail_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.clicks('css', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮

        log.info('MGMT明细表，样本入库选择入库类型临时库')
        self.moved_to_element('css', target_storage_type)  # 入库弹框选择入库类型下拉框
        self.sleep(0.5)
        self.clicks('xpath', target_storage_type_value)  # 入库弹框选择入库类型下拉值（临时库）
        self.sleep(0.5)

        log.info('MGMT明细表，样本入库选择入样本盒')
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(1)

        log.info('MGMT明细表，样本入库录入盒内位置')

        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(mgmt_sql1.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

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
        self.sleep(0.5)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(1)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MGMT明细表入库")

        self.clicks('css', storage_next)
        self.wait_loading()

        log.info('MGMT明细表，获取样本提交状态')
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=1400')
        self.sleep(0.5)
        pageinfo = self.get_text('css', detail_sumbit_status)
        print(pageinfo)
        return pageinfo

    def result_edit(self):
        """
        结果表数据录入，批量计算
        :return:
        """
        log.info("结果表数据录入")
        self.clicks('css', result_all_choice)
        self.sleep(0.5)

        log.info("批量质检结果选择")
        self.moved_to_element('css', ultrafracResults)
        self.sleep(0.5)
        self.clicks('xpath', ultrafracResults_chioice)
        self.sleep(0.5)

        log.info("批量结果判读")
        self.moved_to_element('css', judgeResult)
        self.sleep(0.5)
        self.clicks('xpath', judgeResult_choice)
        self.sleep(0.5)

        self.clicks('css', result_save)
        self.sleep(0.5)

    def result_data(self):
        """
        结果表表单转化后浓度、进入总量、总油滴数、FAM信号油滴数、HEX信号油滴数录入，进行自动计算
        :return:
        """

        log.info("表单转化后浓度、进入总量、总油滴数、FAM信号油滴数、HEX信号油滴数录入，进行自动计算")
        taskstatus = self.get_text('css', result_task_id)  # 获取明细表任务单号
        sql1 = mgmt_sql2.format(taskstatus[5:].strip())
        self.updata_sql(sql1)
        self.sleep(0.5)
        self.refresh()
        self.wait_loading()
        self.sleep(0.5)

        log.info("点击自动计算")
        self.clicks('css', result_all_choice)
        self.sleep(0.5)
        self.clicks('css', result_autoComplete)
        ele = self.isElementExists('css', result_autoComplete_tips)
        if ele:
            self.clicks('css', result_autoComplete_tips)
            self.sleep(0.5)
        self.sleep(0.5)

    def result_sumbit(self):
        """
        结果表提交操作
        :return: 提交状态
        """
        log.info("点击提交按钮")
        self.clicks('css', result_sumbit)

        self.wait_loading()

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MGMT结果表提交")

        ele = self.isElementExists('css', laboratory_auditor)
        if ele:
            log.info("选择实验室审核人")
            self.clicks('css', laboratory_auditor)
            self.input('css', laboratory_auditor, 'dgq')
            self.wait_loading()

            self.clicks('css', laboratory_auditor_choice)
            self.sleep(1)
        # 提交确认按钮
        self.clicks('css', result_sumbit_comfirm)
        self.wait_loading()

        log.info("获取表单是否已提交字段")
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=2000')
        self.sleep(0.5)
        samplestatue = self.get_text('css', sample_statue)
        self.sleep(0.5)
        return samplestatue

    def complete_task(self):
        """
        完成任务单
        :return:任务单状态
        """
        log.info("完成任务单")
        self.clicks('css', complete_task)
        self.wait_loading()

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("MGMT结果表完成任务单")

        self.sleep(1)

        taskstatus = self.get_text('css', detail_task_status)
        return taskstatus[6:].strip()

        # 21基因任务列表查询样本所在任务单

    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(mgmt_file_path,  'lims号')

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
