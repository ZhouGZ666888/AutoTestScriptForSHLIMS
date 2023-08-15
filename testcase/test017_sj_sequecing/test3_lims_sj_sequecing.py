import unittest
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
        self.sj.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.sj.addSelect_or_save_task()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.sj.enter_result_list('css', enter_detail_list_btn, '上机浓度调整前明细表')  # 保存任务单，进入明细表
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_before_concentration_adjustment(self):
        """
          测试上机浓度调整前明细表自动计算、生成浓度调整前结果、提交、入库
        """
        log.info("上机浓度调整前明细表自动计算")
        self.sj.detail_before_concentration_adjustment_data()
        log.info("上机浓度调整前明细表生成浓度调整前结果")
        self.sj.detail_before_concentration_adjustment_create_concentration_adjustment_result()
        log.info("上机明细表提交")
        self.sj.detail_before_concentration_adjustment_sumbit()
        log.info("上机明细表明细表入库")
        pageinfo = self.sj.detail_before_concentration_adjustment_sumbit_into_storage()
        self.sj.enter_result_list('css', before_concentration_adjustment_next, '浓度调整后样本明细')  # 进入上机浓度调整后明细表
        self.assertEqual(pageinfo, "完成", "入库失败！！")

    def test03_after_before_concentration_adjustment(self):
        """
           测试上机结果表批量粘贴导入实验数据、生成上机分组号，提交，完成任务单
        """
        log.info("浓度调整后明细表批量数据录入、自动计算")
        self.sj.detail_after_concentration_adjustment_auto_calculate()
        log.info("浓度调整后明细表生成上机分组号")
        self.sj.detail_after_concentration_adjustment_create_sequencing_group_number()
        log.info("浓度调整后明细表确认上机")
        self.sj.detail_after_concentration_adjustment_confirm_sequencing()
        log.info('浓度调整后明细表 生成samplesheet')
        self.sj.detail_after_concentration_adjustment_create_samplesheet()
        log.info('浓度调整后明细表 提交')
        self.sj.detail_after_concentration_adjustment_submit()
        log.info('浓度调整后明细表 入库')
        pageinfo = self.sj.detail_after_concentration_adjustment_deposit_into_Storage()
        self.sj.enter_result_list('css', after_concentration_adjustment_submit_enter_the_result_list,
                                  '浓度调整后样本明细')  # 进入上机结果表
        self.assertEqual(pageinfo, "完成", "入库失败！！")

    def test04_importFile_and_CompletedResult(self):
        """
        测试上机结果表导入FC质控结果模板，完成任务单操作
        """
        log.info('上机结果表导入FC质控结果模板')
        self.sj.import_fc_quality_control_result()
        log.info('上机结果表完成任务单')
        pageinfo = self.sj.complete_task()
        self.assertEqual(pageinfo[6:].strip(), '完成', '完成任务单失败！')


if __name__ == '__main__':
    unittest.main()
