# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# 流转表测试用例封装
import unittest
from common.enter_tab import EnterTab
from data.execute_sql_action import *
from pageobj.sample_workflowPage import SampleWorkflowPage
from common.logs import log
from common.Main import MyTest


class SampleWorskflow(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.swf = SampleWorkflowPage(self.driver)

    def user_enter_sampleworkflow(self):
        """
        进入流转表列表
        """
        self.swf.refresh()
        EnterTab.enter_workflow(self.basepage)
        EnterTab.enter_single_workflow(self.basepage)

    def user_enter_fj_mixedworkflow(self):
        """
        进入富集混合样本列表
        """
        self.swf.refresh()
        EnterTab.enter_workflow(self.basepage)
        EnterTab.enter_FJ_workflow(self.basepage)

    def user_enter_zc_mixedworkflow(self):
        """
        进入定量混合样本列表
        """
        self.swf.refresh()
        EnterTab.enter_workflow(self.basepage)
        EnterTab.enter_ZC_workflow(self.basepage)

    def test01_search_order(self):
        """
        测试在流转表搜索指定订单
        """
        self.initialize()
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索订单功能")
        self.swf.workflow_search_order()

    def test02_search_sample(self):
        """
        测试在流转表搜索指定LIMS样本号(以提取待选表样本为例)
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索指定LIMS样本号(以提取待选表样本为例)")
        self.swf.workflow_search_samplelimsid(lzb_get_sql1.format('extraction'))

    def test03_search_samplelab(self):
        """
        测试在流转表搜索指定实验室第一部分号
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索指定实验室第一部分号")
        self.swf.workflow_search_samplelab(lzb_get_sql1.format('extraction'))

    def test04_set_pathology(self):
        """
        测试在流转表搜索指定样本，设置病理任务
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索指定样本，设置病理任务")
        self.swf.workflow_set_pathology(lzb_get_sql2.format('extraction'))  # 只挑一些F,T类的样本，否则系统无法设置病理任务

    def test05_sample_fromdata(self):
        """
        测试在流转表搜索指定样本，分管操作，以在样本处理节点分管为例
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索指定样本，分管操作，以在样本处理节点分管为例")
        self.swf.workflow_fg(lzb_get_sql1.format('preparation'))

    def test06_sample_withdraw(self):
        """
        测试在流转表搜索指定数据，出库操作，以在样本接收节点为例
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表搜索指定数据，出库操作，以在样本接收节点为例")
        self.swf.workflow_ck(lzb_get_sql3)

    def test07_update_pooling_data(self):
        """
        测试在流转表对数据，做修改【建库+富集】信息的操作
        """
        self.user_enter_sampleworkflow()  # 进入单样本流转表页面
        log.info("测试流转表对数据，做修改【建库+富集】信息的操作")
        self.swf.workflow_update_wkgj_wkfj(lzb_get_sql4, '血液建库')

    def test08_search_pooling_workflow(self):
        """
        测试在富集混合样本搜索指定样本
        """
        self.user_enter_fj_mixedworkflow()  # 进入单样本流转表页面
        log.info("测试流转表-富集混合样本搜索指定样本")
        self.swf.mixed_workflow_wkfj(lzb_get_sql5)

    def test09_search_libquant_workflow(self):
        """
        测试在定量混合样本搜索指定样本
        """
        self.user_enter_zc_mixedworkflow()  # 进入单样本流转表页面
        log.info("测试流转表-定量混合样本搜索指定样本")
        self.swf.mixed_workflow_wkdl(lzb_get_sql6)


if __name__ == '__main__':
    unittest.main()
