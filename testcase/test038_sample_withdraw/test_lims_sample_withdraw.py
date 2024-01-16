# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# 样本出库测试用例封装
import unittest
from common.enter_tab import EnterTab
from data.sql_action.execute_sql_action import *
from pageobj.ybckPage import GetSampleCK
from common.logs import log
from common.Main import MyTest


class SampleWithdraw(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.gsc = GetSampleCK(self.driver)

    def test01_search_withdraw(self):
        """
        测试在出库列表页搜索指定样本
        """
        self.initializes()
        EnterTab.enter_storage_center(self.basepage)
        EnterTab.enter_withdraw(self.basepage)
        log.info('登录系统，测试在出库列表页搜索指定样本')
        self.gsc.sample_ck_search(ybck_get_sql5)

    def test02_samplereceive_withdraw(self):
        """
        测试出库接样节点的样本
        """
        log.info('登录系统，对接样节点的样本进行出库')
        self.gsc.samplereceive_ck(ybck_get_sql2)

    def test03_samples_withdraw(self):
        """
        测试出库非接样，非混合节点的样本
        """
        log.info('登录系统，出库非接样，非混合节点的样本')
        self.gsc.unsamplereceive_ck(ybck_get_sql3)

    def test04_libquant_withdraw(self):
        """
        测试出库定量混合节点的样本
        """
        log.info('登录系统，出库定量混合节点的样本')
        self.gsc.libquantmixed_sample_ck(ybck_get_sql4)


if __name__ == '__main__':
    unittest.main()
