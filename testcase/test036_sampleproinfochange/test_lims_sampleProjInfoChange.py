# -*- coding: utf-8 -*-
# @Time    : 2022/02/09
# @Author  : guanzhong.zhou
# @File    : 样本项目信息修改模块测试用例封装
import unittest
from PageElemens.sampleProjectInfoChange_ele import *
from pageobj.sampleProjectInfoChangePage import SampleProInfoChangePage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class SampleProInfoChange(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.spic = SampleProInfoChangePage(self.driver)

    def test01_ModifSampleInformationByLims(self):
        """
        测试样本项目信息修改，按样本lims号检索后，导出、导入修改模板，核对导入后数据库样本项目信息更新状态
        """
        self.initializes()

        EnterTab.sample_project_info_change(self.basepage)
        log.info('样本项目信息修改---新建任务单，按lims号检索样本信息，并导出样本-项目信息')
        self.spic.add_task('lims号', search_by_lims_tab, search_by_lims)

        log.info('样本项目信息，修改导出的样本-项目信息模板，更新样本项目号')
        self.spic.edit_download_info()

        log.info('导入修改后样本-项目信息')
        pageinfo = self.spic.upload_sampleinfo()
        self.assertEqual(pageinfo, '上传成功', msg='上传导入文件失败')

    def test02_change_by_labcode(self):
        """
        测试样本项目信息修改，按样本实验室号检索后，导出、导入修改模板，核对导入后数据库样本项目信息更新状态
        """

        log.info('样本项目信息修改---新建任务单，按实验室号检索样本信息，并导出样本-项目信息')
        self.spic.add_task('实验室号', search_by_labCode_tab, search_by_labCode)

        log.info('样本项目信息，修改导出的样本-项目信息模板，更新样本项目号')
        self.spic.edit_download_info()

        log.info('导入修改后样本-项目信息')
        pageinfo = self.spic.upload_sampleinfo()
        self.assertEqual(pageinfo, '上传成功', msg='上传导入文件失败')

    def test03_check_sample_project(self):
        """
        测试从数据库获取修改后样本项目信息，并校验是否修改正确
        """
        log.info('数据库获取修改后样本项目信息,进行比对，验证样本信息是否修改成功')
        sampInfo1, sampInfo2 = self.spic.get_sampleProId_by_changeAfter()
        self.assertEqual(sampInfo1, sampInfo2, msg='样本信息修改成功')


if __name__ == '__main__':
    unittest.main()
