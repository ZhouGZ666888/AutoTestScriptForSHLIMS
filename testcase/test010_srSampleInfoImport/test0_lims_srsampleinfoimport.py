# -*- coding: utf-8 -*-
# @Time    : 2022/03/24
# @Author  : guanzhong.zhou
# @File    : sr样本信息登记测试用例封装
import unittest
from pageobj.srSampleInfoImportPage import SrSampleInfoImp
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class SrSampleInfoImport(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.SrImpt = SrSampleInfoImp(self.driver)

    def test01_sr_sample_import(self):
        """测试导入sr样本信息"""
        self.initialize()

        EnterTab.enter_sr_record(self.basepage)  # 点击SR样本信息登记按钮
        log.info('导入sr样本外部信息')
        self.SrImpt.sr_sample_import()

    def test02_sr_sample_childrenImport(self):
        """测试导入sr样本子文库信息信息"""
        log.info(' 测试根据lims号查询样本登记信息')
        self.SrImpt.sr_sample_childrenImport()

    def test03_sr_sample_match_lims(self):
        """测试一键匹配LIMS号"""
        log.info(' 测试根据lims号查询样本登记信息')
        info = self.SrImpt.match_lims()
        self.assertIsNotNone(info)


if __name__ == '__main__':
    unittest.main()
