# -*- coding: utf-8 -*-
# @Time    : 2023/08/18
# @Author  : guanzhong.zhou
# @File    : APP-A模块测试用例
import unittest
from pageobj.APP_APage import APPAPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class AppA(MyTest):
    def setUp(self) -> None:
        """初始化浏览器驱动"""
        self.ap = APPAPage(self.driver)

    def test01_add_appa_task(self):
        """测试新建APP-A任务单"""
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_APPA(self.basepage)  # 点击APP-A导航树

        log.info('登录系统，进入APP-A页面')
        # 传入驱动
        log.info('新建任务单')
        self.ap.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.ap.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_app_a_aliquot_sample(self):
        """测试APP-A样本分管操作"""
        log.info("APP-A浓度调整前明细表自动计算")
        self.ap.detail_app_a_aliquot_sample()

    def test03_detail_generate_product(self):
        """测试APP-A明细表生成产物"""
        log.info("测试明细表生成产物")
        self.ap.detail_generate_product()

    def test04_detail_batch_storage_type(self):
        """测试APP-A明细表选择批量入库类型"""
        log.info('APP-A明细表选择批量入库类型')
        self.ap.detail_batch_storage_type()

    def test05_detail_remaining_pkg_amt(self):
        """测试APP-A明细表批量包装余量"""
        log.info('APP-A明细表批量包装余量')
        self.ap.detail_remaining_pkg_amt()

    def test06_detail_batch_paste_import_package_btn(self):
        """测试APP-A明细表批量粘贴导入"""
        log.info('APP-A明细表批量粘贴导入')
        self.ap.detail_batch_paste_import_package_btn()

    def test07_detail_autoComplete(self):
        """测试APP-A明细表明细表自动计算、保存"""
        log.info('APP-A明细表明细表自动计算')
        self.ap.detail_autoComplete()
        self.ap.detail_save()

    def test08_detail_enter_result(self):
        """测试APP-A明细表进入结果表"""
        log.info('APP-A明细表进入结果表')
        self.ap.detail_enter_result()

    def test09_result_generate_appname(self):
        """测试结果表生成APP-A产物名称"""
        log.info('结果表生成APP-A产物名称')
        self.ap.result_generate_appname()

    def test10_result_batch_paste_import_package(self):
        """测试APP-A结果表批量粘贴导入"""
        log.info('APP-A结果表批量粘贴导入')
        self.ap.result_batch_paste_import_package()

    def test11_result_autoComplete(self):
        """测试APP-A结果表自动计算"""
        log.info('APP-A结果表自动计算')
        self.ap.result_autoComplete()

    def test12_result_commit(self):
        """测试APP-A结果表提交"""
        log.info('APP-A结果表提交')
        self.ap.result_commit()
        log.info('APP-A结果表数据写入下一步')
        self.ap.write_data_to_excel()

    def test13_detail_commit(self):
        """测试APP-A明细表提交、入库"""
        log.info('APP-A明细表提交、入库')
        self.ap.detail_commit()

    def test14_complete_task(self):
        """测试APP-A结果表完成任务单"""
        log.info('APP-A结果表完成任务单')
        self.ap.complete_task()

    def test15_serach_task(self):
        """测试APP-A首页面查询已完成的样本任务单"""
        EnterTab.enter_APPA(self.basepage)
        log.info('APP-A首页面查询已完成的样本任务单')
        self.ap.serach_task()


if __name__ == '__main__':
    unittest.main()
