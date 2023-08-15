# -*- coding: utf-8 -*-
# @Time    : 2021/12/30
# @Author  : guanzhong.zhou
# @File    : 报告-基本编写任务分配模块页面方法封装

from datetime import datetime
from common.editYaml import *
from common.all_path import  orderNub_path
from common.screenshot import Screenshot
from PageElemens.report_bgbxrwfp_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class ReportWritingTaskAssignmentPage(BasePage):
    """
    报告-基本编写任务分配模块页面基础方法封装
    """

    def serach_data(self, ele, value):
        """
        :param ele: 元素定位
        :param value: 搜索条件
        """
        self.input('css', ele, value)  # 定位文本框输入值
        self.sleep(0.5)
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()

    def search_by_project(self):
        """
        按项目号搜索
        :return:返回查询出的订单信息数量
        """
        log.info("根据项目号搜索")
        self.click_by_js('css', project_num)  # 点击项目号搜索项
        self.sleep(0.5)
        self.clicks('xpath', project_num_chioce)  # 点击选中下拉条件
        self.sleep(0.5)
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', result_report_search):
            allorder = self.findelements('xpath', result_report_search)  # 获取查询结果数量
            self.clicks('css', reset_btn)  # 重置查询条件
            return len(allorder)
        else:
            return 0

    def search_by_date(self):
        """
        按预计实验日期查询
        :return: 返回查询出的订单信息数量
        """
        log.info("按预计实验日期查询")
        now_time = datetime.now()
        str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
        self.serach_data(poolingDate, str_time)  # 调用搜索方法
        if self.isElementExists('xpath', result_report_search):
            allorder = self.findelements('xpath', result_report_search)  # 获取查询结果数量
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
        ordre_numb = read_yaml(orderNub_path)
        self.serach_data(order_nub, ordre_numb['order_number'])  # 调用搜索方法
        if self.isElementExists('xpath', result_report_search):
            allorder = self.findelements('xpath', result_report_search)  # 获取查询结果数量
            return len(allorder)
        else:
            return 0

    def select_writer_bulk(self):
        """
        批量选择编写人
        :return: 返回页面提示信息
        """
        log.info("批量选择编写人")
        self.clicks('css', select_writer_bulk_btn)  # 批量选择编写人按钮
        self.wait_loading()
        self.clicks('css', all_choice)  # 全选按钮
        self.clicks('css', select_writer_bulk_choice)  # 编写人选择

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告编写任务分配,批量选择编写人")

        pageinfo = self.get_pageinfo()  # 获取页面提示信息
        self.wait_loading()
        return pageinfo

    def batch_selection_examiner(self):
        """
        批量选择初审人
        :return: 返回页面提示信息
        """
        log.info("批量选择初审人")
        self.clicks('css', batch_selection_examiner_btn)  # 批量选择审核人按钮
        self.wait_loading()
        self.clicks('css', all_choice)  # 全选按钮
        self.clicks('css', batch_selection_examiner_choice)  # 审核人选择
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告编写任务分配,批量选择初审人")
        pageinfo = self.get_pageinfo()  # 获取页面提示信息
        self.wait_loading()
        self.sleep(0.5)
        return pageinfo

    def get_pageinfo(self):
        """
        获取页面操作提示信息
        Task list saved successfully---保存样本到任务单成功
        Submit successfully---提交成功
        sample in storage successfully---入库成功
        """
        return self.get_text('xpath', page_success_info)
