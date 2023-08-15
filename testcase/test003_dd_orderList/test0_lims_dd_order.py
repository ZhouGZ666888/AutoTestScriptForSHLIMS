import unittest
from common.screenshot import Screenshot
from pageobj.orderPage import OrderPage
from common.enter_tab import EnterTab
from common.Main import MyTest
from common.logs import log


class LimsOrder(MyTest):

    def setUp(self) -> None:
        self.od = OrderPage(self.driver)

    def test01_add_order(self):
        """
        测试新增订单并关联病历功能
        """
        log.info('登录系统，进入订单页面')
        self.initialize()

        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_order(self.basepage)
        log.info(" 调用新增方法")
        self.od.add_order()
        log.info(" 搜索并进入订单编辑页面")
        self.od.enter_edit()
        log.info(" 订单和病历关联")
        result = self.od.bl_dd_associate()
        self.assertIsNotNone(result)

    def test02_save_order(self):
        """
        录入订单详细信息并保存订单
        """
        log.info(" 编辑订单信息并保存")
        self.od.edit_order()
        result = self.od.save_add_order()
        self.assertIsNotNone(result)


    def test03_add_main_order(self):
        """
        测试设置主订单，关联主订单
        """
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_order(self.basepage)
        self.od.add_order()
        log.info("选择并进入订单编辑页面新建订单")
        self.od.enter_edit()
        # 编辑订单，关联病历
        self.od.bl_dd_associate()
        self.od.edit_order()
        log.info("设置主订单号")
        result = self.od.set_mian_order_number()
        self.od.save_add_order()
        # 调用自定义截图方法
        Screenshot(self.driver).get_img("保存订单")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
