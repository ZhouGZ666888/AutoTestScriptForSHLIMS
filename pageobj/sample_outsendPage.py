# -*- coding: utf-8 -*-
# @Time    : 2022/04/10
# @Author  : guanzhong.zhou
# @File    : 样本外送模块页面功能封装
import yaml
from PageElemens.sample_outsend_ele import *
from common.all_path import csps_file_path, functionpageURL_path, sampledata_path
from common.editYaml import read_yaml
from common.screenshot import Screenshot
from common.xlsx_excel import read_excel_col
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleOutSendPage(BasePage):
    """
    样本外送页面方法封装
    """

    # 新建样本外送任务
    def add_sample_outsend_task(self):
        """
        新建样本外送任务
        """
        # 这里调用自定义截图方法


        log.info('点击新建按钮新建样本外送任务，进入样本外详情页面')
        self.clicks('css', add_task)
        self.wait_loading()
        self.sleep(0.5)
        Screenshot(self.driver).get_img("点击新建按钮新建样本外送任务，进入样本外详情页面","进入外送详情页成功")
        log.info('外送申请单详情页，选择外送类型：样本回寄')
        self.click_by_js('css', outsend_type)
        self.sleep(0.5)
        self.clicks('xpath', outsend_type_choice.format('样本回寄'))
        self.sleep(0.5)
        log.info('外送申请单详情页，选择接收方，患者家属')
        self.click_by_js('css', recipient)
        self.sleep(0.5)
        self.clicks('xpath', recipient_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，录入外送目的地地址')
        self.input('css', sendAddress, '测试地址')
        self.sleep(0.5)
        log.info('外送申请单详情页选择寄送方式，快递')
        self.click_by_js('css', sendMethod)
        self.sleep(0.5)
        self.clicks('xpath', sendMethod_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，录入跟踪信息')
        self.input('css', trackingInfo, '测试追踪消息')
        self.sleep(0.5)
        log.info('外送申请单详情页，选择关联项目J022')
        self.clicks('css', projectId)
        self.sleep(0.5)
        self.clicks('xpath', projectId_choice)
        self.sleep(0.5)
        log.info('外送申请单详情页，选择审核人')
        self.clicks('css', lastAuditedBy_btn)
        self.sleep(0.5)
        self.input('css', lastAuditedBy, '周官钟')
        self.sleep(1)
        self.click_by_js('xpath', lastAuditedBy_choice)
        self.sleep(0.5)

        log.info('保存样本外送任申请单')
        self.clicks('css', save_btn)
        self.wait_loading()
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("样本外送明细详情页选择样本回寄方式，录入外送申请单详细信息后保存","保存外送申请单成功")

    # 待选样本表选择样本至明细表
    def add_sample_to_task(self):
        """
        样本外送审核操作
        """
        log.info('从实验模块-取核酸提取结果表样本数据当做外送样本')
        lims_nub = read_excel_col(csps_file_path, 'lims号')
        lims_id_str = "\n".join(lims_nub[:2])  # 取出Excel表中样本，拼接成字符串录入到检索文本中,取后面两条
        print(lims_id_str)

        log.info("点击样本筛选按钮，录入样本lims号，筛选出外送样本")
        self.clicks('css', samplefilter)
        self.sleep(0.5)

        log.info("进入样本筛选弹框,录入lism号")
        self.clicks('css', sampleIdLims_input)
        self.sleep(0.5)
        self.input('css', lims_input, lims_id_str)
        self.sleep(0.5)
        self.click_by_js('css', lims_input_comfirm)

        log.info("录入筛选条件后，点击确认，进行搜索")
        self.clicks('css', detail_search_comfirm)
        self.wait_loading()

        log.info("选择筛选结果，添加至明细表")
        self.clicks('css', detail_all_choice)
        self.sleep(0.5)
        self.clicks('css', add_detail)
        self.wait_loading()

        log.info("进入明细表")
        self.clicks('css', to_detail)
        self.wait_loading()

    # 样本外送明细表处理、提交审核
    def outsend_detail_edit(self):
        """
        样本外送明细表处理、提交审核
        """
        urldata = read_yaml(functionpageURL_path)

        log.info("样本外送明细表全选样本")
        self.clicks('css', outsend_detail_all_choice)
        self.sleep(0.5)

        log.info('外送样本明细表是否全样外送选择：全部外送')
        self.moved_to_element('css', is_allOutsend)
        self.sleep(0.5)
        self.click_by_js('xpath', is_allOutsend_choice)
        self.sleep(0.5)

        log.info('提交审核')
        self.clicks('css', submit_btn)
        self.wait_loading()

        url = self.get_current_url()  # 获取当前页面URL地址
        print('获取的URL地址', url)
        urldata["url"] = url
        with open(functionpageURL_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的URL地址", urldata)

        Screenshot(self.driver).get_img("样本外送明细表添加外送样本，点击添加按钮，选中样本，点击添加到明细表","添加到明细表成功")
        task_status = self.get_text('css', detail_task_status)
        return task_status[3:].strip()

    # 部门审核人角色(样本外送)审核任务单
    def task_for_review(self):
        """
        部门审核人角色审核任务单
        """
        self.into_pending_task()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击待办模块进入样本外送审核页面", "审核页面进入成功")


        log.info('点击完成审核')
        self.clicks('css', finishAudit_btn)
        self.wait_loading()
        self.sleep(0.5)

        Screenshot(self.driver).get_img("部门审核人角色审核任务单，样本外送明细审核页面，点击审核按钮", "审核人审核成功，状态改为取样中")
        log.info('获取审核后的申请单号和状态')
        application_num = self.get_text('css', detail_task_id)
        application_status = self.get_text('css', detail_task_status)  # 取样中
        print(application_status)
        print(application_num)

        log.info('将获取的申请单号写入临时文件')
        application_num = application_num[5:].strip()
        urldata = read_yaml(sampledata_path)
        urldata["sample_outsend_task_id"] = application_num
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的临时文件内容：", urldata)

        return application_status[3:].strip()

    def into_pending_task(self):
        # 进入代办页面
        log.info("通过待办任务页面，进入样本外送审核tab页")
        if self.isElementExists('css', outsendsample_tab):
            self.clicks('css', outsendsample_tab)
        self.sleep(0.5)
        log.info("进入样本外送待办tab页,点击进入按钮")
        self.clicks('css', outsend_review_btn)
        self.wait_loading()
        log.info("待办页面进入样本外送页面，弹出新页面，切换至新页面，并关闭旧页面")
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(0.5)

    # 审核完成后，进行取样确认操作
    def sample_sampling(self):
        """
        在审核完成后，有权限用户进行取样确认操作
        """
        self.into_pending_task()

        log.info('进入审核后的样本外送详情页，点击取样确认按钮')
        self.clicks('css', check_btn)
        self.wait_loading()
        Screenshot(self.driver).get_img("部门审核人角色审核任务单，样本外送明细审核页面，点击审核按钮", "审核人审核成功，状态改为待寄送")

        log.info('获取取样寄送后的申请单状态')
        application_status = self.get_text('css', detail_task_status)  # 待寄送
        print(application_status)
        return application_status[3:].strip()

    def sample_send(self):
        """
        在取样完成后，有权限用户进行待寄送确认操作
        """
        # self.into_pending_task()
        log.info('完成寄送操作')
        self.clicks('css', sendfinish_btn)
        self.wait_loading()
        Screenshot(self.driver).get_img("有权限用户进行待寄送确认操作，点击待寄送按钮","完成寄送，任务状态改为完成")

        log.info('获取完成寄送后的申请单状态')
        application_status = self.get_text('css', detail_task_status)  # 完成
        return application_status[3:].strip()

    # 样本外送申请列表检索
    def search_task(self):
        """
         样本外送申请列表检索申请单
        """
        log.info('根据申请单号检索')
        self.clicks('css', search_btn)
        self.sleep(0.5)

        urldata = read_yaml(sampledata_path)
        application_num = urldata["sample_outsend_task_id"]

        self.input('css', search_lims_task_id, application_num)
        self.clicks('css', search_confirm)
        self.wait_loading()
        self.sleep(1)

        eles = self.findelements('xpath', sample_page_list)
        return eles

    def batch_submit_for_review(self):
        """
        切换登录用户进行审核
        """
        log.info('点击页面退出登录按钮，切换登录用户')
        self.click_by_js('css', logout_btn)
        self.sleep(1)
        self.click_by_js('xpath', logout_choice)
        self.sleep(1)
