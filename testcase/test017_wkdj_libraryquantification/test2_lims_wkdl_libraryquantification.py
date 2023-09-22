import unittest
from PageElemens.libraryquantification_ele import *
from common.all_path import wkdl_non_sr_file_path
from pageobj.libraryquantificationPage import LibraryQuantificationPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class LibraryQuantification(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.wkdl = LibraryQuantificationPage(self.driver)

    def test01_add_libraryquantification_task(self):
        """
        测试新建文库定量任务单，在待选表录入任务描述，选择任务sop,检索lims号，添加、保存任务单
        """
        log.info('登录系统，进入文库定量页面')
        self.initialize()
        if self.wkdl.isElementExists('css', electronic_experiment_record_signed_tips):
            self.wkdl.clicks('css', electronic_experiment_record_signed_tips)
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libquant(self.basepage)  # 点击文库定量导航树

        self.wkdl.add_task()  # 新建任务单，选择任务类型、操作类型、sop
        log.info('核对lims号和富集名称，添加至任务单')
        info = self.wkdl.check_lims_num()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.wkdl.enter_result_list(enter_detail_list_btn, '文库定量明细表')  # 保存任务单，进入明细表
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_libraryquantification_detail(self):
        """
          测试文库定量明细表批量批量粘贴导入实验数据、入库信息、提交入库
        """
        log.info("文库定量明细表选择入库信息、批量粘贴导入实验数据")
        self.wkdl.detail_libraryenrichment()
        log.info("文库定量明细表sr数据选择测序仪、预计上机时间、FC代码、预设Lane号")
        self.wkdl.sequencer_estimatedsequencingdate_fccode_preset_Lanenumber()
        log.info("文库定量明细表生成上机分组号，生成结果操作")
        self.wkdl.create_result_and_sequencing_group_number()
        log.info("文库定量明细表单梯度定量，SR、非SR数据导入")
        self.wkdl.single_gradient_quantification()

        self.wkdl.enter_result_list(enter_result_list_btn, '文库定量结果表')  # 进入文库定量结果表

    def test03_libraryquantification_result(self):
        """
        测试文库定量结果表批量粘贴导入实验数据、生成上机分组号，提交，完成任务单
        """
        log.info("结果表分别根据sr样本lims号、非sr样本分组号，写入模板")
        self.wkdl.result_data_write_import_file()
        log.info("从模板取出数据，批量粘贴导入")
        self.wkdl.non_sr_and_sr_data_paste_import()
        log.info("定量结果表，标准品数据导入")
        self.wkdl.standard_sample_import()
        log.info(' 文库定量结果表提交操作')
        pageinfo1 = self.wkdl.result_submit_sample()
        log.info(' 文库定量结果表样本下一步流程写入Excel')
        self.wkdl.write_data_to_excel()
        self.wkdl.goback_detail()

        self.assertEqual(pageinfo1, '样本提交成功', '提交失败!')

    def test04_detail_submit(self):
        """
        返回明细表提交、入库
        """
        self.wkdl.detail_sumbit()  # 明细表提交操作
        pageinfo = self.wkdl.detail_into_storage()  # 明细表样本入库操作
        log.info(" 进入结果表完成任务单")
        self.assertEqual(pageinfo, '完成', "入库失败，请检查数据！！！")

    def test05_complete_task(self):
        """完成任务单"""
        save_info3 = self.wkdl.complete_task()
        self.assertEqual(save_info3[6:].strip(), '完成', '完成任务单失败！')

    def test06_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libquant(self.basepage)  # 点击文库定量导航树
        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.wkdl.serach_task(wkdl_non_sr_file_path)  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
