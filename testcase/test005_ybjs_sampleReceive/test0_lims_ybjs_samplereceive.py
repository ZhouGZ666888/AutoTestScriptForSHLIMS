import unittest
from common.Main import MyTest
from common.enter_tab import *
from common.logs import log
from pageobj.samplerecPage import SampleReceivePage


class SampleReceive(MyTest):

    def setUp(self) -> None:
        self.src = SampleReceivePage(self.driver)

    def test01_serachOrder(self):
        """
        测试接样列表搜索订单号
        """
        self.initialize()
        log.info('登录系统，进入样本接收页面')
        EnterTab.enter_samplereceive(self.basepage)
        log.info("搜索订单号")
        self.src.search_order()

    def test02_addOrderProductProject(self):
        """测试接样明细编辑订单产品、项目信息"""
        log.info("添加样本的项目信息类型")
        self.src.add_sample_type()

    def test03_addorderSample(self):
        """测试接样新增样本，选择样本类型"""
        log.info("添加样本并为样本选择样本类型")
        self.src.sampleRec_sampleDetail()

    def test04_addgenerate_laboratory_process(self):
        """测试接样生成实验流程"""
        log.info("为样本选择实验流程")
        self.src.generate_laboratory_process()

    def test05_fillSampleinfo(self):
        """
        测试录入样本包装量和样本计量等填充信息
        """
        log.info("录入样本计量、选择质检结果、接样备注")
        self.src.input_sampleamt()
        log.info("把接样样本信息存入对应的Excel文件中")
        self.src.save_all_samples_excel()

    def test06_submit_sample_for_review(self):
        """测试批量提交审核"""
        log.info("批量提交审核")
        self.src.submit_sample_for_review()
        log.info("页面退出登录按钮，切换登录用户")
        self.src.batch_submit_for_review()

    def test07_batchSubmission(self):
        """测试接样审核，完成审核功能"""
        self.login_action('guanzhong.zhou')
        EnterTab.enter_samplereceive(self.basepage)
        self.src.search_order()
        self.src.batch_review()


if __name__ == '__main__':
    unittest.main()
