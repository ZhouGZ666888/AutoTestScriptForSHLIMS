# -*- coding: utf-8 -*-
# @Time    : 2021/12/09
# @Author  : guanzhong.zhou
# @File    : 登录模块页面功能封装
from common import editYaml
from common.all_path import testdata_path
from uitestframework.basepageTools import BasePage
from common.logs import log


class LoginPage(BasePage):
    """LIMS登陆页面"""

    # lims登陆页面用户名输入框，元素定位
    username_loc = (
        '//*[@id="enterpriseUser1"]/div/div[3]/form/div[1]/div/div/input')

    # lims登陆页面密码输入框，元素定位
    password_loc = (
        '//*[@id="enterpriseUser1"]/div/div[3]/form/div[2]/div/div/input')
    # lims登陆页面登陆按钮，元素定位
    login_btn_loc = (
        '//*[@id="enterpriseUser1"]/div/div[3]/form/div[3]/div/button')

    js = "document.getElementById('enterpriseUser1').style.display = 'block';document.getElementById('enterpriseUser').style.display = 'none';"

    def execute_login_js(self):
        """LIMS登陆页面切换登录方式"""
        self.executeJscript(self.js)

    def input_username(self, text):
        """lims登陆页面输入用户名方法
        :param text:用户名"""
        self.input('xpath', self.username_loc, text)

    def input_password(self, text):
        """LIMS登陆页面输入密码方法
        :param text:密码"""
        self.input('xpath', self.password_loc, text)

    def click_login_btn(self):
        """LIMS登陆页面点击登陆按钮方法"""
        self.clicks('xpath', self.login_btn_loc)

    def clear_username_by_js(self):
        """清空用户名输入框方法"""
        username_input = self.findelement('xpath', self.username_loc)
        js = "arguments[0].value=''"
        self.executeJscript(js, username_input)


    def clear_password_by_js(self):
        """清空用户名输入框方法"""

        password_input = self.findelement('xpath', self.password_loc)
        js = "arguments[0].value=''"
        self.executeJscript(js, password_input)

    def explorer_console(self):
        """
        操作浏览器
        """
        log.info('打开浏览器')
        self.max()
        log.info('访问地址')
        self.openbrower()

    def login_single(self, name):
        """
        单独测试正确的账号密码登录
        """

        datas = editYaml.read_yaml(testdata_path)  # 获取测试登录的账号/密码配置数据
        try:
            # log.info("------TestCase Start!------")

            log.info('切换登录方式为账号密码登录')
            self.sleep(1)
            self.execute_login_js()

            log.info("清空输入框信息")
            self.clear_username_by_js()
            self.clear_password_by_js()

            if name == 'guanzhong.zhou':
                sort = 0
            elif name == 'guoqi.dong':
                sort = 1
            elif name == 'wei.sun':
                sort = 2
            else:
                sort = 1
            select_name = datas["companies"][sort]['name']
            select_password = datas["companies"][sort]['password']

            log.info('输入账号：{}'.format(select_name))
            self.input_username(select_name)
            self.sleep(0.5)
            log.info('输入密码：{}'.format(select_password))
            self.sleep(0.5)
            self.input_password(select_password)

            log.info('点击登录按钮')
            self.click_login_btn()
            self.wait_loading()



        except Exception as r:
            raise r

    def login_console(self, name):
        """
        登录功能
        :param name: 登录用户名
        """
        self.explorer_console()
        self.login_single(name)

    def witchUsers(self, name):
        """
        登录功能
        :param name: 登录用户名
        """
        self.login_single(name)


if __name__ == '__main__':
    LoginPage(BasePage)
