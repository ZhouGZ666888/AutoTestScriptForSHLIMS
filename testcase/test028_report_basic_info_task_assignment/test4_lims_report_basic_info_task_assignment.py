# -*- coding: utf-8 -*-
# @Time    : 2021/12/28
# @Author  : guanzhong.zhou
# @File    : 报告-基本信息任务分配模块测试用例封装
import unittest
from pageobj.report_jbxxrwfpPage import ReportBasicInfoTaskAssignmentPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class ReportBasicInfoTaskAssignment(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.bita = ReportBasicInfoTaskAssignmentPage(self.driver)

    def test01_add_sequencing_task(self):
        """
        测试基本信息任务分配模块，根据订单号搜索待分配任务，进行负责人分配
        """
        self.initializes()
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_basictask_distribution(self.basepage)  # 点击基本信息任务分配

        log.info('登录系统，进入报告基本信息处理页面~~~~')
        log.info('搜索测试流转中的订单号')
        self.bita.serach_order()  # 订单号搜索
        log.info('为任务分配负责人')
        self.bita.click_search_btn()
        info = self.bita.batch_choice_charge_person()

        self.assertEqual(info, "选择负责人成功", "选择负责出现错误！！！")


if __name__ == '__main__':
    unittest.main()
