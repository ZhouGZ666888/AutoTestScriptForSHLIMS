import unittest
from common.screenshot import Screenshot
from pageobj.pathologycheckPage import WorkSheet
from PageElemens.pathologycheck_ele import result_save, result_all_chioce, submit_success, result_save_pd, \
    all_chioce_pd, submit_success_pd
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class PathologyCheck(MyTest):

    def setUp(self) -> None:
        self.bljy = WorkSheet(self.driver)

    def test01_add_and_save_HETask(self):
        """测试新建HE病理任务，筛选并添加病理样本到任务单"""
        self.initializes()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_pathology(self.basepage)
        log.info('病理待选表，新建HE病理任务')
        self.bljy.add_task()
        log.info('病理待选表，选择HE病理类型')
        self.bljy.select_tasktype_sop(1)
        self.bljy.check_lims_num()
        self.bljy.add_select_task_or_save()
        result = self.bljy.findelement('xpath', '//*[contains(text(),"任务单保存成功")]')
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("病理检验待选表点击核对lims号，录入样本号进行查询，勾选查询结果，并保存任务单号","保存任务单成功")
        self.assertIsNotNone(result)

    def test02_edit_HE_pathology_result(self):
        """
        测试HE病理任务结果表数据录入、保存、提交功能
        """
        self.bljy.enter_result_list()
        self.bljy.edit_result_pageinfo()
        self.bljy.sava_result(result_save)

        self.bljy.submit_result(result_all_chioce, submit_success)
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("HE病理任务表单录入完成后，点击提交按钮进行结果表提交","提交任务单成功，状态为完成")

        result = self.bljy.findelement('xpath', '//*[contains(text(),"保存成功")]')  # 提交任务单页面提示信息为“保存成功”
        self.assertIsNotNone(result)

    def test03_add_and_save_PDL1Task(self):
        """
        测试新建PD-L1病理任务，筛选并添加病理样本到任务单
        """
        EnterTab.enter_pathology(self.basepage)
        self.bljy.add_task()
        log.info('病理待选表，选择PD-L1(28-8)病理类型')
        self.bljy.select_tasktype_sop(2)
        self.bljy.check_lims_num()
        self.bljy.add_select_task_or_save()
        # 调用自定义截图方法

        result = self.bljy.findelement('xpath', '//*[contains(text(),"任务单保存成功")]')
        Screenshot(self.driver).get_img("病理检验待选表，把接样的病理样本添加进PD-L1(28-8)病理任务","添加样本成功")
        self.assertIsNotNone(result)

    def test04_edit_PD_L1_pathology_result(self):
        """
        测试PD-L1(28-8)病理任务结果表数据录入、保存、提交功能
        """
        self.bljy.enter_result_list()
        self.bljy.edit_result_pageinfo_PD()  # 编辑结果表
        self.bljy.sava_result(result_save_pd)  # 点击保存结果
        self.bljy.submit_result(all_chioce_pd, submit_success_pd)  # 点击提交结果表

        # 调用自定义截图方法

        result = self.bljy.findelement('xpath', '//*[contains(text(),"任务提交成功")]')  # 提交任务单页面提示信息为“任务提交成功”
        Screenshot(self.driver).get_img("PD-L1(28-8)病理任务表单录入完成后，点击提交按钮进行结果表提交","提交任务单成功，任务状态为完成")
        self.assertIsNotNone(result)

    def test5_search(self):
        """
        根据样本lims号，查询该样本所在的任务单
        """
        EnterTab.enter_pathology(self.basepage)
        samples = self.bljy.serach_task()
        self.assertNotEqual(samples, 0, '查询结果错误')


if __name__ == '__main__':
    unittest.main()
