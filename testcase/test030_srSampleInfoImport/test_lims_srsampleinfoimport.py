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

    def test01_add_sr_sample_info_import(self):
        """
        测试导入sr样本信息，并编辑外部样本信息登记详情
        """
        self.initialize()

        EnterTab.enter_sr_record(self.basepage)  # 点击样本项目信息修改按钮
        log.info('导入sr样本外部信息')
        self.SrImpt.sr_sample_import()

        log.info(' 对上传的sr信息进行编辑，进入信息登记详情页')
        self.SrImpt.edit_upload_sample()

        log.info('外部样本信息登记详情页，上传子文库信息，选择sr样本')
        self.SrImpt.sr_sample_detail()

    def test02_search_sample_info(self):
        """
        测试根据lims号查询样本登记信息
        """
        log.info(' 测试根据lims号查询样本登记信息')
        EnterTab.enter_sr_record(self.basepage)
        lists = self.SrImpt.search_lims()
        self.assertNotEqual(lists, 0, msg='样本信息修改成功')


if __name__ == '__main__':
    unittest.main()
