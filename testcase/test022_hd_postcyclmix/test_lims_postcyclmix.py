# -*- coding: utf-8 -*-
# @Time    : 2023/08/22
# @Author  : guanzhong.zhou
# @File    : 环化后混合模块测试用例
import re
import unittest
from pageobj.postcyclmixPage import PostcyclmixPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Postcyclmix(MyTest):
    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.pc = PostcyclmixPage(self.driver)

    def test01_add_appa_task(self):
        """测试新建环化后混合任务单"""
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_postcyclmix(self.basepage)  # 点击环化后混合导航树

        log.info('登录系统，进入环化后混合页面')
        # 传入驱动
        log.info('新建任务单')
        self.pc.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.pc.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_app_a_aliquot_sample(self):
        """测试环化后混合样本分管操作"""
        log.info("环化后混合样本分管操作")
        info = self.pc.detail_app_a_aliquot_sample()
        self.assertEqual(info, "样本分管成功", "样本分管失败！！")

    def test03_detail_generate_product(self):
        """测试环化后混合明细表生成产物"""
        log.info("测试明细表生成产物")
        info = self.pc.detail_generate_product()
        self.assertEqual(info, "成功生成混合产物", "生成产物失败！！")

    def test04_detail_batch_data(self):
        """测试环化后混合明细表批量数据"""
        log.info('环化后混合明细表选择批量数据')
        info = self.pc.detail_batch_data()
        self.assertEqual(info, "余样入库", "余样入库失败！！")

    def test05_detail_autoComplete(self):
        """测试环化后混合明细表自动计算"""
        log.info('环化后混合明细表自动计算')
        info = self.pc.detail_autoComplete()
        self.assertEqual(info, "自动计算成功", "自动计算失败！！")

    def test06_detail_save(self):
        """测试环化后混合明细表保存"""
        log.info('环化后混合明细表保存')
        info = self.pc.detail_save()
        self.assertEqual(info, "结果保存成功", "结果保存失败！！")

    def test07_detail_enter_result(self):
        """测试环化后混合明细表进入结果表"""
        log.info('环化后混合明细表进入结果表')
        self.pc.detail_enter_result()
        self.assertIsNotNone(re.search(r'返回明细表', self.pc.get_source))

    def test08_result_autoComplete(self):
        """测试环化后混合结果表自动计算"""
        log.info('环化后混合明细表进入结果表')
        self.pc.result_autoComplete()

    def test09_result_commit(self):
        """测试环化后混合结果表提交"""
        log.info('环化后混合结果表提交')
        info = self.pc.result_commit()
        log.info('环化后混合结果表数据写入下一步')
        self.pc.write_data_to_excel()
        self.assertEqual(info, "是", "结果表提交失败！！")

    def test10_detail_commit(self):
        """测试环化后混合明细表提交、入库"""
        log.info('环化后混合明细表提交、入库')
        self.pc.detail_commit()
        self.assertIsNotNone(re.search(r'完成', self.pc.get_source))

    def test11_complete_task(self):
        """测试环化后混合结果表完成任务单"""
        log.info('环化后混合结果表完成任务单')
        info = self.pc.complete_task()
        self.assertEqual(info, "完成", "完成任务单成功！！")

    def test12_serach_task(self):
        """测试环化后混合首页面查询已完成的样本任务单"""
        EnterTab.enter_postcyclmix(self.basepage)  # 点击环化后混合导航树
        log.info('环化后混合首页面查询已完成的样本任务单')
        info = self.pc.serach_task()
        self.assertNotEqual(info, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
