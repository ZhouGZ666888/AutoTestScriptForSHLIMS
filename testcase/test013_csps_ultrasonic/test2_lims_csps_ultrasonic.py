import unittest
from pageobj.ultrasonicPage import UltrasonicPage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest
from PageElemens.ultrasonic_ele import *


class Ultrasonic(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.us = UltrasonicPage(self.driver)

    def test01_add_ultrasonic_task(self):
        """
        测试新建超声破碎任务单，在待选表选择任务类型、sop,检索lims号，添加、保存任务单
        """
        log.info('登录系统，进入超声破碎页面')
        self.initialize()
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_ultrafrac(self.basepage)  # 点击核酸提取导航树
        self.us.add_task()  # 新建任务单，选择任务类型、sop
        info = self.us.check_lims_num()  # 核对lims，添加至任务单
        self.us.enter_result_list(enter_detail_list_btn, '超声破碎明细表')  # 保存任务单，进入明细表
        self.assertEqual(info, "任务单保存成功", "保存样本到明细表失败！！")

    def test02_ultrasonic_detail(self):
        """
        测试超声破碎明细表批量数量录入、自动计算、提交、入库
        """
        log.info('测试超声破碎明细表批量数量录入、自动计算、提交、入库')
        self.us.aliquot_sample()  # 明细表分管操作
        self.us.detail_ultrasonic()  # 超声破碎明细表数据录入、自动计算操作
        self.us.enter_result_list(enter_result_list_btn, '超声破碎结果表')  # 进入超声破碎结果表

    def test03_ultrasonic_result(self):
        """
        测试超声破碎结果表修改产物类型、表单数据录入、提交任务单
        """
        log.info(' 测试超声破碎结果表修改产物类型、表单数据录入、提交和完成任务单')
        self.us.ultrasonic_result_data_input()  # 结果表产物类型、批量数录入
        self.us.ultrasonic_result_formdata_input()  # 结果表表单数据录入
        pageinfo = self.us.result_submit_sample()  # 结果表提交
        self.us.write_data_to_excel()  # 结果表下一步数据写入对应Excel
        self.us.goback_detail()
        self.assertEqual(pageinfo, '样本提交成功', '提交失败!')

    def test04_detail_submit(self):
        """
        返回明细表提交、入库,完成任务单
        """
        self.us.detail_sumbit()  # 明细表提交操作
        result = self.us.detail_into_storage()  # 明细表样本入库操作
        taskstatus = self.us.complete_task()  # 结果表完成任务单
        self.assertIsNotNone(result)
        self.assertEqual(taskstatus[6:].strip(), '完成', '完成任务单失败！')

    def test05_search_task_by_lims(self):
        """
        测试根据添加到的任务单中的lims样本号搜索对应的任务单
        """
        log.info('  测试根据添加到的任务单中的lims样本号搜索对应的任务单')
        EnterTab.enter_test_center(self.basepage)
        EnterTab.enter_ultrafrac(self.basepage)  # 点击核酸提取导航树
        samples = self.us.serach_task()  # 根据lims号搜索任务单号
        self.assertNotEqual(samples, 0, "查询结果错误，查询失败！")


if __name__ == '__main__':
    unittest.main()
