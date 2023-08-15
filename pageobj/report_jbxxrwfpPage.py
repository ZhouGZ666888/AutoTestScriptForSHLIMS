# -*- coding: utf-8 -*-
# @Time    : 2021/12/28
# @Author  : guanzhong.zhou
# @File    : 报告-基本信息任务分配模块页面方法封装
from PageElemens.report_jbxxrwfp_ele import *
from common.editYaml import *
from common.all_path import report_views_refresh_sql, orderNub_path
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from uitestframework.basepageTools import BasePage
from common.logs import log


def execute_sql():
    """
    报告模块操作前先执行一遍sql，刷新报告数据对的视图
    """
    # 读取sql
    with open(report_views_refresh_sql, 'r', encoding='utf-8', errors='ignore') as f:
        sa = f.read()
    executeSql.test_updateByParam(sa)
    print('执行数据库刷新视图成功<+_+>')


class ReportBasicInfoTaskAssignmentPage(BasePage):
    """
    报告-基本信息任务分配模块页面基础方法封装
    """

    def serach_order(self):
        """根据样本号查询待分配样本"""
        log.info("根据样本号查询待分配样本")
        execute_sql()  # 刷新报告数据对的视图
        order = read_yaml(orderNub_path)
        self.input('css', order_num, order['order_number'])
        self.sleep(1)
    def click_search_btn(self):
        """
        点击搜索按钮
        """
        log.info("点击搜索按钮")
        self.clicks('css', search_btn)
        self.wait_loading()

    def batch_choice_charge_person(self):
        """
        批量选择负责人
        """
        log.info("批量选择负责人")
        self.clicks('css', all_choice)  # 全选搜索结果
        self.sleep(0.5)
        self.clicks('css', batch_choice_person_charge)  # 点击批量选择负责人
        self.clicks('css', charge_person_input)
        self.input('css', charge_person_input, 'zgz')  # 弹框中录入负责人名称
        self.wait_loading()
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告信息任务分配，批量选择负责人")
        self.clicks('xpath', charge_person_choice)
        self.clicks('css', batch_choice_person_charge_comfirm)  # 选择负责人后确认
        pageinfo = self.get_page_info()
        self.wait_loading()
        return pageinfo

    def get_page_info(self):
        """
        获取数据操作后，页面给出的提示信息语
       选择负责人成功
        """
        log.info('获取页面提示信息')
        return self.get_text('xpath', page_info)
