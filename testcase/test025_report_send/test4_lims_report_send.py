# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : guanzhong.zhou
# @File    : 报告发送模块测试用例封装
import unittest
from pageobj.report_sendPage import ReportSendPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class ReportSend(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rs = ReportSendPage(self.driver)

    def test01_serach_info_by_complete_date(self):
        """
        测试发送模块，根据预计实验日期搜索待发送任务
        """
        self.initialize()
        log.info('登录系统，进入报告发送页面')
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_send(self.basepage)  # 点击基本信息任务分配

        log.info('根据报告完成日期查询')
        result = self.rs.search_by_date()
        self.assertNotEqual(result, 0, "查询无结果！！！")

    def test02_serach_info_by_order(self):
        """
        测试发送模块，根据订单号搜索待发送任务
        """
        log.info('按订单号搜索')
        result2 = self.rs.search_by_order()
        self.assertNotEqual(result2, 0, "查询无结果！！！")

    def test03_update_report(self):
        """
        测试修改报告审核状态,并保存报告信息
        """
        log.info('修改报告审核状态')
        self.rs.edit_report_status()
        log.info('保存修改')
        pageinfo = self.rs.save()
        self.assertEqual(pageinfo, '保存成功', "保存失败！！！")


if __name__ == '__main__':
    unittest.main()
