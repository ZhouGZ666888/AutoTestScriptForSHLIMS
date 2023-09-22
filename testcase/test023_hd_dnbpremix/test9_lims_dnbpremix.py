# -*- coding: utf-8 -*-
# @Time    : 2023/08/22
# @Author  : guanzhong.zhou
# @File    : DNB制备模块测试用例
import unittest, re
from pageobj.dnbpremixPage import DnbpremixPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Postcyclmix(MyTest):
    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.db = DnbpremixPage(self.driver)

    def test01_add_appa_task(self):
        """测试新建DNB制备任务单"""
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_dnbpremix(self.basepage)  # 点击DNB制备导航树

        log.info('登录系统，进入DNB制备页面')
        # 传入驱动
        log.info('新建任务单')
        self.db.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.db.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_app_a_aliquot_sample(self):
        """测试DNB制备样本分管操作"""
        log.info("DNB制备浓度调整前明细表自动计算")
        info = self.db.detail_app_a_aliquot_sample()
        self.assertEqual(info, "样本分管成功", "样本分管失败！！")

    def test03_detail_generate_product(self):
        """测试DNB制备明细表生成中间产物"""
        log.info("测试明细表生成中间产物")
        info = self.db.detail_generate_product()

        self.assertEqual(info, "生成中间产物成功", "生成产物失败！！")

    def test04_detail_batch_data(self):
        """测试DNB制备明细表批量数据"""
        log.info('DNB制备明细表选择批量数据')
        info = self.db.detail_batch_data()
        self.assertEqual(info, "余样入库", "余样入库失败！！")

    def test05_detail_autoComplete(self):
        """测试DNB制备明细表自动计算"""
        log.info('DNB制备明细表自动计算')
        info = self.db.detail_autoComplete()

        self.assertEqual(info, "自动计算成功", "自动计算失败！！")

    def test06_detail_save(self):
        """测试DNB制备明细表保存"""
        log.info('DNB制备明细表保存')
        info = self.db.detail_save()
        self.assertEqual(info, "结果保存成功", "结果保存失败！！")

    def test07_detail_enter_middle(self):
        """测试DNB制备明细表进入中间表"""
        log.info('DNB制备明细表进入中间表')
        self.db.detail_enter_middle()
        self.assertIsNotNone(re.search(r'返回明细表', self.db.get_source))

    def test08_middle_dnbpremix_name(self):
        """测试DDNB制备中间表样本录入产物文库名称"""
        log.info('DNB制备中间表样本录入产物文库名称')
        self.db.middle_dnbpremix_name()

    def test09_middle_autoComplete(self):
        """测试DNB制备中间表自动计算"""
        log.info('DNB制备中间表自动计算')
        self.db.middle_autoComplete()

    def test10_middle_generate_product(self):
        """测试DNB制备中间表生成混合后DNB产物文库"""
        log.info('DNB制备中间表生成混合后DNB产物文库')
        info = self.db.middle_generate_product()
        self.assertEqual(info, "是", "生成产物失败！！")

    def test11_middle_enter_resutl(self):
        """测试DNB制备进入结果表"""
        log.info('DNB制备进入结果表')
        self.db.middle_enter_resutl()
        self.assertIsNotNone(re.search(r'返回中间产物表', self.db.get_source))

    def test12_result_commit(self):
        """测试DNB制备结果表提交"""
        log.info('DNB制备结果表提交')
        info = self.db.result_commit()
        log.info('DNB制备结果表数据写入下一步')
        self.db.write_data_to_excel()
        self.assertEqual(info, "是", "结果表提交失败！！")

    def test13_detail_commit(self):
        """测试DNB制备明细表提交、入库"""
        log.info('DNB制备明细表提交、入库')
        self.db.detail_commit()
        self.assertIsNotNone(re.search(r'完成', self.db.get_source))

    def test14_serach_task(self):
        """测试DNB制备首页面查询已完成的样本任务单"""
        EnterTab.enter_dnbpremix(self.basepage)  # 点击DNB制备导航树
        log.info('DNB制备首页面查询已完成的样本任务单')
        info = self.db.serach_task()
        self.assertNotEqual(info, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
