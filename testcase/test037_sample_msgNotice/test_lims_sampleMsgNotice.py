# -*- coding: utf-8 -*-
# @Time    : 2022/02/23
# @Author  : guanzhong.zhou
# @File    : 样本消息通知模块测试用例封装
import unittest
from pageobj.samgpleMsgNoticePage import SampleMsgNoticePage
from common.enter_tab import EnterTab
from common.logs import log
from common.Main import MyTest


class SampleMsgNotice(MyTest):

    def setUp(self) -> None:
        """
        初始化浏览器驱动
        """
        self.smn = SampleMsgNoticePage(self.driver)

    def test01_add_sample_notice_task(self):
        """
        测试新建样本通知消息任务，录入通知内容，并发送
        """
        self.initialize()
        EnterTab.sample_message_notice(self.basepage)  # 点击样本通知消息列表按钮

        log.info('样本通知消息任务新建任务单，录入待通知样本lims号、通知内容并发送通知')
        self.smn.add_sample_notice_task()

        log.info('核酸提取模块新建任务单，将接收通知消息的样本加入任务单')
        self.smn.add_extraction_task()

        log.info('通知消息样本接收到通知消息，对消息进行处理')
        pageinfo = self.smn.notice_process()
        self.assertEqual(pageinfo, '测试通知消息', msg='通知消息错误')

    def test02_change_by_labcode(self):
        """
        测试样本通知消息处理完后，校验通知状态是否符合预期
        """
        # 传入驱动
        EnterTab.sample_message_notice(self.basepage)  # 点击样本通知消息列表按钮
        log.info('样本通知消息处理完后，消息列表根据lims号搜索出任务单，校验通知状态是否符合预期')
        res1, res2 = self.smn.sample_task_status()
        self.assertEqual(res1, '已处理', msg='通知消息错误')
        self.assertEqual(res2, '已读', msg='通知消息错误')


if __name__ == '__main__':
    unittest.main()
