# -*- coding: utf-8 -*-
# @Time    : 2022/01/24
# @Author  : guanzhong.zhou
# @File    : MGMT模块测试用例封装
import unittest
from PageElemens.mgmt_ele import *
from pageobj.mgmtPage import MGMTPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Mgmt(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.mt = MGMTPage(self.driver)

    def test01_add_mgmt_task(self):
        """
        测试新建MGMT任务单，在待选表录入SOP，添加样本、保存任务单
        """
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_mgmt(self.basepage)  # 点击MGMT导航树

        log.info('登录系统，进入MGMT页面~~~')
        log.info('新建任务单，选择sop')
        self.mt.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.mt.check_lims_num()
        log.info('保存任务单，进入明细表')
        self.mt.enter_result_list(enter_detail_list_btn, 'MGMT明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_twentyonegene_edit(self):
        """
        测试MGMT明细表录入批量入库类型、自动计算、提交入库操作
        """

        log.info('录入批量入库类型、自动计算')
        self.mt.detail_mgmt_edit()
        log.info('明细表提交操作')
        self.mt.detail_sumbit()
        log.info('明细表入库操作')
        pageinfo = self.mt.detail_into_storage()
        log.info('保存任务单，进入明细表')
        self.mt.enter_result_list(enter_result_list_btn, 'MGMT结果表')
        self.assertEqual(pageinfo, '完成', '入库失败！')

    def test03_result_twentyonegene_edit(self):
        """
        MGMT结果表，表单数据录入、结果分析、提交、完成任务单测试
        """
        log.info("MGMT结果表批量质检结果、批量结果判读")
        self.mt.result_edit()
        log.info(" 结果表表单转化后浓度、进入总量、总油滴数、FAM信号油滴数、HEX信号油滴数录入，进行自动计算")
        self.mt.result_data()
        log.info("MGMT结果表提交操作")
        samplestatue = self.mt.result_sumbit()
        log.info("MGMT完成任务单")
        taskstatue = self.mt.complete_task()
        self.assertEqual(samplestatue, '是', '提交失败')
        self.assertEqual(taskstatue, '完成', '任务单完成失败！')

    def test04_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_mgmt(self.basepage)  # 点击MGMT导航树

        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.mt.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
