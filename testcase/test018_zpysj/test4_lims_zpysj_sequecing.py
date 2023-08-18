import unittest, re
from pageobj.zpysjPage import MassspectrPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class Massspectr(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.ms = MassspectrPage(self.driver)

    def test01_add_sequencing_task(self):
        """
        测试新建质谱仪上机任务单，在待选表录入质谱仪上机任务类型,质谱仪上机SOP，添加样本、保存任务单
        """
        self.initialize()
        log.info('登录系统，进入质谱仪上机页面')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_Massspectr(self.basepage)  # 点击质谱仪上机导航树

        log.info('新建任务单，录入质谱仪上机任务类型,质谱仪上机SOP')
        self.ms.add_task()
        log.info('核对样本lims号并选中加入任务单')
        info = self.ms.check_lims_num()  # 核对lims，添加至任务单
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_detail_data_processing(self):
        """
          测试质谱仪上机明细表录入表单数据，导入样本列表进行编辑
        """
        log.info("质谱仪上机明细表录入批量数据")
        self.ms.detail_libconstruction()
        log.info("质谱仪上机明细表导出样本，并对列表中样本进行编辑")
        self.ms.detail_exportData()

    def test03_import_data(self):
        """
           测试质谱仪上机明细表导入Excel数据，并确认上机
        """
        log.info("导入编辑好的Excel数据")
        self.ms.detail_importData()
        log.info("确认上机操作")
        self.ms.detail_confirm_sequencing()
        result = re.search(r'当前任务单中所有样本已确认上机', self.ms.get_source)
        self.assertIsNotNone(result)

    def test04_detail_submit(self):
        """
        测试质谱仪上机提交、入库操作
        """
        log.info('质谱仪上机结果表导入FC质控结果模板')
        self.ms.detail_submit()
        log.info('质谱仪上机结果表完成任务单')
        pageinfo = self.ms.detail_into_storage()
        self.assertEqual(pageinfo.strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_Massspectr(self.basepage)  # 点击质谱仪导航树

        log.info(" 测试根据添加到的任务单中的lims样本号搜索对应的任务单")
        samples = self.ms.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
