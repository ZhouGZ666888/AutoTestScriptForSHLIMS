# -*- coding: utf-8 -*-
# @Time    : 2022/02/23
# @Author  : guanzhong.zhou
# @File    : 样本消息通知模块页面方法封装


from common.editYaml import *
from common.all_path import sampledata_path
from common.screenshot import Screenshot
from common.enter_tab import EnterTab
from PageElemens.nucleicAcidExtraction_ele import *
from pageobj.nucleicAcidExtractionPage import NucleicAcidExtractionPage
from PageElemens.samplemsgnotice_ele import *
from data.sql_action.execute_sql_action import sampleMsgNotice
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleMsgNoticePage(BasePage):
    """
    样本消息通知方法封装
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.enter = EnterTab(self.driver)
        self.hstq = NucleicAcidExtractionPage(self.driver)

    def get_notice_sample(self):
        """
        准备发送通知的样本数据，以核酸提取明细表为例，从数据库获取待选表数据，加入到明细表
        """
        # 执行sql语句，获取核酸提取待选表中一条样本号
        result = self.select_sql(sampleMsgNotice)
        lims_nub = [i['previous_sample_id_lims'] for i in result]
        print(lims_nub)

        # 把获得的lims样本号存入临时文件，在样本信息通知处理完后，根据该lims号搜索通知任务单
        taskID_nub = read_yaml(sampledata_path)
        taskID_nub["samplemsgnotice"] = lims_nub[0]
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(taskID_nub, fs, allow_unicode=True)

        return lims_nub

    def add_sample_notice_task(self):
        """
        新建样本通知消息任务
        """
        # 调用获取样本号方法
        lims_nub = self.get_notice_sample()

        log.info("新建消息通知，点击新建，录入样本lims号")
        self.clicks('css', add_send)
        self.sleep(0.5)
        self.input('css', samplesearch_textarea, lims_nub[0])
        self.sleep(0.5)
        self.clicks('css', samplesearch_textarea_next)
        self.sleep(0.5)

        log.info('填入通知内容，并发送消息')
        self.clicks('css', notice_info)
        self.input('css', notice_info_input, '测试通知消息')

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本消息通知，点击新建按钮，新建样本通知消息任务","打开新建消息通知弹框成功")

        self.clicks('css', comfirm_send_btn)
        self.wait_loading()

    # 核酸提取模块新建任务单
    def add_extraction_task(self):
        """
        核酸提取模块新建任务单
        """
        lims_nub = self.get_notice_sample()

        log.info('调用进入模块方法，进入核酸提取模块')
        self.enter.enter_test_center()
        self.enter.enter_extraction()

        log.info('调用核酸提取页面方法，新建提取任务')
        self.hstq.add_task()

        log.info('核酸提取待选表搜索出发送消息的样本lims号')
        self.clicks('css', check_lims_sample_num)
        self.sleep(0.5)

        self.input('css', check_lims_sample_number_textarea, lims_nub[0])
        self.sleep(0.5)
        self.clicks('css', check_lims_sample_number_confirm)
        self.wait_loading()
        self.sleep(0.5)

        log.info('选中核对后的样本，点击【加入选中样本&保存】,并进入待选表')
        self.click_by_js('css', all_choice)
        self.sleep(1)
        self.clicks('css', addSelect_or_save_btn)
        self.wait_loading()
        self.clicks('css', enter_detail_list_btn)
        self.wait_loading()

    def notice_process(self):
        """
        消息通知处理。对样本发送消息后，该样本进入提取明细表模块
        """
        log.info("对接受到的样本通知消息进入处理")
        if self.isElementExists('css', samplemsgnotice):  # 核酸提取明细表收到通知消息

            # 这里调用自定义截图方法
            Screenshot(self.driver).get_img("样本消息通知，核酸提取明细表点击查看收到的样本通知消息","收到的样本消息与发送的消息一致")

            msg = self.get_text('css', samplemsgnotice_notice_msg)
            print(msg)
            self.clicks('css', process_checkbox)
            self.sleep(0.5)
            self.clicks('css', samplemsgnotice_sumbit)
            self.wait_loading()
            return msg
        else:
            eermsg = "样本消息接收错误"
            return eermsg

    def sample_task_status(self):
        """
        样本消息通知任务列表，检查通知任务处理状态是否反写正确
        """
        taskID_nub = read_yaml(sampledata_path)
        lims_nub = taskID_nub["samplemsgnotice"]
        print("搜索lims号", lims_nub)
        log.info("搜索条件根据lims号，搜索出任务单，查看消息通知处理情况")
        self.input('css', check_by_sample_lims, lims_nub)
        self.sleep(0.5)
        self.clicks('css', search_btn)
        self.wait_loading()
        self.sleep(0.5)

        log.info("校验搜索出的通知单，处理状态")
        if self.isElementExists('css', sample_list):
            samplelist_status = self.get_text('css', sample_status)
            isRead = self.get_text('css', sample_isRead)
            print(samplelist_status, isRead)
            return samplelist_status, isRead
