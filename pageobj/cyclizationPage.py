# -*- coding: utf-8 -*-
# @Time    : 2023/08/18
# @Author  : guanzhong.zhou
# @File    : 环化模块页面功能封装
import pyperclip
import xlrd,re
from selenium.webdriver.common.keys import Keys
from common.all_path import  position_in_box_path, cyclization_file_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common.xlsx_excel import get_lims_for_excel, pandas_write_excel, read_excel_col
from PageElemens.cyclization_ele import *
from conf.config import cyclization_result
from data.sql_action.execute_sql_action import cyclization_update, cyclization_get_lims, cyclization_next_step
from uitestframework.basepageTools import BasePage
from common.logs import log


class CycliPage(BasePage):
    """环化页面方法封装"""

    # 获取页面提示信息
    def get_pageinfo(self):
        return self.get_text('xpath', page_success_info)

    # 新增任务单
    def add_task(self):
        """新建环化任务单"""
        log.info("环化首页，点击新建按钮，进入样本待选表，新增环化任务")
        self.clicks('css', add_task)
        self.wait_loading()
        log.info("选择sop")
        self.clicks('css', sop_btn)
        self.sleep(0.5)
        self.clicks('css', sop_choice)
        self.wait_loading()
        log.info("环化录入任务描述")
        self.input('css', task_des, '环化自动化测试任务')

    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        log.info("环化待选表核对lims号功能，并保存任务单号")
        lims_id_str = get_lims_for_excel(cyclization_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()
        self.sleep(1)

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.clicks('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        # 调用自定义截图方法
        Screenshot(self.driver).get_img("点击新建按钮，进入环化待选表","进入待选表成功")

        pageinfo = self.get_pageinfo()
        self.wait_loading()
        self.clicks('css', enter_detail_list_btn)  # 进入明细表
        return pageinfo

    # 样本分管操作
    def detail_app_a_aliquot_sample(self):
        """样本分管操作"""
        # 选择一条样本进行分管
        self.clicks('css', detail_choice_one_sample)
        self.sleep(0.5)
        log.info("环化样本分管")
        self.clicks('css', detail_aliquot_sample)
        self.wait_loading()
        self.clicks('css', aliquot_sample_all_choice)
        self.sleep(0.5)
        log.info("环化样本分管选择分管数量")
        self.clicks('css', aliquot_sample_numb)
        self.clicks('css', aliquot_sample_numb_confirm)
        self.sleep(0.5)
        log.info("环化样本明细表分管完成")
        # 明细表分管完成按钮
        self.clicks('css', aliquot_sample_next_step_finsh)
        pageinfo = self.get_pageinfo()
        self.wait_loading()
        return pageinfo
        # 样本分管成功

    # 明细表生成产物
    def detail_generate_product(self):
        """明细表生成产物"""
        self.clicks('css', detail_part_choice)  # 全选样本
        log.info("环化样本生成产物信息")
        self.clicks('css', detail_generate_product_btn)
        self.wait_loading()
        self.clicks('css', detail_generate_product_all_choice)
        self.sleep(0.5)
        log.info("环化样本生成产物设置生成产物数量")
        # 明细表生成产物弹框批量生成产物数量按钮
        self.clicks('css', detail_generate_product_numb_btn)
        # 明细表生成产物弹框批量生成产物数量确认按钮
        self.clicks('css', generate_product_numb_confirm)
        # 明细表生成产物弹框确认按钮
        self.clicks('css', generate_product_confirm)
        pageinfo = self.get_pageinfo()
        self.wait_loading()
        taskId = self.get_text('css', detail_task_id)
        taskid=re.findall(r'[A-Za-z0-9]+', taskId)[0]
        executeSql.test_updateByParam(cyclization_update.format(taskid, taskid))  # 更新数据库，结果表自动计算数据，设置下一步流向
        self.refresh()
        return pageinfo

    # 批量数据
    def detail_batch_data(self):
        """批量数据"""
        self.clicks('css', detail_all_choice)  # 全选样本
        self.sleep(0.5)
        self.clicks('css', detail_batch_data_btn)
        self.sleep(0.5)
        log.info("环化批量数据，录入包装余量")
        self.input('css', detail_remaining_sample_pkg_amt_input, 1)
        self.sleep(0.5)
        log.info("环化批量数据，选择入库类型")

        self.clicks('css', detail_batch_storage_type)  # 入库弹框选择入库类型下拉框
        self.sleep(0.5)
        self.clicks('xpath', detail_batch_storage_type_choice)  # 入库弹框选择入库类型下拉值（余样入库）
        self.sleep(0.5)
        self.clicks('css', detail_batch_data_btn_confirm)
        depositType=self.get_text('css','tr:nth-child(1) .cylizationScheduletableCol-depositType')
        return depositType
    # 明细表自动计算
    def detail_autoComplete(self):
        """明细表自动计算"""
        log.info("环化明细表明细表自动计算")
        self.clicks('css', detail_autoComplete_btn)
        pageinfo = self.get_pageinfo()
        self.wait_loading()
        return pageinfo
    # 明细表保存
    def detail_save(self):
        """明细表保存"""
        log.info("环化明细表保存")
        self.clicks('css', detail_save)
        pageinfo = self.get_pageinfo()
        self.wait_loading()
        return pageinfo

    # 进入结果表
    def detail_enter_result(self):
        """进入结果表"""
        log.info("环化进入结果表")
        self.clicks('css', detail_enter_result)
        self.wait_loading()

    # 自动计算
    def result_autoComplete(self):
        """环化结果表自动计算,计算两遍"""
        log.info("环化结果表自动计算")
        self.clicks('css', result_all_choice)
        self.sleep(0.5)
        self.clicks('css', result_autoComplete)
        self.sleep(0.5)
        self.clicks('css', result_autoComplete_tip)
        self.sleep(0.5)
        self.clicks('css', result_autoComplete)
        self.sleep(0.5)
        self.clicks('css', result_autoComplete_tip)
        self.sleep(0.5)

    # 结果表提交
    def result_commit(self):
        """结果表提交"""
        log.info("环化结果表提交")
        self.clicks('css', result_commit)
        self.wait_loading()
        self.clicks('css', result_commit_confirm)
        self.wait_loading()
        info=self.get_text('css',submitType)
        return info
    # 明细表提交、入库
    def detail_commit(self):
        """明细表提交、入库"""
        log.info("结果表返回明细表")
        self.clicks('css', result_return_detail)
        self.sleep(0.5)
        self.clicks('css', result_return_detail_confirm)
        self.wait_loading()
        log.info("环化明细表提交")
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        self.clicks('css', detail_commit)
        self.wait_loading()
        self.clicks('css', detail_commit_confirm)
        self.wait_loading()
        log.info("环化明细表入库")
        self.clicks('css', deposit_into_storage)
        self.sleep(1)
        self.clicks('css', storage_all_choice)  # 入库弹框全选按钮
        self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
        self.sleep(0.5)
        self.input('css', target_storage, '自动化测试用(勿删)')  # 入库弹框选择样本盒弹框t搜索文本录入框
        self.clicks('css', select_sample_box_search)  # 入库弹框选择样本盒弹框t搜索按钮
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
        self.clicks('xpath', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮

        taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
        lims_id = executeSql.test_select_limsdb(cyclization_get_lims.format(re.findall(r'[A-Za-z0-9]+', taskstatus)[0]))  # 从数据库获取当前任务单号下样本lims号

        lims_list = [item[key] for item in lims_id for key in item]  # 把获取的lims号转换为一维列表
        nub_list = [str(i) for i in range(1, len(lims_list) + 1)]  # 根据lims样本数量，生成数字列表，作为盒内位置编号用
        res = [list(i) for i in zip(lims_list, nub_list)]  # 将lims号和数字编号转换为二维列表格式，写入Excel

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
        self.clicks('xpath', batch_copy_BoxPosition_btn)
        self.findelement('css', batch_copy_BoxPosition_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('css', batch_copy_BoxPosition_comfirm)
        self.sleep(1)
        Screenshot(self.driver).get_img("环化明细表点击入库按钮，在弹框中录入样本盒信息、盒内位置信息后点击下一步","样本入库成功")

        self.clicks('xpath', storage_next)
        self.wait_loading()
        info=self.get_text('css','tr:nth-child(1) .cyclizationSchedule-tableCol-submitStatus')
        return info
        # 完成任务单

    # 完成任务单
    def complete_task(self):
        """完成任务单"""
        log.info(' 环化明细表进入结果表,完成任务单')
        self.clicks('css', detail_enter_result)
        self.wait_loading()
        self.clicks('css', result_complete_task_btn)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("文库富集结果表点击完成任务单按钮","任务单完成，状态改为完成")
        self.clicks('css', result_complete_task_confirm_btn)
        self.wait_loading()
        taskstatus = self.get_text('css', result_task_status)
        log.info('环化结果表完成任务单，任务单状态:%s' % taskstatus.strip())
        return taskstatus.strip()

    # 结果表样本流程环节写入Excel
    def write_data_to_excel(self):
        """
         根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
        """
        self.add_excel_xlxs(cyclization_next_step, cyclization_result, result_task_id)
        print('下一步流程写入成功')

    # 首页面查询已完成的样本任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(cyclization_file_path, 'lims号')
        log.info(' 环化首页面查询已完成的样本任务单')
        self.clicks('css', search_btn)
        self.sleep(0.5)
        self.input('css', lims_input, lims_id[0])
        self.sleep(0.5)
        self.clicks('css', search_btn)
        self.wait_loading()
        self.sleep(0.5)
        samples = self.findelements('xpath', sample_page_list)
        return len(samples)
