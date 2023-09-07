# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : guanzhong.zhou
# @File    : 报告上传模块测试用例封装
import unittest
from pageobj.report_uploadPage import ReportUploadPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class ReportUpload(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.rup = ReportUploadPage(self.driver)

    def test01_serach_by_poolingdate(self):
        """
        测试报告上传模块，根据预计实验日期搜索待处理任务
        """
        log.info('登录系统，进入报告发送页面')
        self.initialize()
        EnterTab.enter_report_center(self.basepage)  # 点击报告任务列表
        EnterTab.enter_report_upload(self.basepage)  # 点击基本信息任务分配
        log.info('根据预计实验日期查询')
        result = self.rup.search_by_poolingdate()
        self.assertNotEqual(result, 0, "根据预计实验日期查询无结果！！！")

    def test02_serach_by_assignmentDate(self):
        """
        测试报告上传模块，根据最新富集日期查询待处理任务
        """
        log.info('根据最新富集日期查询')
        result2 = self.rup.search_by_assignmentDate()
        self.assertNotEqual(result2, 0, "根据最新富集日期查询无结果！！！")

    def test03_serach_by_order(self):
        """
        测试报告上传模块，根据订单号搜索待处理任务
        """
        log.info('按订单号搜索')
        result3 = self.rup.search_by_order()
        self.assertNotEqual(result3, 0, "按订单号查询无结果！！！")

    def test04_update_report_info(self):
        """
        测试选择报告归属、选择复审人功能
        """
        log.info('选择报告归属')
        self.rup.select_report_belong()
        log.info('选择复审人')
        pageinfo1 = self.rup.choice_rehearing_person()
        self.assertEqual(pageinfo1, '选择复审人成功', "选择复审人功能失败！！！")

    def test05_upload_file_for_report(self):
        """测试上传报告文件"""
        log.info('上传报告文件')
        report_info = self.rup.upload_report_file()
        self.assertEqual(report_info, '上传成功', "上传报告文件失败！！！")

    def test06_upload_file_for_read(self):
        """测试上传解读文件"""
        decode_info = self.rup.upload_read_file()
        self.assertEqual(decode_info, '上传成功', "上传解读文件失败！！！")

    def test07_upload_file_for_other(self):
        """测试上传其他文件"""
        self.rup.upload_other_file()

    def test08_upload_file_for_mutation(self):
        """测试上传突变文件"""
        log.info('突变文件上传')
        mutation_file_info = self.rup.update_mutation_file()
        self.assertEqual(mutation_file_info, '上传成功', "上传突变文件失败！！！")

    def test09_complete_task(self):
        """完成任务"""
        log.info('完成任务')
        complete_info = self.rup.complete_report_task()
        self.assertEqual(complete_info, '修改', "报告任务完成失败！！！")


if __name__ == '__main__':
    unittest.main()
