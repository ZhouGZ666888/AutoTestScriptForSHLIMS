# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong


import unittest, time
from pageobj.sopPage import *
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class SopBasedata(MyTest):
    def setUp(self) -> None:
        self.sop = SopPage(self.driver)

    def user_enter_order(self):
        """
        调用进入模块功能
        """
        # 调用登录(单独调试case用，批量跑用例则需要注释)
        self.initialize()
        EnterTab.enter_sop_center(self.basepage)  # 点击sop的tab按钮

    def test01_sop_list_search(self):
        """
        测试sop主数据列表页搜索功能
        """
        log.info('登录系统，进入sop面')
        self.user_enter_order()  # 调用进入模块功能
        self.sop.search_task()

    def test02_add_sop_data(self):
        """
        测试新建sop主数据功能
        """
        moudles_list = ['病理', '病理', '样本处理', '核酸提取', '超声破碎', '文库构建', '文库定量', '上机']
        type_list = ['HE', 'PD-L1(28-8)', '血液体液分离', 'DNA提取（组织）', 'DNA破碎', 'cfDNA 1.0', '单梯度定量', 'illumina上机']


        for i in range(len(moudles_list)):
            now = time.strftime("%Y-%m-%d-%H:%M:%S")
            log.info("当前新建的sop模块为：" + str(moudles_list[i]))
            log.info("当前新建的sop类型为：" + str(type_list[i]))
            self.sop.creat_sop(moudles_list[i] + '_' + str(now), moudles_list[i], type_list[i])


if __name__ == '__main__':
    unittest.main()
