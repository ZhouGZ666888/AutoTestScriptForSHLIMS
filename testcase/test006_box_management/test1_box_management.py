# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong

import unittest, time
from pageobj.hwglPage import *
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class SampleBoxManagement(MyTest):

    def setUp(self) -> None:
        self.hwgl = SampleHwgl(self.driver)

    def test01_box_list_search(self):
        """
        测试样本盒管理列表页搜索功能
        """
        self.initializes()
        EnterTab.enter_storage_center(self.basepage)  # 点击样本库位管理的tab按钮
        EnterTab.enter_box_user(self.basepage)  # 点击盒位管理的tab按钮
        self.hwgl.hwgl_list_search()

    def test02_box_list_delete(self):
        """
        测试样本盒管理列表页删除功能
        """

        self.hwgl.hwgl_list_delete()

    def test03_box_list_add(self):
        """
        测试样本盒管理列表页新增盒子功能
        """
        now = time.strftime("%Y-%m-%d-%H:%M:%S")
        print(now)
        box_name = '盒子_' + str(now)

        result = self.hwgl.hwgl_list_add(1, box_name)  # 每次新建一个盒子
        assert box_name in result[0]['box_name']


if __name__ == '__main__':
    unittest.main()
