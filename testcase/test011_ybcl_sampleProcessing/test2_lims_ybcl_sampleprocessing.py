import unittest
from pageobj.sampleprocessingPage import SampleProcessingPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest
from PageElemens.sampleProcessing_ele import *


class SampleProcessing(MyTest):

    def setUp(self) -> None:
        self.spp = SampleProcessingPage(self.driver)

    def test01_add_SampleProcessing_task(self):
        """
        测试新建样本处理任务单，筛选并添加待处理样本到任务单中
        """
        self.initialize()

        log.info('进入样本处理页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_preparation(self.basepage)
        # 新建样本处理任务单
        self.spp.add_task()
        info = self.spp.check_lims_num()
        self.spp.enter_result_list(enter_result_list_btn, '样本处理明细表')
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_Sample_detail_to_be_processed(self):
        """
        测试样本处理明细表数据录入、保存、提交功能
        """

        self.spp.sample_detail()  # 样本数据录入，入库类型、库位选择
        self.spp.enter_result_list(goResult, '结果表')

    def test03_product_result(self):
        """
        测试样本处理结果表，数据录入、提交、完成任务单
        """
        # 录入结果表数据，并提交
        save_info1 = self.spp.sample_result_process_sumbit()
        # 写入样本lims号和实验室号存入Excel进行数据流转，并返回明细表
        self.spp.write_data_to_excel()
        self.spp.goback_detail()
        self.assertEqual(save_info1, '是', '提交失败!')

    def test04_detail_submit(self):
        """
        返回明细表提交、入库,完成任务单
        """

        detail_sumbit_staus = self.spp.detail_sumbit()
        save_info2 = self.spp.deposit_into_storage()  # 样本入库操作

        save_info3 = self.spp.complete_task()

        self.assertEqual(detail_sumbit_staus, '待入库', "入库失败，请检查数据！！！")
        self.assertEqual(save_info2, '完成', "入库失败，请检查数据！！！")

        self.assertEqual(save_info3[6:].strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        # 传入驱动
        EnterTab.enter_test_center(self.basepage)

        EnterTab.enter_preparation(self.basepage)
        samples = self.spp.serach_task()  # 根据lims号搜索任务单号

        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
