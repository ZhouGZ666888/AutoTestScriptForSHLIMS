# -*- coding: utf-8 -*-
# @Time    : 2021/12/16
# @Author  : guanzhong.zhou
# @File    : 21基因模块页面功能封装


import pyperclip, xlrd, yaml, re
from selenium.webdriver.common.keys import Keys
from PageElemens.genes_21_ele import *
from common import editYaml
from common.DataBaseConfig import executeSql
from common.all_path import esyjy_file_path, functionpageURL_path, sampledata_path, twentyonegene_file_path, \
    position_in_box_path
from common.screenshot import Screenshot
from common.xlsx_excel import get_lims_for_excel, read_excel_col, pandas_write_excel
from data.sql_action.execute_sql_action import twentyonegene_sql1, twentyonegene_sql2, twentyonegene_sql3
from uitestframework.basepageTools import BasePage
from common.logs import log


class Genes21Page(BasePage):
    """21基因页面方法封装"""

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

        return self.get_text('xpath', page_success_info)

    def goback_detail(self):
        """返回明细表"""
        log.info('点击按钮返回明细表')
        self.click_by_js('css', goback_detail)
        self.sleep(0.5)
        self.clicks('css', goback_page_info)
        self.wait_loading()

    # 新增任务单
    def add_task(self):
        """
        新建21基因任务单
        """
        # 这里调用自定义截图方法
        self.sleep(1)
        Screenshot(self.driver).get_img("点击左侧导航栏，进入21基因任务模块", "进入21基因模块成功，展示数据列表")

        log.info("21基因首页，点击新建按钮，进入样本待选表，新增21基因任务")
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
        log.info("21基因待选表核对lims号功能，并保存任务单号")
        lims_id_str = get_lims_for_excel(esyjy_file_path)
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
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击新建按钮，进入21基因待选表，选择样本", "进入待选表勾选样本后保存成功")

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
        log.info('点击按钮进入{}'.format(page))
        self.wait_loading()
        self.sleep(2)
        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    # 明细表录入Qubit浓度、体积、总量
    def detail_twentyonegene_date(self):
        """
        21基因明细表，录入Qubit浓度、体积、总量
        """
        log.info(" 21基因明细表，录入Qubit浓度、体积、总量")
        taskstatus = self.get_text('css', detail_task_id)  # 获取明细表任务单号
        sql1 = twentyonegene_sql1.format(re.findall(r'[A-Za-z0-9]+', taskstatus)[0])
        self.updata_sql(sql1)
        self.sleep(0.5)
        self.refresh()
        self.clicks('css', detail_save_result)
        self.wait_loading()

    # 21基因明细表选择批量入库类型、录入批量包装余量
    def detail_twentyonegene_batchdate(self):
        """21基因明细表选择批量入库类型、录入批量包装余量"""
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        log.info('21基因明细表，批量样本入库类型---余样入库')
        self.moved_to_element('css', batchStorageType)  # 入库弹框选择入库类型下拉框
        self.sleep(1)
        self.click_by_js('xpath', batchStorageType_choice)  # 入库弹框选择入库类型下拉值（临时库）
        self.sleep(0.5)
        log.info('21基因明细表，批量包装余量')
        self.clicks('css', handleBatchData)
        self.sleep(0.5)
        self.input('css', handleBatchData_input, 1)
        self.sleep(0.5)
        self.clicks('css', handleBatchData_confirm)
        self.sleep(0.5)
        log.info('21基因明细表，保存数据')
        self.clicks('css', detail_save_result)
        return self.get_pageinfo()

    # 明细表合并分析
    def detail_twentyonegene_merge(self):
        log.info(" 21基因明细表，明细表合并分析操作")
        # 样本全选
        self.sleep(2)
        self.clicks("css", detail_all_choice)
        log.info(" 21基因明细表，点击合并分析按钮")
        self.clicks('css', merge)
        self.sleep(0.5)
        log.info(" 合并分析弹框选择第一条作为主样本")
        self.clicks('css', merge_main_sample)

        # 取出设置主样本的lims号，存到临时文件，在明细表中取出进行提交
        lims_nub = self.get_text('css', merge_main_sample)
        datas = editYaml.read_yaml(sampledata_path)
        print(lims_nub)
        datas["twentyonegene_lims"] = lims_nub
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式
            yaml.safe_dump(datas, fs, allow_unicode=True)

        log.info("合并分析弹框点击确认")
        self.clicks('css', merge_main_btn)
        log.info("合并分析弹框点击继续")
        self.clicks('css', merge_main_continue_btn)
        info = self.get_pageinfo()
        self.wait_loading()
        return info

    # 明细表提交
    def detail_sumbit(self):
        """21基因明细表，样本提交操作"""
        log.info("21基因明细表样本提交---读取保存的合并分析主样本")
        datas = editYaml.read_yaml(sampledata_path)
        all_lims = self.findelements('css', all_samples)
        log.info("21基因明细表样本提交---明细表判断主样本，并点击选中主样本")
        for i in range(1, len(all_lims) + 1):
            lims_nub = self.get_text('css', samples_lims.format(i))
            self.sleep(0.5)
            if lims_nub == datas["twentyonegene_lims"]:
                self.clicks('css', samples_lims.format(i))
        log.info("点击提交按钮")
        self.clicks('css', detail_submit_btn)  # 提交按钮
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("21基因明细表点击提交按钮", "弹出提交确认提示框")
        self.clicks('css', detail_submit_comfirm)  # 提交弹框确认按钮
        info = self.get_pageinfo()
        self.wait_loading()
        return info

    # 明细表入库
    def detail_into_storage(self):
        """21基因明细表样本入库操作"""
        datas = editYaml.read_yaml(sampledata_path)
        all_lims = self.findelements('css', all_samples)
        log.info("21基因明细表样本入库---明细表判断主样本，并点击选中主样本")
        for i in range(1, len(all_lims) + 1):
            lims_nub = self.get_text('css', samples_lims.format(i))
            self.sleep(0.5)
            if lims_nub == datas["twentyonegene_lims"]:
                self.clicks('css', samples_lims.format(i))
        try:
            log.info('21基因明细表，样本入库操作')

            self.clicks('css', deposit_into_storage)  # 入库按钮
            self.sleep(0.5)
            self.clicks('css', storage_all_choice)  # 入库弹框全选按钮

            log.info('21基因明细表，样本入库选择入样本盒')
            self.clicks('css', batch_paste_sample_box)  # 入库弹框选择样本盒按钮
            self.wait_loading()
            self.input('css', target_storage, '自动化测试用(勿删)')
            self.sleep(0.5)
            self.clicks('css', select_sample_box_search)
            self.wait_loading()
            self.clicks('css', select_sample_box_choice)  # 入库弹框选选择样本盒值，默认选择列表第一条数据
            self.clicks('css', select_sample_box_comfirm)  # 入库弹框选选择样本盒弹框，确认按钮
            self.sleep(0.5)

            log.info('21基因明细表，样本入库录入盒内位置')

            taskstatus = self.get_text('css', detail_task_id)  # 获取任务单号
            lims_id = executeSql.test_select_limsdb(
                twentyonegene_sql3.format(taskstatus[5:].strip()))  # 从数据库获取当前任务单号下样本lims号

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
            Screenshot(self.driver).get_img("21基因明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步", "样本入库成功")

            self.clicks('css', storage_next)
            self.wait_loading()

            self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=3000')
            self.sleep(0.5)
            pageInfo = self.get_text('css', sumbit_status)
            print(pageInfo)
            return pageInfo
        except Exception as info:
            print(info)

    # 结果表表单录入
    def result_twentyonegene_date(self):
        """
        21基因结果表盒内位置录入
        """
        log.info(" 21基因结果表，进入体积、进入总量")
        taskstatus = self.get_text('css', result_task_id)  # 获取明细表任务单号
        sql1 = twentyonegene_sql2.format(re.findall(r'[A-Za-z0-9]+', taskstatus)[0])
        self.updata_sql(sql1)
        self.sleep(0.5)
        self.refresh()

    # 21基因结果分析
    def result_twentyonegene_analysis(self):
        """
        21基因结果分析
        """
        log.info(" 21基因结果表，点击21基因结果分析")
        self.clicks('css', result_analysis)

        log.info("切换到新打开的页面")
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.switch_to_window(handle)
        # 这里调用自定义截图方法
        self.sleep(3)
        Screenshot(self.driver).get_img("点击进入21基因分析结果表按钮", "进入结果表成功")
        log.info("---21基因分析任务信息页面，录入详情数据---")
        log.info("21基因分析任务信息页面，录入算法版本")

        self.clicks('css', aly)
        self.clicks('css', aly_choice)
        self.sleep(0.5)

        log.info("21基因分析任务信息页面，录入【结果内参平均值是否合格】下拉选择")
        self.clicks('css', isEligible)
        self.clicks('css', isEligible_choice)
        self.sleep(0.5)

        log.info("21基因分析结果表,导入数据")
        self.clicks('css', batchImport)
        self.sleep(0.5)
        # 导入文件模板复制出模板数据
        data = xlrd.open_workbook(twentyonegene_file_path)
        num_list = []
        for index in range(0, 22):
            tables = data.sheets()[0]
            vals = tables.row_values(index)
            imp_data = '\t'.join(map(str, vals))
            num_list.append(imp_data)
        print("\n".join(map(str, num_list)))
        pyperclip.copy("\n".join(map(str, num_list)))

        self.clicks('css', batchImport_input)
        self.findelement('css', batchImport_input).send_keys(Keys.CONTROL, 'v')
        self.sleep(0.5)
        self.clicks('css', batchImport_comfirm)
        self.sleep(1)

    # 21基因结果分析保存并完成
    def result_twentyonegene_analysis_complete(self):
        """
        21基因分析结果表,保存并完成
        :return:
        """
        log.info("21基因分析结果表,保存操作")
        self.clicks('css', twentyonegene_analysis_save)
        self.wait_loading()
        self.sleep(0.5)
        log.info("21基因分析结果表,完成操作")
        self.clicks('css', twentyonegene_analysis_complete)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("21基因分析结果表,点击完成按钮", "分析结果表完成操作")

        self.wait_loading()
        self.sleep(0.5)

        log.info("调用关闭21基因分析页面方法")
        self.close_analysis_page()

    def close_analysis_page(self):
        """
        关闭21基因分析页面
        """
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                self.close()
                # 切换到新窗口句柄，即新打开的页面
                self.switch_to_window(handle)
        self.sleep(1)

    # 提交任务单
    def sumbit_task(self):
        """
        提交并完成任务单
        """
        log.info("提交任务单")
        self.clicks('css', result_all_choice)
        self.sleep(0.5)
        self.clicks('css', result_submit)
        self.sleep(1)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("21基因结果表,点击提交任务单", "弹出提交确认弹框")
        self.clicks('css', result_submit_comfirm)
        self.wait_loading()
        self.sleep(0.5)

    def complete_task(self):
        """
        完成任务单
        """
        log.info("完成任务单")
        self.clicks('css', result_complete_task_btn)
        self.wait_loading()
        self.sleep(1)
        Screenshot(self.driver).get_img("21基因结果表,点击完成任务单", "任务单完成，状态改为完成")
        taskstatus = self.get_text('css', detail_task_status)
        return taskstatus[6:].strip()

    # 21基因任务列表查询样本所在任务单
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(esyjy_file_path, 'lims号')

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
