# -*- coding: utf-8 -*-
# @Time    : 2021/11/11
# @Author  : guanzhong.zhou
# @File    : 样本处理页面功能封装
import yaml
from PageElemens.sampleProcessing_ele import *
from common import editYaml
from common.all_path import functionpageURL_path, sampledata_path
from common.editYaml import read_yaml, save_yaml
from common.screenshot import Screenshot
from common.xlsx_excel import get_lims_for_excel, read_excel_col
from data.sql_action.execute_sql_action import next_step_sql, ybcl_detail_sql
from uitestframework.basepageTools import BasePage
from conf.config import *
from common.logs import log


class SampleProcessingPage(BasePage):
    """
    样本处理，待选表、明细表、结果表页面功能封装
    """

    # 新增任务单
    def add_task(self):
        """
        新建样本处理任务单
        """
        log.info("样本处理首页，点击新建按钮，进入样本待选表，新增样本处理任务")
        self.clicks('css', add_sample_process_task)
        self.wait_loading()
        self.wait_loading()
        self.sleep(0.5)

        log.info("选择样本类型")
        self.clicks('css', task_type)
        self.sleep(0.5)
        self.clicks('css', task_type_choice)
        self.wait_loading()
        self.sleep(0.5)

        log.info("选择sop")
        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_choice)
        self.wait_loading()
        self.sleep(1)

    # 待选表校验lims号
    def check_lims_num(self):
        """
        核对lims号功能，并保存任务单号
        根据样本接收模块样本类型，写入到Excel中样本类型顺序为：1.FF白片——核酸提取-破碎；2.ED抗凝血-体液样本分离；3.骨冷冻组织-21基因；4.DNA文库-SR上机
        """
        limsNub = get_lims_for_excel(sampleprocessing_file_path)
        log.info('获取接样流程中的lims样本号,核对lims号是否存在')
        self.clicks('css', check_lims_sample_num)
        self.sleep(0.5)

        self.input('css', check_lims_sample_number_textarea, limsNub)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()

        log.info('选中核对后的样本，点击【加入选中样本&保存】')
        self.clicks('css', all_choice)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)
        pageinfo = self.get_pageinfo()
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本处理待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")
        self.wait_loading()
        self.sleep(0.5)

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


        return pageinfo

    # 进入明细表或结果表
    def enter_result_list(self, ele, page):
        """
        进入下一节点，获取下一节点URL地址
        """
        urldata = editYaml.read_yaml(functionpageURL_path)

        self.clicks('css', ele)
        log.info('点击按钮进入{}'.format(page))
        # eles = self.findelement('css', goback_page_info)
        if self.isDisPlayed('css', goback_page_info):
            self.clicks('css', goback_page_info)
            self.wait_loading()
        else:
            self.wait_loading()

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    def goback_detail(self):
        """
        返回明细表

        """

        urldata = editYaml.read_yaml(functionpageURL_path)
        log.info('点击按钮返回明细表')
        self.click_by_js('css', goback_detail)

        self.clicks('css', goback_page_info)
        self.wait_loading()
        self.sleep(1)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    # 打开指定页面
    def enter_function_page(self, url):
        """
        进入指定url页面
        """
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
        self.sleep(0.5)

    # 明细表数据等录入操作
    def sample_detail(self):
        """
        样本处理明细表数据录入、提交操作
        """
        self.sleep(0.5)
        log.info("全选样本，点击生成排序号")
        self.click_by_js('css', create_sort_number)  # 生成排序号
        # print('已生成排序号')
        self.sleep(0.5)
        self.clicks('css', detail_all_choice)  # 样本列表数据全选
        self.sleep(0.5)
        # print('已生成排序号')

        log.info("选择批量入库类型：样本入库")
        self.moved_to_element('css', batch_storage_type)  # 批量入库类型下拉框
        self.sleep(0.5)
        self.clicks('xpath', batch_actual_data_choice)  # 选择批量入库类型下拉值：临时库

        log.info("录入批量实测数据")
        self.clicks('css', batch_actual_data)  # 批量实测数据
        self.sleep(0.5)
        self.input('css', Acual_sample_amount, 20)  # 批量实测数据-样本计量（实测）
        self.sleep(0.5)
        self.input('css', Actual_sample_package_amount, 1)  # 批量实测数据-包装量（实测）
        self.sleep(0.5)
        self.clicks('css', batch_actual_data_btn)  # 批量实测数据弹框按钮
        self.sleep(0.5)

        log.info("录入批量余样数据")
        self.clicks('css', batch_remaining_data)  # 批量余样数据
        self.sleep(0.5)
        self.input('css', remaining_sample_amount, 15)  # 计量余样录入框
        self.sleep(0.5)
        self.input('css', remaining_sample_package_amount, 1)  # 包装余量录入框
        self.sleep(0.5)
        self.clicks('css', batch_remaining_data_confirm)  # 批量余样弹框确认按钮
        self.sleep(0.5)

        log.info("选择库位类型：临时库")
        self.clicks('css', target_storage_type)  # 目标库位类型下拉框
        self.sleep(0.5)
        self.click_by_js('xpath', target_storage_type_choice)  # 目标库位类型下拉值
        self.sleep(0.5)

        log.info("选择样本盒")
        self.clicks('xpath', select_sample_box)  # 选择样本盒按钮
        self.wait_loading()
        self.input('css', target_storage, '自动化测试用(勿删)')
        self.sleep(0.5)
        self.clicks('css', select_sample_box_search)
        self.wait_loading()
        self.clicks('css', select_sample_box_choice)  # 选择样本盒值，默认选择列表第一条数据
        self.sleep(0.5)
        self.clicks('css', select_sample_box_comfirm)  # 选择样本盒弹框，确认按钮
        self.sleep(1)

        log.info("明细表保存")
        self.clicks('css', detail_save_result)
        self.wait_loading()

        log.info("明细表插入盒内位置")
        taskstatus = self.get_text('css', detail_task_id)
        self.updata_sql(ybcl_detail_sql.format(taskstatus[5:].strip()))
        self.refresh()
        self.wait_loading()
        self.sleep(0.5)

    # 明细表提交
    def detail_sumbit(self):
        log.info("提交样本")
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        self.click_by_js('css', submit_btn)
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本处理明细表点击提交按钮","弹出提交确认按钮")
        self.click_by_js('css', submit_comfirm)
        self.wait_loading()
        self.sleep(1)
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=1890')
        self.sleep(0.5)
        samples_status = self.get_text('css', submit_status)
        return samples_status

    # 明细表入库操作
    def deposit_into_storage(self):
        """
        入库操作
        """
        log.info("选中样本进行入库操作")
        self.clicks('css', detail_all_choice)  # 获取所有样本数量
        self.sleep(0.5)
        self.clicks('xpath', deposit_into_storage)  # 入库按钮
        self.sleep(0.5)
        self.clicks('css', storage_all_choice)  # 入库弹框中全选样本
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本处理明细表点击入库按钮，在弹框中录入库位信息和盒内位置后点击下一步","样本入库成功")
        self.clicks('css', storage_next)  # 入库弹框点击下一步按钮
        self.wait_loading()

        # 获取一条写入报告的上机样本的实验室号
        bioinformatic_negative = self.get_text('css', detail_labNub)
        print('获取一条写入报告的上机样本的实验室号', bioinformatic_negative)
        datas = read_yaml(sampledata_path)
        datas["bioinformatic_negative_lab_num"] = bioinformatic_negative
        save_yaml(sampledata_path, datas)

        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=1890')
        self.sleep(0.5)
        samples_status = self.get_text('css', submit_status)
        return samples_status

    # 结果表数据处理、提交
    def sample_result_process_sumbit(self):
        """
        结果表数据处理、提交
        """
        self.sleep(1)
        self.clicks('css', result_all_choice)  # 样本列表数据全选按钮
        self.sleep(1)
        log.info("选中样本，录入批量数据")
        self.clicks('css', batch_data)
        self.sleep(1)
        self.input('css', product_amount, 20)  # 批量数据弹框，产物计量
        self.sleep(0.5)

        self.clicks('css', sample_amount_unit)  # 批量数据弹框，计量单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', sample_amount_unit_choice)  # 批量数据弹框，计量单位下拉值
        self.sleep(0.5)
        self.input('css', sample_package_amount, 1)  # 批量数据弹框，产物包装量文本框
        self.sleep(0.5)
        self.clicks('css', sampl_package_amount_unit)  # 批量数据弹框，包装单位下拉框
        self.sleep(0.5)
        self.clicks('xpath', sampl_package_amount_unit_choice)  # 批量数据弹框，包装单位下拉值
        self.sleep(0.5)
        self.input('css', number_of_labels_printed, 1)  # 批量数据弹框,标签打印份数
        self.sleep(0.5)
        self.clicks('css', batch_data_comfirm)
        self.sleep(0.5)
        print('打印')
        ssfs = self.findelements('css', samples_lims)
        for i in ssfs:
            print(i.text)
        self.sleep(1)
        log.info("录入数据后，点击提交样本")
        self.clicks('css', result_submit)  # 点击提交
        self.wait_loading()
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本处理结果表点击提交按钮","弹出提交确认按钮")
        self.clicks('css', result_submit_comfirm)  # 点击提交确认
        self.wait_loading()

        # 获取样本提交状态表单文本
        self.executeJscript('document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=1890')
        self.sleep(0.5)
        submit_info = self.get_text('css', result_sample_status)
        print('样本处理结果表提交状态', submit_info)
        return submit_info

    # 结果表下一步样本写入对应Excel
    def write_data_to_excel(self):
        """
         根据结果表样本下一步流程，把对应的样本lims号、实验室号、下一步流程以追加形式写入该流程的Excel
        """
        # 样本数据写入流转表
        self.add_excel_xlxs(next_step_sql, preparation_result, result_task_id)
        self.sleep(1)

    # 结果表完成
    def complete_task(self):
        """
        完成任务单
        """
        log.info("点击完成任务单")
        self.clicks('css', goResult)
        self.wait_loading()
        self.sleep(1)
        self.click_by_js('css', complete_task_btn)
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本处理结果表点击完成任务单按钮","完成任务单成功，状态改为完成")
        log.info("获取任务单完成状态")
        taskstatus = self.get_text('css', task_status)
        print(taskstatus)
        self.sleep(0.5)

        log.info("样本处理任务单号写入临时数据")
        # 获取任务单号
        taskID = self.get_text('css', result_task_id)
        print(taskID[5:].strip())

        # 把样本处理任务单号写入临时文件，到报告处理环节，取出处理任务单号，进行数据库查询，获取任务单下lims号和实验室号
        taskID_nub = editYaml.read_yaml(sampledata_path)
        taskID_nub["sampleprocessing_reportprocess_taskid"] = taskID[5:].strip()
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(taskID_nub, fs, allow_unicode=True)
        print("写入后的临时文件内容：", taskID_nub)

        return taskstatus

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

    # 等待页面提示消失
    def wait_pageinfo(self):
        """
        等待页面提示信息结束
        """
        self.wait_pageinfo_end()
        self.sleep(3)

    # 任务单列表检索
    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        lims_id = read_excel_col(sampleprocessing_file_path, 'lims号')

        self.clicks('css', search)
        self.sleep(0.5)
        self.input('css', search_lims_sample_num, lims_id[0])
        self.sleep(0.5)
        self.clicks('css', search_confirm)
        self.wait_loading()
        samples = self.findelements('xpath', sample_page_list)
        return len(samples)


if __name__ == '__main__':
    # lims_nub = read_excel_xlsx_list_col(all_path.sampleprocessing_file_path, 0, 'lims号')
    # print(lims_nub[3][0])
    pass
    # we = SampleProcessingPage(BasePage)
    #
    # we.write_sample()
