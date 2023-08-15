# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : guanzhong.zhou
# @File    : 报告发送模块页面方法封装

from datetime import datetime
from PageElemens.report_send_ele import *
from common.editYaml import *
from common.all_path import  orderNub_path
from common.logs import log
from common.screenshot import Screenshot
from uitestframework.basepageTools import BasePage


class ReportSendPage(BasePage):
    """
    报告-基本信息任务分配模块页面基础方法封装
    """

    def serach_data(self, ele, value):
        """
        :param ele: 元素定位
        :param value: 搜索条件
        """

        self.input('xpath', ele, value)  # 定位文本框输入值
        self.sleep(0.5)
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()

    def search_by_date(self):
        """
        根据预计实验日期查询
        :return: 返回查询结果数量
        """
        log.info("根据预计实验日期查询")
        # 获取当前时间
        str_time = datetime.now().strftime('%Y.%m.%d')
        self.input('css', reportSend_form_completeDate, str_time)
        self.sleep(0.5)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', search_result):
            allorder = self.findelements('xpath', search_result)  # 获取查询结果数量
            self.clicks('css', reset_btn)  # 重置查询条件
            return len(allorder)
        else:
            return 0

    def search_by_order(self):
        """
        按订单号搜索
        :return:返回查询出的订单信息数量
        """
        log.info("按订单号搜索")
        order = read_yaml(orderNub_path)  # 订单Excel获取订单号
        self.input('css', order_num, order['order_number'])
        self.sleep(0.5)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', search_result):
            allorder = self.findelements('xpath', search_result)  # 获取查询结果数量
            return len(allorder)
        else:
            return 0

    def edit_report_status(self):
        """
        修改报告审核状态
        """
        log.info("修改报告审核状态")
        self.clicks('xpath', audit_status)  # 点击表单审核状态表单
        self.clicks('xpath', audit_status_select)  # 点击表单审核状态下拉
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告发送，修改报告审核状态")
        self.clicks('xpath', audit_status_choice)  # 表单审核状态选择---已审核

    def save(self):
        """
        保存信息
        :return:返回页面提示信息
        """
        log.info("保存信息")
        self.clicks('css', save_btn)
        pageinfo = self.get_save_info()
        print(pageinfo)
        return pageinfo

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        return self.get_text('xpath', page_info)
