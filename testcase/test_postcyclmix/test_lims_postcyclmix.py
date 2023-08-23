# -*- coding: utf-8 -*-
# @Time    : 2023/08/22
# @Author  : guanzhong.zhou
# @File    : 环化后混合模块测试用例
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
        log.info("环化后混合浓度调整前明细表自动计算")
        self.pc.detail_app_a_aliquot_sample()

    def test03_detail_generate_product(self):
        """测试环化后混合明细表生成产物"""
        log.info("测试明细表生成产物")
        self.pc.detail_generate_product()

    def test04_detail_batch_data(self):
        """测试环化后混合明细表批量数据"""
        log.info('环化后混合明细表选择批量数据')
        self.pc.detail_batch_data()

    def test05_detail_autoComplete(self):
        """测试环化后混合明细表自动计算"""
        log.info('环化后混合明细表自动计算')
        self.pc.detail_autoComplete()

    def test06_detail_save(self):
        """测试环化后混合明细表保存"""
        log.info('环化后混合明细表保存')
        self.pc.detail_save()

    def test07_detail_enter_result(self):
        """测试环化后混合明细表进入结果表"""
        log.info('环化后混合明细表进入结果表')
        self.pc.detail_enter_result()

    def test08_result_autoComplete(self):
        """测试环化后混合结果表自动计算"""
        log.info('环化后混合明细表进入结果表')
        self.pc.result_autoComplete()

    def test09_result_commit(self):
        """测试环化后混合结果表提交"""
        log.info('环化后混合结果表提交')
        self.pc.result_commit()
        log.info('环化后混合结果表数据写入下一步')
        self.pc.write_data_to_excel()

    def test10_detail_commit(self):
        """测试环化后混合明细表提交、入库"""
        log.info('环化后混合明细表提交、入库')
        self.pc.detail_commit()

    def test11_complete_task(self):
        """测试环化后混合结果表完成任务单"""
        log.info('环化后混合结果表完成任务单')
        self.pc.complete_task()

    def test12_serach_task(self):
        """测试环化后混合首页面查询已完成的样本任务单"""
        log.info('环化后混合首页面查询已完成的样本任务单')
        self.pc.serach_task()


if __name__ == '__main__':
    unittest.main()
