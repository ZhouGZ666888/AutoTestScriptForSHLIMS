# -*- coding: utf-8 -*-
# @Time    : 2022/02/08
# @Author  : guanzhong.zhou
# @File    : 数据修改模块测试用例封装
import unittest
from common import all_path
from common.editYaml import read_yaml
from pageobj.datachangePage import DataChangePage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class DateModification(MyTest):
    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.dc = DataChangePage(self.driver)

    def enter_func_page(self):
        """
        调用打开页面方法，直接进入核酸提取明细表或者结果表页面，对提取进行数据修改
        """
        datas = read_yaml(all_path.sampledata_path)  # 获取测试登录的账号/密码配置数据
        now_handle = self.basepage.get_current_window_handle()
        self.dc.enter_function_page(datas['datachange_url'])
        print('打开的URL地址', datas['datachange_url'])
        all_handles = self.basepage.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.basepage.close()
                self.basepage.switch_to_window(handle)
                self.basepage.wait_loading()
        self.basepage.sleep(1)

    def test01_dataChange(self):
        """
        测试提取明细表，对样本数据进行修改并提交审核
        """
        self.initialize()
        self.enter_func_page()
        log.info('核酸提取明细表数据修改操作')
        self.dc.extraction_detail_datachange()

    def test02_datachange_task_review(self):
        """
        测试对提交的数据修改任务进行审核操作
        """

        log.info('切换用户进行数据修改审批')
        self.dc.batch_submit_for_review()
        self.login_action('guoqi.dong')
        EnterTab.enter_unresolve_job(self.basepage)
        log.info('数据修改审核操作')
        page = self.dc.edit_task()
        self.assertEqual(page, '完成', '审核数据修改任务单不成功！')

    def test03_search_task(self):
        """
        测试根据查询条件查询数据修改任务单功能
        """
        EnterTab.enter_update_sample(self.basepage)
        log.info('数据修改任务单查询操作')
        page1, page2, page3 = self.dc.search_task()
        self.assertEqual(page2, page3, '任务单号不一致')
        self.assertEqual(page1, '完成', '审核状态不是完成状态')


if __name__ == '__main__':
    unittest.main()
