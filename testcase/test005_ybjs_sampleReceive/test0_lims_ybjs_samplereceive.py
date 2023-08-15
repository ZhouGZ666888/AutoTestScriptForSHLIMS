import unittest
from common.Main import MyTest
from common.enter_tab import *
from common.logs import log
from pageobj.samplerecPage import SampleReceivePage


class SampleReceive(MyTest):

    def setUp(self) -> None:
        self.src = SampleReceivePage(self.driver)

    def test01_addSamples(self):
        """
        测试新增接样样本，选择样本类型，根据样本类型选择并生成对应实验流程
        """
        self.initialize()

        log.info('登录系统，进入样本接收页面')
        EnterTab.enter_samplereceive(self.basepage)

        log.info("搜索订单号")
        self.src.search_order()

        log.info("添加样本的项目信息类型")
        self.src.add_sample_type()

        log.info("添加样本并为样本选择样本类型")
        self.src.sampleRec_sampleDetail()

        log.info("为样本选择实验流程")
        self.src.generate_laboratory_process()

    def test02_fillSampleinfo(self):
        """
        录入样本包装量和样本计量等填充信息，并批量提交审核
        """

        log.info("录入样本计量、选择质检结果、接样备注")
        self.src.input_sampleamt()

        log.info("把接样样本信息存入对应的Excel文件中")
        self.src.save_all_samples_excel()

        log.info("批量提交审核")
        self.src.submit_sample_for_review()

        log.info("页面退出登录按钮，切换登录用户")
        self.src.batch_submit_for_review()

    def test03_batchSubmission(self):
        """
        对样本进行批量提交审核，切换用户进行完成审核功能测试
        """
        self.login_action('guanzhong.zhou')
        EnterTab.enter_samplereceive(self.basepage)

        self.src.search_order()
        self.src.batch_review()


'''

FBI提醒，本处test04注释代码，为流转表设置富集时间用，平时不用，需要时可放开注释
FBI提醒，本处test04注释代码，为流转表设置富集时间用，平时不用，需要时可放开注释
FBI提醒，本处test04注释代码，为流转表设置富集时间用，平时不用，需要时可放开注释
FBI提醒，本处test04注释代码，为流转表设置富集时间用，平时不用，需要时可放开注释


'''
# def test04_set_poollingtime(self):
#     """
#     进入流转表设置富集节点的预计富集时间
#     uesrname="guanzhong.zhou"
#     """
#     # 调用登录
#     Lims_Login_sccuess(self.driver).login_single('guanzhong.zhou')
#
#     self.basepage.wait_loading()
#     EnterTab.enter_workflow(self.basepage)#点击【流转表】
#     self.basepage.wait_loading()
#     EnterTab.enter_single_workflow(self.basepage)#点击【单样本流转表】
#
#     tomorrow = (datetime.datetime.now() + datetime.timedelta(days=+2)).strftime('%Y.%m.%d')
#     print(tomorrow)
#     test = SampleReceivePage(self.driver)#调用流转表设置富集预计时间
#     test.set_estimated_generated_time(tomorrow)


if __name__ == '__main__':
    unittest.main()
