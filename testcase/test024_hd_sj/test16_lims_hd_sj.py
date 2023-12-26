import re
import unittest
from common.all_path import hd_sj_file_path
from pageobj.sjsequecingPage import SjSequecingPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest
from PageElemens.sj_sequecing_ele import *


class SjSequecing(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.sj = SjSequecingPage(self.driver)

    def test01_add_sequencing_task(self):
        """
        测试新建上机任务单，在待选表录入上机批次号，FC SN码，浓度调整SOP,上机SOP，添加样本、保存任务单
        """
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_sequencing(self.basepage)  # 点击上机导航树

        log.info('登录系统，进入上机页面')
        # 传入驱动
        log.info('新建任务单，录入上机批次号，FC SN码，浓度调整SOP,上机SOP')
        self.sj.add_hd_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.sj.addSelect_or_save_task(hd_sj_file_path)  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.sj.enter_result_list('css', enter_detail_list_btn, '上机浓度调整前明细表')  # 保存任务单，进入明细表
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_hd_detail_data_input(self):
        """华大上机明细表表单数据录入"""
        log.info("上机浓度调整前明细表自动计算")
        self.sj.hd_detail_data_input()

    def test03_hd_detail_datch_data(self):
        """华大上机明细表批量数据录入"""
        log.info("华大上机明细表批量数据录入")
        info = self.sj.hd_detail_datch_data()
        self.assertEqual(info, "录入成功", "批量数据录入失败！！")

    # def test04_hd_detail_autoCompleteLabel(self):
    #     """华大上机明细表自动计算标签"""
    #     log.info("华大上机明细表自动计算标签")
    #     info = self.sj.hd_detail_autoCompleteLabel()
    #     self.assertEqual(info, "双标签", "自动计算标签失败！！")

    def test05_hd_detail_generateNo(self):
        """华大上机明细表生成上机分组号"""
        log.info("华大上机明细表生成上机分组号")
        info = self.sj.hd_detail_generateNo()
        self.assertEqual(info, "生成上机分组号成功", "生成上机分组号失败！！")

    def test06_hd_detail_confirm(self):
        """华大上机明细表确认上机"""
        log.info("华大上机明细表确认上机")
        self.sj.hd_detail_confirm()
        self.assertIsNotNone(re.search(r'已确认', self.sj.get_source))

    def test07_hd_detail_create_samplesheet(self):
        """华大上机明细表生成samplesheet"""
        log.info("华大上机明细表生成samplesheet")
        self.sj.hd_detail_create_samplesheet()

    def test08_hd_detail_sumbit(self):
        """华大上机明细表明细表提交"""
        log.info("华大上机明细表明细表提交")
        info = self.sj.hd_detail_sumbit()
        self.assertEqual(info, "样本提交成功", "样本提交失败！！")

    def test09_hd_sj_result(self):
        """华大上机结果表完成任务单"""
        log.info("华大上机结果表完成任务单")
        self.sj.hd_sj_result()


if __name__ == '__main__':
    unittest.main()
