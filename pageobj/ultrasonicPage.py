# -*- coding: utf-8 -*-
# @Time    : 2021/12/02
# @Author  : guanzhong.zhou
# @File    : 超声破碎模块页面功能封装
import re

import pyperclip, yaml
import xlrd
from selenium.webdriver.common.keys import Keys
from common import editYaml
from common.all_path import csps_file_path, functionpageURL_path, position_in_box_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common.xlsx_excel import get_lims_for_excel, pandas_write_excel, read_excel_col
from conf.config import ultrafrac_result
from PageElemens.ultrasonic_ele import *
from data.execute_sql_action import csps_result_sql, csps_detail_sql, next_step_sql
from uitestframework.basepageTools import BasePage
from common.logs import log


class UltrasonicPage(BasePage):
    """
    超声破碎页面方法封装
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
        新建超声破碎任务单
        """
        log.info("超声破碎首页，点击新建按钮，进入样本待选表，新增超声破碎任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()
        self.wait_loading()
        self.sleep(1)

        log.info("选择任务类型")
        self.click_by_js('css', task_type)
        self.sleep(0.5)
        self.clicks('css', task_type_choice)
        self.wait_loading()


        log.info("选择操作方式")
        self.click_by_js('css', OperationType)
        self.sleep(0.5)
        self.clicks('xpath', OperationType_choice)
        self.sleep(0.5)


        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()

        log.info("选择副操实验员")
        self.clicks('css', slaverUser_btn)
        self.wait_loading()
        self.clicks('xpath', slaverUser_input)
        self.sleep(0.5)
        self.input('xpath', slaverUser_input,'周官钟')
        self.wait_loading()
        self.clicks('xpath', slaverUser_choice)
        self.sleep(0.5)
        self.clicks('xpath', slaverUser_add_btn)
        self.sleep(0.5)
        self.clicks('xpath', slaverUser_choice_)
        self.sleep(0.5)
        self.clicks('xpath', slaverUser_confirm_btn)
        self.sleep(0.5)


    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        lims_id_str = get_lims_for_excel(csps_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.clicks('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("超声破碎待选表添加样本")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
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
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()
        self.sleep(1)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    def aliquot_sample(self):
        """
        样本分管操作
        """
        log.info('样本分管操作')

        self.clicks('css', first_sample)  # 全选样本进行分管操作
        self.sleep(0.5)
        self.clicks('css', aliquot_sample)  # 点击分管按钮
        self.sleep(0.5)
        self.clicks('css', aliquot_sample_all_choice)  # 分管弹框全选按钮
        self.sleep(0.5)
        self.input('css', aliquot_number, 1)  # 分管弹框分管数文本录入
        self.clicks('css', aliquot_number_batch_edit)  # 分管弹框分管数文本录入后批量填入按钮
        self.clicks('css', aliquot_sample_next)  # 分管弹框下一步按钮
        self.sleep(1)

        self.clicks('css', aliquot_sample_last_step_all_choice)  # 分管最后步骤弹框全选
        self.sleep(0.5)
        self.moved_to_element('css', aliquot_sample_last_step)  # 分管弹框最后步骤下拉框
        self.sleep(0.5)
        self.clicks('xpath', aliquot_sample_last_step_choice)  # 分管弹框最后步骤下拉值选择
        self.sleep(0.5)
        self.clicks('css', changeProject)  # 修改项目信息
        self.clicks('css', changeProject_comfirm)  # 修改项目信息弹框确认按钮
        self.sleep(0.5)
        self.clicks('css', aliquot_sample_last_step_comfirm)  # 明细表分管弹框分管后确认按钮
        self.wait_loading()
        self.sleep(0.5)

        log.info('选择优化项目')
        # 选择优化项目弹框全选按钮
        self.clicks('css', dialog_parOpt_all_choice)
        # 选择优化项目按钮
        self.clicks('css', dialog_parOpt_btn)
        # 选择优化项目弹框录入
        self.input('css', dialog_parOpt_input, 'M')
        # 选择优化项目弹框搜索
        self.clicks('css', dialog_parOpt_search)
        self.wait_loading()
        # 选择优化项目弹框选择第一条
        self.clicks('css', dialog_parOpt_choice)
        # 选择优化项目内弹框确定
        self.clicks('css', dialog_parOpt_comfirm)
        # 选择优化项目大弹框确定
        self.clicks('css', dialog_parOpt_comfirm_comfirm)

        self.wait_loading()
        self.sleep(1)

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

    # 明细表数据录入操作
    def detail_ultrasonic(self):
        """
        超声破碎明细表，选择入库信息、批量数据录入
        """
        log.info("超声破碎明细表选择入库类型：余样入库")
        self.clicks('css', create_sort_number)  # 生成排序号按钮
        self.sleep(0.5)
        self.clicks('css', detail_all_choice)  # 列表全选按钮
        self.sleep(1)

        log.info("超声破碎明细表录入批量数据")
        self.clicks('css', detail_batch_data)  # 明细表批量数据按钮
        self.sleep(0.5)
        self.input('css', detail_remaining_sample_package_amount, 1)  # 明细表批量数据，包装余量
        self.sleep(0.5)

        # 进入量和进入体积会自动计算出来，此处不用批量录入
        # self.input('css', detail_used_sample_amount, 1)  # 明细表批量数据，样本进入量
        # self.sleep(0.5)
        # self.input('css', detail_sample_package_amount_unit, 1)  # 明细表批量数据，样本进入体积
        # self.sleep(0.5)
        self.clicks('css', detail_batch_data_comfirm)  # 明细表批量数据弹框，确认按钮
        self.sleep(1)
        log.info("超声破碎明细表自动计算")
        self.clicks('css', detail_auto_calculate)  # 自动计算按钮
        self.sleep(1)
        ele = self.isElementExists('css', detail_auto_calculate_info)
        if ele:
            self.clicks('css', detail_auto_calculate_info)  # 自动计算部分表格有值提示信息
            self.sleep(1)

        self.sleep(1)

    # 明细表提交
    def detail_sumbit(self):
        """
        超声破碎明细表，样本提交操作
        :return:
        """
        log.info("超声破碎明细表样本提交")
        self.clicks('css', detail_all_choice)
        self.clicks('css', submit_btn)  # 提交按钮

        self.sleep(0.5)
        Screenshot(self.driver).get_img("超声破碎明细表提交")
        # 这里调用自定义截图方法
        self.sleep(1)
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()

    # 明细表入库
    def detail_into_storage(self):
        """
        超声破碎明细表样本入库操作
        """
        log.info('超声破碎明细表，样本入库操作')
        self.clicks('css', detail_all_choice)  # 列表全选按钮
        self.sleep(0.5)
        self.clicks('css', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮


        log.info('超声破碎明细表，样本入库选择入样本盒')
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
        self.sleep(1)

        log.info('超声破碎明细表，样本入库录入盒内位置')

        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(csps_detail_sql.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel
        print(res)
        pandas_write_excel(res, position_in_box_path)

        data = xlrd.open_workbook(position_in_box_path)
        num_list = []
        for item in range(0, len(lims_list)):
            tables = data.sheets()[0]
            vals = tables.row_values(item)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))

        # 粘贴到【批量粘贴盒内位置】文本框
        self.clicks('css', batch_copy_BoxPosition)
        self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(1)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(1)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("超声破碎明细表入库")
        self.clicks('css', storage_next)
        result = self.findelement('xpath', '//p[contains(text(),"样本入库成功")]')

        self.wait_loading()

        return result

    # 结果表数据录入
    def ultrasonic_result_data_input(self):
        """
        超声破碎结果表修改产物类型、批量数据、自动计算操作
        """
        log.info("超声破碎结果表，修改产物类型")
        self.clicks('css', result_all_choice)  # 样本列表数据全选按钮
        self.sleep(0.5)
        self.clicks('css', result_change_product_type)  # 修改产物类型
        self.sleep(0.5)
        self.clicks('xpath', result_change_product_type_choice)  # 修改产物类型弹框数据选择，默认选择石蜡组织DNA
        self.sleep(0.5)
        self.clicks('css', result_change_product_type_comfirm)  # 修改产物类型弹框数据选择，确认
        ele = self.isElementExists('css', result_change_product_type_continue_comfirm)
        print(ele)
        if ele:
            self.clicks('css', result_change_product_type_continue_comfirm)

        self.wait_loading()
        self.sleep(1)

        log.info("超声破碎结果表，批量数据")
        self.clicks('css', result_batch_data)  # 批量数据按钮
        self.wait_loading()
        self.sleep(0.5)
        self.input('css', result_sample_package_amount, 1)  # 批量数据弹框，产物包装量
        self.sleep(0.5)
        self.clicks('css', result_sample_package_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', result_sample_amount_unit_choice)  # 批量数据弹框，包装单位下拉值（管 ）
        self.sleep(0.5)
        self.input('css', result_number_of_labels_printed, 1)  # 批量数据弹框，标签打印份数文本框
        self.sleep(0.5)
        self.clicks('css', result_batch_data_comfirm)  # 批量数据弹框，确认按钮
        self.sleep(1.5)

        log.info("超声破碎结果表，自动计算数据")
        self.clicks('css', result_auto_calculate)  # 结果表自动计算按钮
        self.wait_loading()
        self.sleep(0.5)
        ele = self.isElementExists('css', result_auto_calculate_promote)
        if ele:
            self.clicks('css', result_auto_calculate_promote)  # 结果表自动计算提示框确认按钮
        self.sleep(1)

    # 结果表表单（盒内位置）录入
    def ultrasonic_result_formdata_input(self):
        """
        超声破碎结果表盒内位置录入，通过SQL写入
        """
        taskstatus = self.get_text('css', result_task_id)
        sqls = csps_result_sql.format(taskstatus[5:].strip())
        self.updata_sql(sqls)
        self.refresh()
        self.wait_loading()

    # 结果表提交
    def result_submit_sample(self):
        """
        结果表提交
        """
        log.info(' 超声破碎结果表,点击提交')
        self.clicks('css', result_all_choice)  # 数据全选
        self.clicks('css', result_submit)  # 提交按钮
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("超声破碎结果表提交")

        self.clicks('css', result_submit_comfirm)  # 提交确认按钮
        pageinfo = self.get_pageinfo()
        print(pageinfo)
        self.wait_loading()

        return pageinfo

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """
         根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
        """
        self.add_excel_xlxs(next_step_sql, ultrafrac_result, result_task_id)
        print("下一步流程写入成功")

    # 完成任务单
    def complete_task(self):
        """
        完成任务单
        """
        log.info('超声破碎结果表,点击完成任务单')

        self.clicks('css', enter_result_list_btn)
        self.wait_loading()
        self.sleep(1)
        self.click_by_js('css', result_complete_task_btn)
        if re.search(r'请在当前选择的SOP中选择使用的仪器', self.get_source):
            pass
        else:
            self.wait_loading()
            self.sleep(2)

            # 调用自定义截图方法
            Screenshot(self.driver).get_img("超声破碎结果表完成任务单")

            taskstatus = self.get_text('css', task_status)
            print(taskstatus)

            return taskstatus

    # 超声破碎任务列表查询样本所在任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(csps_file_path, 'lims号')

        self.clicks('css', search)
        self.sleep(1)
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(1)
        self.clicks('css', search_confirm)
        self.wait_loading()
        self.sleep(1)
        print('进入页面')
        samples = self.findelements('xpath', sample_page_list)
        print(len(samples))
        return len(samples)
