# -*- coding: utf-8 -*-
# @Time    : 2023/08/22
# @Author  : guanzhong.zhou
# @File    : 环化模块测试用例
import unittest
from pageobj.cyclizationPage import CycliPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Cyclization(MyTest):
    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.cy = CycliPage(self.driver)

    def test01_add_appa_task(self):
        """测试新建环化任务单"""
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_cyclization(self.basepage)  # 点击环化导航树

        log.info('登录系统，进入环化页面')
        # 传入驱动
        log.info('新建任务单')
        self.cy.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.cy.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_app_a_aliquot_sample(self):
        """测试环化样本分管操作"""
        log.info("环化浓度调整前明细表自动计算")
        self.cy.detail_app_a_aliquot_sample()

    def test03_detail_generate_product(self):
        """测试环化明细表生成产物"""
        log.info("测试明细表生成产物")
        self.cy.detail_generate_product()

    def test04_detail_batch_data(self):
        """测试环化明细表批量数据"""
        log.info('环化明细表选择批量数据')
        self.cy.detail_batch_data()

    def test05_detail_autoComplete(self):
        """测试环化明细表自动计算"""
        log.info('环化明细表自动计算')
        self.cy.detail_autoComplete()

    def test06_detail_save(self):
        """测试环化明细表保存"""
        log.info('环化明细表保存')
        self.cy.detail_save()

    def test07_detail_enter_result(self):
        """测试环化明细表进入结果表"""
        log.info('环化明细表进入结果表')
        self.cy.detail_enter_result()

    def test08_result_autoComplete(self):
        """测试环化结果表自动计算"""
        log.info('环化明细表进入结果表')
        self.cy.result_autoComplete()

    def test09_result_commit(self):
        """测试环化结果表提交"""
        log.info('环化结果表提交')
        self.cy.result_commit()
        log.info('环化结果表数据写入下一步')
        self.cy.write_data_to_excel()

    def test10_detail_commit(self):
        """测试环化明细表提交、入库"""
        log.info('环化明细表提交、入库')
        self.cy.detail_commit()

    def test11_complete_task(self):
        """测试环化结果表完成任务单"""
        log.info('环化结果表完成任务单')
        self.cy.complete_task()

    def test12_serach_task(self):
        """测试环化首页面查询已完成的样本任务单"""
        log.info('环化首页面查询已完成的样本任务单')
        self.cy.serach_task()


if __name__ == '__main__':
    unittest.main()
