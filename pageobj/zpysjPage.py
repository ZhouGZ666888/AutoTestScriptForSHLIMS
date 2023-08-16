# -*- coding: utf-8 -*-
# @Time    : 2023/03/02
# @Author  : guanzhong.zhou
# @File    : 质谱仪上机模块页面方法封装
# -*-*************************************************************************************-*-

from datetime import datetime
import pyperclip, xlrd
from selenium.webdriver.common.keys import Keys
from PageElemens.zpysj_ele import *
from common.all_path import zpy_file_path, position_in_box_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from common.xlsx_excel import get_lims_for_excel, get_firstDownloadFile, pandas_write_excel, read_excel_col
from data.sql_action.execute_sql_action import Massspectr_sample_no, Massspectr
from uitestframework.basepageTools import BasePage
from common.logs import log
import pandas as pd


class MassspectrPage(BasePage):
    """
    质谱仪上机页面方法封装
    """

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
        新建质谱仪上机任务单
        """
        log.info("质谱仪上机首页，点击新建按钮，进入样本待选表，新增质谱仪上机任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()

        log.info("选择任务类型:多肽上机")
        self.click_by_js('css', task_type)
        self.sleep(0.5)
        self.clicks('css', task_type_choice)
        self.wait_loading()

        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()


    # 待选表校验lims号
    def check_lims_num(self):
        """
        待选表核对lims号功能，并保存任务单号
        """
        lims_id_str = get_lims_for_excel(zpy_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(1)
        self.input('css', check_lims_sample_number_textarea, lims_id_str)
        self.sleep(0.5)
        try:
            self.clicks('css', check_lims_sample_number_confirm)
        except Exception as a:
            print(a)
            log.info('部分样本号未被查询到，请检查样本号是否正确、是否换行且使用英文逗号进行分割')
        self.wait_loading()

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.click_by_js('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)

        Screenshot(self.driver).get_img("质谱仪上机待选表核对lims号功能，并保存任务单号")
        pageInfo = self.get_pageinfo()
        self.sleep(1)
        log.info('选中核对后的样本，进入明细表')
        self.clicks('css', enter_detail_list_btn)  # 进入明细表
        self.wait_loading()

        return pageInfo

    # 明细表录入批量数据
    def detail_libconstruction(self):
        """
        质谱仪上机明细表，选择入库信息、批量包装余量、录入96孔版位置
        """
        self.click_by_js('css', detail_all_choice)  # 列表全选按钮
        log.info("质谱仪上机明细表录入批量数据")
        self.clicks('css', batchData)  # 点击批量数据
        self.sleep(0.5)
        log.info("批量数据---液相柱")
        self.clicks('css', liquidColumn)  # 批量数据---液相柱
        self.sleep(0.5)
        self.clicks('xpath', liquidColumn_choice)
        self.sleep(0.5)
        log.info("批量数据---录入包装余量")
        self.input('css', SamplePkgAmt, 1)  # 录入包装余量
        self.sleep(0.5)
        log.info("批量数据---液质联用仪器号")
        self.clicks('css', lcmsModel)  # 液质联用仪器号
        self.sleep(0.5)
        self.clicks('xpath', lcmsModel_choice)
        log.info("批量数据---扫描模式")
        self.clicks('css', scanMethod)  # 扫描模式
        self.sleep(0.5)
        self.clicks('xpath', scanMethod_choice)

        self.clicks('css', confirm_btn)  # 确认
        self.sleep(0.5)

        self.clicks('css', save_result)
        self.wait_loading()

    # 明细表导出样本，并对列表中样本进行编辑
    def detail_exportData(self):
        """
        导出样本列表，并对列表中样本进行编辑，录入各样本字段的值
        """
        taskstatus = self.get_text('css', task_id)  # 获取任务单号
        executeSql.test_updateByParam(Massspectr.format(taskstatus[5:].strip()))  # 数据库给部分字段赋值
        self.refresh()

        log.info("质谱仪上机明细表导出样本列表")
        self.clicks('css', export_btn)
        self.wait_loading()
        self.sleep(1)

        log.info('在设置的下载文件夹下，获取最新导出的样本——项目信息文件')
        filepath = get_firstDownloadFile()

        log.info('编辑导出样本列表的值')
        try:
            data = pd.read_excel(filepath, header=0)
            data["组别"] = 5
            data["复溶体积μL"] = "22"
            data["梯度时间mi"] = "5"
            data["上机序列号"] = 'SNJ' + datetime.now().strftime('%Y%m%d%H%M')
            data["项目编号"] = 'J022'
            data.to_excel(filepath, index=False)
        except  IOError as EEROR1:
            print(EEROR1)
        except  Exception as EEROR2:
            print(EEROR2)
        self.sleep(1)

    # 导入样本列表文件
    def detail_importData(self):
        """
        把编辑好的样本文件导入系统
        """
        log.info('导入已编辑的样本列表Excel文件')
        filepath = get_firstDownloadFile()
        self.clicks('css', import_btn)
        # 设置页面导入按钮为可见
        self.executeJscript(
            "document.querySelector('.dialog-csv-import .el-dialog__body input').style.setProperty('display','block','important');")
        self.sleep(1)
        self.input('css', upload_sampleInfo_btn, filepath)
        Screenshot(self.driver).get_img("导入已编辑的样本列表Excel文件")
        self.sleep(1)
        self.click_by_js('css', import_confirm_btn)
        self.sleep(1)
        self.click_by_js('css', detail_all_choice)  # 列表全选按钮
        self.clicks('css', save_result)
        self.wait_loading()

    # 确认上机、生成samplesheet
    def detail_confirm_sequencing(self):
        """确认上机、生成samplesheet"""
        self.clicks('css', confirmSequencing)
        self.sleep(0.5)
        self.clicks('xpath', confirmSequencing_confirm)
        self.sleep(1)

    # 明细表提交
    def detail_submit(self):
        """
        质谱仪上机明细表，样本提交操作
        :return:
        """
        self.sleep(1)
        log.info("质谱仪上机明细表样本提交")
        self.clicks('css', detail_all_choice)
        self.click_by_js('css', submit)  # 提交按钮
        self.sleep(1)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("质谱仪上机明细表提交")
        self.clicks('css', submit_comfirm)  # 提交弹框确认按钮
        self.wait_loading()

    # 明细表入库
    def detail_into_storage(self):
        """
        质谱仪上机明细表样本入库操作
        """
        try:
            log.info('质谱仪上机明细表，样本入库操作')

            self.clicks('css', deposit_into_storage)  # 入库按钮
            self.sleep(0.5)
            self.clicks('css', storage_all_choice)  # 入库弹框全选按钮

            log.info('质谱仪上机明细表，样本入库选择入样本盒')
            self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
            self.wait_loading()
            self.input('css', target_storage, '自动化测试用(勿删)')
            self.sleep(0.5)
            self.clicks('css', select_sample_box_search)
            self.wait_loading()
            self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
            self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
            self.sleep(0.5)

            log.info('质谱仪上机明细表，样本入库录入盒内位置')
            taskstatus = self.get_text('css', task_id)  # 获取任务单号
            lims_id = executeSql.test_select_limsdb(
                Massspectr_sample_no.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

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
            Screenshot(self.driver).get_img("质谱仪上机明细表入库")

            self.clicks('css', storage_next)
            self.wait_loading()

            self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3200;')
            self.sleep(1)
            pageInfo = self.get_text('css', detail_sumbit_status)
            print(pageInfo)
            return pageInfo
        except Exception as info:
            print(info)

    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        log.info(' 质谱仪上机模块，查询实验样本所在任务单')
        lims_id = read_excel_col(zpy_file_path, 'lims号')
        self.clicks('css', search)
        self.sleep(1)
        self.input('css', search_lims_sample_num, lims_id[0])
        print(lims_id[0][0])
        self.sleep(1)
        self.clicks('css', search_confirm)
        self.wait_loading()
        samples = self.findelements('xpath', sample_page_list)
        return len(samples)
