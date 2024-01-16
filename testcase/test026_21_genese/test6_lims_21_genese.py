# -*- coding: utf-8 -*-
# @Time    : 2021/12/16
# @Author  : guanzhong.zhou
# @File    : 21基因模块测试用例封装
import re
import unittest
from pageobj.genes21Page import Genes21Page
from PageElemens.genes_21_ele import *
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Genes21(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.ge = Genes21Page(self.driver)

    def test01_add_sequencing_task(self):
        """
        测试新建21基因任务单，在待选表录入SOP，添加样本、保存任务单
        """
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_21gene(self.basepage)  # 点击21基因导航树

        log.info('登录系统，进入21基因页面')
        # 传入驱动
        log.info('新建任务单，选择sop')
        self.ge.add_task()  # 新建任务单，选择sop
        log.info('核对样本lims号并选中加入任务单')
        info = self.ge.check_lims_num()
        log.info('保存任务单，进入明细表')
        self.ge.enter_result_list(enter_detail_list_btn, '21基因明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_twentyonegene_batchdate(self):
        """21基因明细表选择批量入库类型、录入批量包装余量"""
        info = self.ge.detail_twentyonegene_batchdate()
        self.assertEqual(info, "结果保存成功", '保存失败')

    def test03_detail_twentyonegene_date(self):
        """测试21基因明细表数据录入"""
        log.info('录入表单数据')
        self.ge.detail_twentyonegene_date()

    def test04_detail_twentyonegene_merge(self):
        """测试21基因明细表合并分析操作"""
        info = self.ge.detail_twentyonegene_merge()
        self.assertEqual(info, "合并成功", '合并失败')

    def test05_enter_result_list(self):
        """测试进入结果表"""
        log.info('保存任务单，进入结果表')
        self.ge.enter_result_list(enter_result_list_btn, '21基因结果表')

    def test06_result_twentyonegene_edit(self):
        """测试21基因结果表，表单数据录入、结果分析、提交、完成任务单测试"""
        log.info(" 21基因结果表，进入体积、进入总量")
        self.ge.result_twentyonegene_date()
        log.info(" 21基因结果表提交")
        self.ge.sumbit_task()
        log.info("21基因结果分析")
        self.ge.result_twentyonegene_analysis()
        log.info("21基因分析结果表,保存并完成")
        self.ge.result_twentyonegene_analysis_complete()

    def test07_goback_detail(self):
        """测试返回明细表"""
        self.ge.goback_detail()
        result = re.search(r'21基因实验明细表', self.ge.get_source)
        self.assertIsNotNone(result)

    def test08_detail_sumbit(self):
        """测试明细表提交操作"""
        info = self.ge.detail_sumbit()
        self.assertEqual(info, '提交成功', '提交成功失败！')

    def test09_detail_into_storage(self):
        """测试明细表入库"""
        info = self.ge.detail_into_storage()
        self.assertEqual(info, '完成', '入库失败！')

    def test10_complete_task(self):
        """测试完成任务单"""
        self.ge.enter_result_list(enter_result_list_btn, '21基因结果表')
        log.info("21基因分析结果表,完成任务单")
        pageinfo = self.ge.complete_task()
        self.assertEqual(pageinfo, '完成', '任务单完成失败！')

    def test11_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_21gene(self.basepage)  # 点击21基因导航树

        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.ge.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
