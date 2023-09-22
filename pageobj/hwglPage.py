# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
from PageElemens.hwgl_ele import *
from common.screenshot import Screenshot
from common.DataBaseConfig import executeSql
from uitestframework.basepageTools import BasePage
from common.logs import log


class SampleHwgl(BasePage):
    """
    列表页，详情页的动作封装
    """

    def hwgl_list_search(self):
        """
        列表页关于搜索功能的封装
        """

        log.info("点击样本盒列表的搜索按钮")
        self.clicks('xpath', hwgl_list_search_button)
        self.wait_loading()

        log.info("搜索弹框中输入指定盒子信息")
        self.clicks('xpath', hwgl_list_search_box_name)
        self.input('xpath', hwgl_list_search_box_name, '盒子')
        log.info("点击确定，搜索成功")
        self.clicks('xpath', hwgl_list_search_confirm)
        self.wait_loading()

    def hwgl_list_delete(self):
        """
        列表页关于删除功能的封装
        """

        log.info("点击选中指定盒位信息")
        self.clicks('xpath', hwgl_list_first_data)
        self.clicks('xpath', hwgl_list_detel)
        # 判断禁止删除的提示语是否可见
        is_toast = self.isElementExists('xpath', hwgl_list_detel_toast)
        if is_toast:
            log.info("校验盒位存在样本，不能删除功能")
            print("当前样本盒内有样本，不可删除")
        else:
            self.clicks('xpath', hwgl_list_detel_reason)
            self.input('xpath', hwgl_list_detel_reason, '测试删除样本盒')
            self.sleep(1)
            self.clicks('xpath', hwgl_list_detel_confirm)
            log.info("校验盒位不存在样本，可以删除功能")

    def hwgl_list_add(self, box_num, box_name):
        """
        列表页关于新增盒子功能的封装
        """

        log.info("点击新增按钮")
        self.clicks('xpath', hwgl_list_add)
        self.sleep(1)
        log.info("输入新建样本盒数量")
        self.input('xpath', hwgl_list_num, box_num)
        self.sleep(1)
        log.info("点击确定")
        self.clicks('xpath', hwgl_list_num_confirm)
        self.sleep(1)
        log.info("输入盒子名称")
        self.clicks('css', hwgl_detail_box_name)
        self.sleep(0.5)
        self.input('css', hwgl_detail_box_name_value, box_name)
        self.sleep(1)

        log.info("选择盒子的规格")
        self.clicks('css', hwgl_detail_box_size)
        self.sleep(0.5)
        log.info("点击下拉框")
        self.clicks('css', hwgl_detail_box_size_select)
        self.sleep(0.5)
        log.info("选择规格")
        self.clicks('xpath', hwgl_detail_box_size_value)
        self.sleep(1)
        self.clicks('css', other_position)

        # 这里调用自定义截图方法

        self.clicks('xpath', hwgl_detail_box_add_confirm)
        Screenshot(self.driver).get_img("盒位管理，点击新增样本盒，录入样本盒信息后点击保存","新增样本盒成功")
        self.wait_loading()
        self.sleep(2)  # 等会一会，防止数据库还没写入，就去执行查询SQL了

        log.info("开始查询数据库，校验新建的盒子信息")
        sqldata = 'SELECT  "box_id",  "box_name",  "box_type",  "storage_id",  "position_in_drawer",  "box_specification" FROM "lims"."sample_box_info_t" WHERE box_name =' + "'" + box_name + "'"

        ret = executeSql.test_select_limsdb(sqldata)
        return ret


if __name__ == '__main__':
    test = SampleHwgl(BasePage)
    test.hwgl_list_add(1, '1126样本盒')
