# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : guanzhong.zhou
# @File    : 报告-基本信息处理模块测试用例封装

import unittest

from pageobj.report_jbxxclPage import ReportBasicInfoProcessingPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class ReportBasicInfoProcessing(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rbip = ReportBasicInfoProcessingPage(self.driver)

    def test01_info_serach_by_project(self):
        """
        测试基本信息处理模块，根据项目号搜索待处理任务
        """
        log.info('登录系统，进入报告基本信息处理页面')
        self.initializes()
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_basictask_deal(self.basepage)  # 点击基本信息任务分配
        # 传入驱动

        log.info('按项目号搜索')
        result1 = self.rbip.search_by_project()  # 订单号搜索

        self.assertNotEqual(result1, 0, "按项目号查询无结果！！！")

    def test02_info_serach_by_experimental_date(self):
        """
        测试基本信息处理模块，根据预计实验日期搜索待处理任务
        """
        log.info('按预计实验日期查询')
        result2 = self.rbip.search_by_date()
        self.assertNotEqual(result2, 0, "按预计实验日期查询无结果！！！")

    def test03_info_serach_by_order(self):
        """
        测试基本信息处理模块，根据订单号搜索待处理任务
        """
        log.info('按订单号搜索')
        result3 = self.rbip.search_by_order()
        self.assertNotEqual(result3, 0, "按订单号查询无结果！！！")

    def test04_edit_sample_info(self):
        """测试新增报告任务，录入产品信息、写入报告上机/不上机样本"""
        log.info('批量选择负责人、录入【写入报告的不上机样本】和【写入报告的上机样本】')
        self.rbip.edit_sample_info()
    def test05_(self):
        """测试选择生信阴性对照"""
        log.info('选择生信阴性对照')
        self.rbip.bioinformatic_negative()

    def test06_(self):
        """测试选择报告形式"""
        log.info('选择报告形式')
        self.rbip.choice_report_style()

    def test07_(self):
        """测试选择报告归属"""
        log.info('选择报告归属')
        self.rbip.choice_report_belongTo()

    def test08_(self):
        """测试选择报告模板"""
        log.info('选择报告模板')
        self.rbip.choice_report_TemplateName()

    def test09_view_and_update_medical(self):
        """测试点击查看样本信息和修改病历"""
        log.info('点击并查看样本信息')
        result1 = self.rbip.click_to_view()
        log.info('点击修改病历，打开并进入病历修改页面，获取页面title')
        result2 = self.rbip.update_medical()
        self.assertNotEqual(result1, 0, "点击查看获取样本信息错误")
        self.assertEqual(result2, '电子病历详情', "进入病历修改页面成功")


if __name__ == '__main__':
    unittest.main()
