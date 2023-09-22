# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
from PageElemens.kwgl_ele import *
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleKwgl(BasePage):
    """
    列表页，详情页的动作封装
    """

    def kwgl_change_role(self, userid, role_id, vaild):
        """
        将切换用户是否为库管功能封装
        """

        log.info("修改用户角色，修改为临时库权限")
        sqlData = 'UPDATE sys_user_role SET is_valid=' + "'" + vaild + "'" + ' WHERE user_id=' + "'" + userid + "'" + 'AND ' \
                                                                                                                      'role_id=' + "'" + role_id + "'"

        executeSql.test_update_27mysql(sqlData)
        self.sleep(3)

    def kwgl_add_temporary_storage(self, storage_name, username):
        """
        将新建临时库功能封装
        """

        log.info("点击新增按钮")
        self.clicks('xpath', kwgl_list_add_ls_button)

        self.sleep(1)
        log.info("点击输入框，输入库位信息")
        self.clicks('xpath', kwgl_list_add_ls_name)
        self.input('xpath', kwgl_list_add_ls_name, storage_name)
        self.sleep(0.5)

        log.info("点击下拉框，选择库位位置")
        self.clicks('xpath', kwgl_list_add_ls_location_select)
        self.clicks('xpath', kwgl_list_add_ls_location)
        self.sleep(0.5)

        log.info("输入库位位置描述信息")
        self.clicks('xpath', kwgl_list_add_ls_location_desc)
        self.input('xpath', kwgl_list_add_ls_location_desc, '国旗测试新建库位-描述信息')
        self.sleep(0.5)

        log.info('点击编辑按钮，弹框中输入使用人姓名')
        self.clicks('xpath', kwgl_list_add_ls_user)
        self.input('xpath', kwgl_list_add_ls_username, username)
        self.sleep(2)
        log.info('弹框中输入使用人姓名，系统联想成功')
        self.clicks('xpath', kwgl_list_add_ls_username_search)
        self.sleep(1)
        self.clicks('xpath', kwgl_list_add_ls_username_add_butoon)
        self.sleep(1)

        log.info('确认添加使用人')
        self.clicks('xpath', kwgl_list_add_ls_username_add_confirmn)

        self.sleep(2)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("库位管理，点击新增临时库，录入库位信息后保存","新建库位成功")

        log.info('确认修改库位信息，完成修改')
        self.clicks('xpath', kwgl_list_add_ls_confirm)
        self.sleep(0.5)

    def kwgl_list_search(self, storage_name):
        """
        将新建临时库功能封装
        """

        log.info("进入列表页，点击搜索按钮")
        self.sleep(1)
        self.clicks('xpath', kwgl_list_search_button)
        self.sleep(0.5)
        log.info("输入指定的库位姓名")
        self.clicks('xpath', kwgl_list_search_name)
        self.input('xpath', kwgl_list_search_name, storage_name)
        self.sleep(0.5)
        log.info("搜索指定库位名称成功")
        self.clicks('xpath', kwgl_list_search_confirm)
        self.sleep(0.5)


if __name__ == '__main__':
    test = SampleKwgl(BasePage)
    test.kwgl_change_role('2535', '2001', '0')
