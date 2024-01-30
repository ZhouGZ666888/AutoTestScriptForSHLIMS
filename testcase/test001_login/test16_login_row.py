import unittest
from common.Main import MyTest
from common import all_path
from common.editYaml import read_yaml
from ddt import ddt, data
from common.logs import log
from common.screenshot import Screenshot


@ddt
class LimsLogin(MyTest):
    """
    世和Lims登录功能点
    """
    datas = read_yaml(all_path.testdata_path)  # 获取测试登录的账号/密码配置数据

    def setUp(self) -> None:
        log.info('打开浏览器,窗口最大化')
        self.basepage.max()
        log.info('访问地址')
        self.basepage.openbrower()
        log.info('切换登录方式为账号密码登录')
        self.lg.execute_login_js()


    def test01_error_username_login(self):
        """
        用戶名错误，登录失败
        """
        try:
            log.info('输入错误账号/密码登录：error/error')
            self.lg.input_username("error")
            self.lg.input_password("error")
            log.info('点击登录按钮')
            self.lg.click_login_btn()
        except AssertionError as r:
            log.error("登录这里报错了 ：%s" % r)
            # 获取登录失败后的提示语tips
        login_error = self.basepage.get_text('xpath',
                                             "//div[@class='el-message el-message--error']/p[text()='请填写正确的用户名、密码']")
        # 断言提示语
        self.assertIn("请填写正确的", login_error)
        log.info('获取登录失败的提示语：{}'.format(login_error))

    @data(*datas["companies"])
    def test02_login_data(self, datas):
        """
        数据驱动测试多个账号登录LIMS系统
        """
        try:
            log.info("清空输入框信息")
            self.lg.clear_username_by_js()
            self.lg.clear_password_by_js()

            log.info('输入账号：{}'.format(datas['name']))
            self.lg.input_username(datas['name'])

            log.info('输入密码：{}'.format(datas['password']))
            self.lg.input_password(datas['password'])

            log.info('点击登录')
            self.lg.click_login_btn()

        except Exception as r:
            log.warning("登录这里报错了 ：%s" % r)
        self.basepage.wait_loading()
        self.basepage.sleep(3)
        log.info('登录成功后校验当前地址正确')
        current_url = self.basepage.get_current_url()
        self.assertIn("home", current_url)
        Screenshot(self.driver).get_img("用户录入账号密码登录系统", "登录系统成功")

if __name__ == '__main__':
    unittest.main()
