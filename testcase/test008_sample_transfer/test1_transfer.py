# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong


import unittest
from common.enter_tab import EnterTab
from pageobj.kwglPage import *
from pageobj.ybhykPage import SampleYbyk
from common.logs import log
from common.Main import MyTest


class SampleTransfer(MyTest):

    def setUp(self) -> None:
        self.kwgl = SampleKwgl(self.driver)
        self.ybyk = SampleYbyk(self.driver)

    def user_enter_order(self):
        """
        调用进入模块功能
        """
        self.kwgl.kwgl_change_role('2535', '2001', '0')  # 使用数据库，将用户修改为非库管角色
        # 调用登录(单独调试case用，批量跑用例则需要注释)
        self.initialize()
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_transfer(self.basepage)  # 点击样本/盒移位的tab按钮

    def test01_box_add_transfer(self):
        """
        测试新增样本盒移库的功能，新建任务单到完成任务单
        """

        self.user_enter_order()  # 调用进入模块功能

        self.ybyk.ybhyk_change_role('2535', '2001', '0')  # 将董国奇用户置为临时库权限
        self.ybyk.ybhyk_add_temporary_storage()  # 点击新增移样本盒任务单
        self.ybyk.ybhyk_add_temporary_storage_detail()  # 新增移样本盒任务单后，进入详情页添加信息
        self.ybyk.wait_loading()  # 自动进入详情页，等待loading结束

    def test02_box_list_search_transfer(self):
        """
        测试库位管理列表页搜索样本盒在当前哪个任务单中功能
        """
        EnterTab.enter_transfer(self.basepage)
        self.ybyk.ybhyk_list_search()

    def test03_sample_add_transfer(self):
        """
        测试新增样本移库的功能，新建任务单到完成任务单
        """

        self.ybyk.ybhyk_change_role('2535', '2001', '0')  # 将董国奇用户置为临时库权限
        self.ybyk.ybyk_add_temporary_storage()  # 点击新增移样本盒任务单
        self.ybyk.ybyk_add_temporary_storage_detail()  # 新增移样本盒任务单后，进入详情页添加信息
        self.ybyk.wait_loading()  # 自动进入详情页，等待loading结束

    def test04_sample_list_search_transfer(self):
        """
        测试库位管理列表页搜索样本在当前哪个任务单中功能
        """
        EnterTab.enter_transfer(self.basepage)  # 点击样本/盒移位的tab按钮
        self.ybyk.ybyk_list_search()


if __name__ == '__main__':
    unittest.main()
