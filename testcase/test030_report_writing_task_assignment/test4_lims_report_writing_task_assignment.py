# -*- coding: utf-8 -*-
# @Time    : 2021/12/30
# @Author  : guanzhong.zhou
# @File    : 报告-基本编写任务分配测试用例封装
import unittest
from pageobj.report_bgbxrwfpPage import ReportWritingTaskAssignmentPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class ReportWritingTaskAssignment(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rwta = ReportWritingTaskAssignmentPage(self.driver)

    def test01_serach_info_by_project(self):
        """
        测试报告编写任务分配模块，根据项目号搜索待处理任务
        """
        log.info('登录系统，进入报告编写任务分配页面')
        self.initialize()
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_edittask_distribution(self.basepage)  # 点击基本信息任务分配

        log.info('按项目号搜索')
        result = self.rwta.search_by_project()
        self.assertNotEqual(result, 0, "按项目号查询无结果！！！")

    def test02_serach_info_by_experimental_date(self):
        """
        测试基本信息处理模块，根据预计实验日期搜索待处理任务
        """
        log.info('按预计实验日期查询')
        result = self.rwta.search_by_date()
        self.assertNotEqual(result, 0, "按预计实验日期查询无结果！！！")

    def test03_serach_info_by_order(self):
        """
        测试基本信息处理模块，根据订单号搜索待处理任务
        """
        log.info('按订单号搜索')
        result = self.rwta.search_by_order()
        self.assertNotEqual(result, 0, "按订单号查询无结果！！！")

    def test04_edit_sample_choice_writer(self):
        """
        测试对筛选出的报告任务批量选择编写人
        """
        log.info('选择编写人')
        pageinfo = self.rwta.select_writer_bulk()
        self.assertEqual(pageinfo, '选择编写人成功', "选择编写人功能失败！！！")

    def test05_edit_sample_choice_examiner(self):
        """
        测试对筛选出的报告任务批量选择审核人
        """
        log.info('选择审核人')
        pageinfo = self.rwta.batch_selection_examiner()
        self.assertEqual(pageinfo, '选择初审人成功', "选择编写人功能失败！！！")


if __name__ == '__main__':
    unittest.main()
