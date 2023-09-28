# -*- coding: utf-8 -*-
# @Time    : 2021/11/22
# @Author  : guanzhong.zhou
# @File    : 病理检验模块页面功能封装
import  datetime
from PageElemens.pathologycheck_ele import *
from common.editYaml import *
from common.all_path import pathologycheck_file_path, functionpageURL_path
from common.screenshot import Screenshot
from common.xlsx_excel import get_lims_for_excel, read_excel_col
from uitestframework.basepageTools import BasePage
from common.logs import log


class WorkSheet(BasePage):
    """
    病理检验页面功能封装
    """
    str_time = datetime.datetime.now().strftime('%Y.%m.%d')  # 获取当前时间

    def add_task(self):
        """
        新增病理任务
        """
        log.info('点击新增按钮，新增病理任务')
        self.click_by_js('css', add)
        self.wait_loading()
        self.sleep(0.5)

    def select_tasktype_sop(self, index):
        """
        选择任务类型、sop种类,
        1.HE
        2.PD-L1(28-8)
        3.PD-L1(22C3)
        4.PD-L1(SP142)
        5.PD-L1(SP263)
        6.CD4
        7.CD8
        :param index: int型参数，不同index代表不同病理类型，见上
        """

        self.clicks('css', task_type)
        self.sleep(0.5)

        self.clicks('css', task_type_chioce.format(index))
        self.wait_loading()
        log.info('病理待选表，选择sop')

        self.clicks('css', select_sop)
        self.sleep(0.5)
        self.clicks('css', select_sop_chioce)
        self.wait_loading()
        self.sleep(0.5)

    def check_lims_num(self):
        """
        核对lims号功能
        """
        lims_nub = get_lims_for_excel(pathologycheck_file_path)

        log.info('获取样本接收的带病理标记的样本lims号，核对lims样本号')
        self.clicks('css', check_lims_sample_number)
        self.sleep(0.5)
        print(lims_nub)
        self.input('css', check_lims_sample_number_textarea, lims_nub)
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()

    def add_select_task_or_save(self):
        log.info('全选核对后的样本号，加入并保存任务单')
        self.clicks('css', all_chioce)
        self.sleep(0.5)
        self.clicks('css', addSelect_or_save_btn)
        pageinfo = self.get_pageinfo()
        Screenshot(self.driver).get_img("病理检验待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")
        return pageinfo

    def enter_result_list(self):
        """
        进入结果表，获取结果表URL地址
        """
        log.info('点击按钮进入结果表')
        urldata = read_yaml(functionpageURL_path)

        self.clicks('css', enter_result_list_btn)
        self.wait_loading()
        self.sleep(5)

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

    def edit_result_pageinfo(self):
        """
        编辑、录入HE病理结果表表单信息
        """
        # now_time = datetime.datetime.now()
        # str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
        log.info('进入HE病理结果表')
        log.info('全部选中样本')

        self.click_by_js('css', result_all_chioce)
        log.info('批量实验数据...')
        self.clicks('css', batch_laboratory_data)  # 批量实验数据按钮
        self.sleep(0.5)
        self.input('css', necrotic_cell_ratio, 10)  # 坏死细胞比例（%）文本录入框
        self.sleep(0.5)
        self.clicks('css', quality_control_result)  # 质控结果下拉选择
        self.sleep(0.5)
        self.clicks('xpath', quality_control_result_value)  # 质控结果下拉选择值
        self.sleep(0.5)
        self.clicks('css', test_result)  # 检验结果下拉选择
        self.sleep(0.5)
        self.clicks('xpath', test_result_value)  # 检验结果下拉选择值
        self.sleep(0.5)
        self.input('css', number_of_labels_printed, 1)  # 标签打印份数文本框
        self.sleep(0.5)
        self.input('css', stained_sections_socation, '测试')
        self.clicks('css', confirm_btn)  # 批量实验数据，确认按钮
        self.sleep(1)

        log.info('批量实验员/日期数据...')
        self.clicks('css', batch_laboratory_personnel_data)  # 批量实验员/日期按钮
        self.input('css', laboratory_personnel, "F")  # 实验员文本录入
        self.wait_loading()
        self.clicks('css', laboratory_personnel_value)  # 实验员文本录入，选择人员
        self.input('css', laboratory_test_date, self.str_time)  # 录入实验日期
        self.clicks('css', batch_laboratory_personnel_data_confirm)  # 批量实验员/日期，录入后点击确认按钮
        self.sleep(1)

        log.info('批量诊断者/日期数据...')
        self.clicks('css', batch_diagnosis_data)  # 批量诊断者/日期按钮
        self.input('css', batch_diagnosis, 'Z')  # 诊断者文本录入
        self.wait_loading()
        self.clicks('css', batch_diagnosis_value)  # 诊断者选择，默认第一条
        self.input('css', diagnosed_date, self.str_time)  # 录入诊断日期
        self.clicks('css', batch_diagnosis_data_confirm)  # 批量诊断者/日期，确认按钮
        self.sleep(2)

        log.info('录入Tumor cell content数据值...10')
        eles = self.findelements('css', all_sample)
        for i in range(len(eles)):
            j = i + 1
            self.clicks('css', all_sample_one_by_one.format(j))
            self.input('css', all_tumor_cell_content_input.format(j), 10)
            self.sleep(1)
        log.info('录入Tumor cell content数据值结束')

    def edit_result_pageinfo_PD(self):
        """
        编辑、录入PD-L1(28-8)病理结果表表单信息
        """

        log.info('进入PD-L1(28-8)病理结果表')
        log.info('全部选中样本')

        self.click_by_js('css', all_chioce_pd)
        log.info('选择癌种类型...')
        self.clicks('css', batch_cancer_type_pd)  # 选择癌种信息弹框
        self.sleep(0.5)
        self.clicks('css', cancer_type)  # 癌种类型选择下拉框
        self.sleep(0.5)
        self.clicks('xpath', cancer_type_chioce)  # 癌种下拉类型值选择，第三条
        self.sleep(0.5)
        self.clicks('css', cancer_type_confirm)  # 癌种选择弹框，确认按钮
        self.sleep(1)

        log.info('批量实验数据...')
        self.clicks('css', batch_laboratory_data_pd)  # 批量实验数据按钮
        self.sleep(0.5)
        log.info('TPS文本录入...')
        self.input('css', tps, 10)  # TPS文本录入
        log.info('CPS文本录入...')
        self.input('css', cps, 10)  # CPS文本录入
        log.info('标签打印份数文本框...')
        self.input('css', number_of_labels_printed_pd, 1)  # 标签打印份数文本框
        self.sleep(0.5)
        log.info('选择活肿瘤细胞数目...')
        self.clicks('css', Number_of_viable_tumor_cell)  # 活肿瘤细胞数目≥100个为合格,下拉选择弹框
        self.sleep(0.5)
        self.clicks('xpath', Number_of_viable_tumor_cell_choice)  # 活肿瘤细胞数目≥100个为合格,下拉值选择
        self.sleep(0.5)
        log.info('选择质控片染色结果下拉...')
        self.clicks('css', quality_contol_sample_staining_result)  # 质控片染色结果下拉按钮
        self.sleep(0.5)
        self.clicks('xpath', quality_contol_sample_staining_result_choice)  # 质控片染色结果下拉按钮值选择
        self.sleep(0.5)
        log.info('选择测试结果...')
        self.clicks('css', test_result_pd)  # 测试结果下拉按钮
        self.clicks('xpath', test_result_pd_choice)  # 测试结果下拉值选择按钮
        self.sleep(0.5)
        self.clicks('css', batch_laboratory_data_pd_confirm)  # 批量实验数据弹框确认按钮
        self.sleep(1)

        log.info('批量实验员/日期数据...')
        self.clicks('css', batch_laboratory_personnel_data_pd)  # 批量实验员/日期按钮
        self.sleep(0.5)
        self.input('css', laboratory_personnel_pd, "F")  # 实验员文本录入
        self.wait_loading()
        self.clicks('css', laboratory_personnel_value_pd)  # 实验员文本录入，选择人员
        self.sleep(0.5)
        self.input('css', laboratory_test_date_pd, self.str_time)  # 录入实验日期
        self.sleep(0.5)
        self.clicks('css', batch_laboratory_personnel_data_confirm_pd)  # 批量实验员/日期，录入后点击确认按钮
        self.sleep(1)

        log.info('批量诊断者/日期数据...')
        self.clicks('css', batch_diagnosis_data_pd)  # 批量诊断者/日期按钮
        self.sleep(0.5)
        self.input('css', batch_diagnosis_pd, 'Z')  # 诊断者文本录入
        self.wait_loading()
        self.clicks('css', batch_diagnosis_value_pd)  # 诊断者选择，默认第一条
        self.sleep(0.5)
        self.input('css', diagnosed_date_pd, self.str_time)  # 录入诊断日期
        self.sleep(0.5)
        self.clicks('css', batch_diagnosis_data_confirm_pd)  # 批量诊断者/日期，确认按钮
        self.sleep(1)

    def sava_result(self, ele):
        """
        结果表保存任务单
        """
        log.info('结果表保存任务单')
        self.clicks('css', ele)  # 点击结果表保存按钮
        self.wait_loading()

    def submit_result(self, ele1, ele2):
        """
        结果表提交任务单
        """
        log.info('结果表提交任务单')
        self.click_by_js('css', ele1)  # 点击全选按钮，选中全部样本
        self.sleep(0.5)
        self.clicks('css', ele2)  # 点击结果表提交按钮

    def wait_pageinfo(self):
        """
        等待页面提示信息结束
        """
        self.wait_pageinfo_end()
        self.sleep(3)

    def serach_task(self):
        """
        首页面查询已完成的样本任务单
        """
        print('获取样本号')
        lims_nub = read_excel_col(pathologycheck_file_path, 'lims号')

        self.clicks('css', search)
        self.sleep(0.5)
        self.input('css', search_lims_sample_num, lims_nub[0])
        self.sleep(0.5)
        self.clicks('css', search_confirm)
        self.wait_loading()
        print('进入页面')
        if self.isElementExists('xpath', sample_num):
            samples = self.findelements('xpath', sample_num)
            print(len(samples))
            return len(samples)
        else:
            return 0

    def enter_function_page(self, url):
        """
        进入指定url页面
        """
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()
        self.sleep(1)

    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Saved successfully---结果表保存、提交成功
        """
        if self.isElementExists('xpath', page_success_info):
            return self.get_text('xpath', page_success_info)
        else:
            return None
