import unittest
from PageElemens.libraryquantification_ele import *
from common.all_path import wkdl_hdsr_file_path
from pageobj.libraryquantificationPage import LibraryQuantificationPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class LibraryHdQuantification(MyTest):
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
        info=self.wkdl.get_huada_sr_sample()  # 核对lims，添加至任务单
        log.info('保存任务单，进入明细表')
        self.wkdl.enter_result_list(enter_detail_list_btn, '文库定量明细表')  # 保存任务单，进入明细表

        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_import_huada_sr_sample(self):
        """测试明细表导入华大样本数据"""
        log.info("明细表导入华大样本数据")
        self.wkdl.detail_import_huada_sr_sample()

    def test03_detail_batch_data(self):
        """测试明细表sr数据选择测序仪、预计上机时间、FC代码、预设Lane号"""
        log.info('明细表sr数据选择测序仪、预计上机时间、FC代码、预设Lane号')
        self.wkdl.detail_batch_data()

    def test04_detail_generate_product(self):
        """测试明细表华大样本生成生成结果"""
        log.info("明细表华大样本生成生成结果")
        self.wkdl.detail_huada_sr_sample_generate_product()

    def test05_detail_hd_single_gradient_quantification(self):
        """测试单梯度定量，华大SR数据导入"""
        log.info('单梯度定量，华大SR数据导入')
        self.wkdl.hd_single_gradient_quantification()

    def test06_detail_enter_result(self):
        """测试明细表进入结果表"""
        log.info('明细表进入结果表')
        self.wkdl.enter_result_list(enter_result_list_btn, '文库定量结果表')  # 进入文库定量结果表

    def test08_result_huada_sr_sample_write_import_file(self):
        """测试结果表华大样本导入数据"""
        log.info('结果表华大样本导入数据')
        self.wkdl.result_huada_sr_sample_write_import_file()

    def test09_standard_sample_import(self):
        """测试标准品数据导入"""
        log.info('标准品数据导入')
        self.wkdl.standard_sample_import()

    def test10_detail_commit(self):
        """测试文库定量结果表提交操作"""
        log.info(' 文库定量结果表提交操作')
        self.wkdl.result_submit_sample()
        log.info(' 文库定量结果表样本下一步流程写入Excel')
        self.wkdl.write_data_to_excel()
        self.wkdl.goback_detail()

    def test11_detail_submit(self):
        """返回明细表提交、入库"""
        self.wkdl.detail_sumbit()  # 明细表提交操作
        pageinfo = self.wkdl.detail_into_storage()  # 明细表样本入库操作
        log.info(" 进入结果表完成任务单")
        self.assertEqual(pageinfo, '完成', "入库失败，请检查数据！！！")

    def test12_complete_task(self):
        """完成任务单"""
        save_info3 = self.wkdl.complete_task()
        self.assertEqual(save_info3[6:].strip(), '完成', '完成任务单失败！')

    def test13_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_libquant(self.basepage)  # 点击文库定量导航树
        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.wkdl.serach_task(wkdl_hdsr_file_path)  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
