# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
from PageElemens.sop_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class SopPage(BasePage):
    """
    列表页，详情页的动作封装
    """

    def search_task(self):
        """
        列表页检索指定条件的sop主数据
        """
        log.info("点击sop列表的搜索按钮")
        self.clicks('css', sop_list_search_butten)
        self.sleep(0.5)

        log.info("弹框中，选择提取任务类型的sop条件：这里指定提取的sop主数据")
        self.clicks('xpath', sop_list_search_module_type)
        self.sleep(1)
        self.clicks('xpath', sop_list_search_module)
        self.sleep(1)
        self.clicks('xpath', sop_list_search_module_comfirm)
        self.wait_loading()
        log.info("sop主数据搜索提取类型数据成功，数据展示正确")
        self.clicks('xpath', sop_list_search_show_obsolete_sop)
        log.info("勾选展示已失效的按钮，数据展示正确")
        self.wait_loading()

    def creat_sop(self, sop_name, module_value, type_value):
        """
        新建sop主数据，填写详情页信息，最后确认生效
        """
        log.info("点击sop列表的新建按钮")
        self.clicks('xpath', sop_list_creat_butten)
        self.wait_loading()

        log.info("详情页，填写sop名称")
        self.clicks('xpath', sop_detail_sopname)
        self.input('xpath', sop_detail_sopname, sop_name)
        self.sleep(1)
        log.info("详情页，填写sop版本号")
        self.clicks('xpath', sop_detail_sopname_version)
        self.input('xpath', sop_detail_sopname_version, '1.1.0')
        self.sleep(1)

        log.info("详情页，填写核对人信息")
        self.clicks('xpath', sop_detail_sopname_people)
        self.sleep(1)
        self.clicks('xpath', sop_detail_sopname_people_value)
        self.sleep(1)
        self.input('xpath', sop_detail_sopname_people_value, '甄鑫')
        self.sleep(1)
        self.clicks('xpath', sop_detail_sopname_search_button)
        self.sleep(1)
        self.clicks('xpath', sop_detail_sopname_search_value)
        self.sleep(1)
        self.clicks('xpath', sop_detail_sopname_confirm_button)
        self.sleep(1)

        log.info("详情页，填写sop编码")
        self.clicks('xpath', sop_detail_sopname_code)
        self.input('xpath', sop_detail_sopname_code, 'DF03')
        self.sleep(1)
        log.info("详情页，选择sop所属模块")
        self.clicks('xpath', sop_detail_sopname_module)
        self.sleep(2)
        print(str(sop_detail_sopname_module_value.format(str(module_value))))
        self.clicks('xpath', sop_detail_sopname_module_value.format(str(module_value)))

        self.sleep(1)

        log.info("详情页，选择操作方式")
        self.clicks('xpath', sop_detail_work_type)
        self.sleep(1)
        self.clicks('xpath', sop_detail_work_type_value)
        self.sleep(1)

        log.info("详情页，选择sop所属模块对应的任务类型")
        self.clicks('xpath', sop_detail_sopname_type)
        self.sleep(1)
        self.clicks('xpath', sop_detail_sopname_type_value.format(str(type_value)))
        self.sleep(1)
        log.info("详情页，填写sop描述")
        self.clicks('xpath', sop_detail_sopname_decription)
        self.input('xpath', sop_detail_sopname_decription, '国旗测试')
        self.sleep(1)
        # log.info("详情页，填写sop文件编号")
        # self.clicks('xpath', sop_detail_sopname_fileNo)
        # self.input('xpath',sop_detail_sopname_fileNo,'NJ20211020')
        # self.sleep(1)
        # log.info("详情页，填写sop文件名称")
        # self.clicks('xpath', sop_detail_sopname_filename)
        # self.input('xpath',sop_detail_sopname_filename,'NJ20211020.pdf')
        # self.sleep(1)
        log.info("详情页，点击保存sop基础数据")
        self.clicks('xpath', sop_detail_save_butten)
        self.sleep(1)
        self.wait_loading()

        log.info("详情页，点击【新增产物类型】按钮")
        self.click_by_js('xpath', sop_detail_product)
        self.sleep(2)
        log.info("详情页，点击【新增产物类型】按钮后，点击搜索原始样本类型弹框")
        self.clicks('css', sop_detail_original_sample_type)
        self.sleep(2)

        log.info("详情页，默认选择首选项")
        self.click_by_js('css', sop_detail_original_sample_type_search_result)
        self.sleep(1)

        log.info("详情页，点击确定")
        self.clicks('xpath', sop_detail_original_sample_type_search_comfirm)
        self.sleep(1)

        log.info("详情页，点击【新增产物类型】按钮后，点击搜索产物样本类型弹框")
        self.clicks('css', sop_detail_product_sample_type)
        self.sleep(2)

        log.info("详情页，默认选择首选项")
        self.clicks('css', sop_detail_product_sample_type_search_result)
        self.sleep(2)
        log.info("详情页，点击确定")
        self.clicks('xpath', sop_detail_product_sample_type_search_comfirm)
        self.sleep(1)

        log.info("详情页，点击新增步骤按钮，输入步骤编号")
        self.clicks('xpath', sop_detail_add_step)
        self.sleep(1)
        # log.info("输入编号")
        # self.input('css', sop_detail_step_num,'1')
        # self.sleep(1)
        log.info("详情页，点击同步编号按钮")
        self.clicks('xpath', sop_detail_add_restep)
        self.sleep(2)

        log.info("详情页，使用JS让页面滑动到最顶端，点击sop生效按钮")
        self.executeJscript(scroll_view)
        self.sleep(1)
        self.clicks('xpath', sop_effect_button)
        self.sleep(1)
        log.info("详情页，sop生效成功")
        self.clicks('xpath', sop_effect_button_confirm)
        self.sleep(2)

        log.info("详情页，点击返回列表页，开始新的sop新建任务")
        self.clicks('xpath', sop_go_back_list_button)
        self.sleep(1)
        self.clicks('xpath', sop_go_back_list_button_confirm)
        self.wait_loading()
        self.sleep(1)
