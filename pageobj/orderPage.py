# -*- coding: utf-8 -*-
# @Time    : 2021/11/01
# @Author  : guanzhong.zhou
# @File    : 订单模块页面功能封装
from PageElemens.orderlist_ele import *
from common.editYaml import *
from common.all_path import  orderNub_path
from common.screenshot import Screenshot
from data.execute_sql_action import order_isexists_sql
from uitestframework.basepageTools import BasePage
from common.logs import log


class OrderPage(BasePage):
    """
    订单页面基础功能封装
    """

    def check_order_isExists(self, order):
        """
        新建订单前，先到数据库查询是否已存在相同订单号，若存在则返回递归方法，将订单号+1再次验证
        :param order: Excel读取的订单号
        :return: 返回验证后数据库不存在的订单号
        """
        # 数据库获取订单号，判断查询结果是否有值
        result = self.select_sql(order_isexists_sql.format(order))
        result1 = [dct[item] for dct in result for item in dct]
        # 查询订单号数为0，则说明该订单号不在数据库，则可用，返回该号
        if result1[0] == 0:
            return order
        # 订单号不为0，说明数据库已有该订单号，订单号不可用，在原订单号基础上+1后，传给方法，再次递归验证
        elif result1[0] != 0:
            print('订单已存在！')
            new_order = str(int(order) + 1)
            return self.check_order_isExists(new_order)

    def add_order(self):
        """新建订单,录入订单号和参检人姓名"""
        log.info('新增订单，录入订单号、患者姓名')
        self.click_by_js("class_name", add_orders)
        self.sleep(0.5)
        # 判断是否存在存储订单号的yaml文件，如果不存在则新建yaml文件，并把新的订单号存入，如果存在，则取里面的已有订单号，并+1，作为新的订单号
        order = read_yaml(orderNub_path)

        try:
            if  'order_number' not in order:
                first_order_num = '92090001'
                # 验证订单号是否可用
                order_nub = self.check_order_isExists(first_order_num)
                print('新建的订单号', order_nub)

                self.input('css', order_num_input, order_nub)
                self.sleep(0.5)
                self.input('css', patient_name_input, '张三')
                self.sleep(0.5)

                # 调用自定义截图方法
                Screenshot(self.driver).get_img("新建订单")

                self.clicks('css', add_confirm)
                self.wait_loading()

                # 把订单号和患者姓名写入Excel
                dic1 = {'order_number': order_nub,
                        'patient_name': '张三'
                        }
                save_yaml(orderNub_path, dic1)  # 订单号写入临时文件

            else:
                old_ordernum = order['order_number']
                # 验证订单号是否可用
                new_ordernum = self.check_order_isExists(str(int(old_ordernum) + 1))

                self.input('css', order_num_input, new_ordernum)
                self.sleep(0.5)
                self.input('css', patient_name_input, str(order['name']).strip())
                self.sleep(0.5)

                # 调用自定义截图方法
                Screenshot(self.driver).get_img("新建订单")
                self.clicks('css', add_confirm)
                self.wait_loading()
                log.info("将新订单号写入文件")
                order['order_number']=str(new_ordernum)
                save_yaml(orderNub_path, order)  # 订单号写入临时文件
                self.sleep(1)
        except Exception as e:
            print(e)

    def enter_edit(self):
        """搜索出新建订单，选中并编辑"""
        self.click_by_js('css', search_order)
        orderInfo = read_yaml(orderNub_path)
        self.input('css', search_order_input, orderInfo['order_number'])
        self.clicks('css', search_order_comfirm)
        self.wait_loading()

        self.click_by_js('css', first_order)
        self.sleep(0.2)
        self.clicks('css', edit_order)
        self.wait_loading()


    def bl_dd_associate(self):
        """进行病历关联，不进行主订单的选择"""
        order = read_yaml(orderNub_path)
        log.info('选择癌种')
        self.clicks('css', cancer_type_chioce)
        self.sleep(0.2)
        self.clicks('css', cancer_type)
        self.sleep(1)
        log.info('进入关联病历弹框')
        self.clicks('css', ele_patient_number)
        self.wait_loading()
        self.sleep(0.5)
        self.input('css', identification_numb, str(order['identificationNo']).strip())
        self.input('css', patient_name, str(order['name']).strip())
        self.sleep(0.5)
        self.clicks('css', search_num_button)
        self.wait_loading()
        self.clicks('css', similar_case)  # 查询结果，选中第一条
        self.sleep(0.5)
        self.clicks('css', ele_chioce_confirm)
        result = self.findelement('xpath', '//*[text()="电子病历关联成功"]')
        self.wait_loading()
        return result

    def edit_order(self):
        """
         编辑订单信息
        """
        log.info('选择报告是否体现医院信息、是否寄送纸质版、录入报告接收人')
        self.clicks('css', is_hospital_info_displayed)
        self.sleep(0.2)
        self.clicks('xpath', hospital_info_displayed)
        self.sleep(0.2)

        self.clicks('css', formMedicalBaseInfo)
        self.sleep(0.5)
        self.clicks('xpath', formMedicalBaseInfoChoice)
        self.sleep(1)

        self.clicks('css', report_receiver_button)
        self.sleep(0.5)
        self.clicks('xpath', report_receiver)
        self.sleep(1)
        log.info('新增联系人信息,录入姓名、联系方式、地址')
        self.clicks('css', add_new_contact)
        self.sleep(0.5)
        self.clicks('css', contact_name)
        self.input('css', contact_name_inout, '测试人员')
        self.sleep(0.5)
        self.clicks('css', contact_tel_numb)
        self.input('css', contact_tel_numb_input, '15252415241')
        self.sleep(0.5)

        log.info('新增医生信息')
        self.clicks('css', chioce_physician)
        self.wait_loading()
        self.input('css', search_by_department, '肺')
        self.clicks('css', physician_search_button)
        self.wait_loading()
        self.clicks('css', chioce_department)
        self.sleep(1)
        self.clicks('css', chioce_physician_confirm)
        self.sleep(1)
        log.info('录入销售代表和款项信息')
        self.clicks('css', sales_information)
        self.input('css', sales_information, '董国奇')
        self.sleep(0.5)

        self.clicks('xpath', chioce_sale)
        self.sleep(0.5)
        self.clicks('css', payment_due)
        self.sleep(0.5)
        self.input('css', fee_after_amendment, '10000')
        self.sleep(0.5)
        self.input('css', amendment_reason, '无理由')
        self.sleep(0.5)
        self.clicks('css', change_fee_confirm)
        self.sleep(1)

    def save_add_order(self):
        """
        保存订单
        :return:获取保存成功提示信息
        """
        log.info('保存订单')
        self.click_by_js('css', save_button)
        result = self.findelement('xpath', '//*[text()="保存成功"]')
        self.wait_loading()
        return result

    def set_mian_order_number(self):
        """
        设置主订单号
        """
        log.info('设置主订单号')
        self.click_by_js('css', productPkgId)  # 点击所属套餐
        self.clicks('xpath', productPkgId_choice)  # 选择所属套餐
        self.sleep(1)
        self.input('css', pulseplanCount, 3)  # 输入动态监测次数
        self.sleep(0.5)
        self.clicks('css', main_order_number)  # 点击主项目
        self.wait_loading()
        if self.isElementExists('css', chioce_main_order_number):
            self.clicks('css', chioce_main_order_number)
            self.sleep(0.5)
            self.clicks('css', chioce_main_order_number_confirm)
        result = self.findelement('xpath', '//*[text()="订单关联成功"]')
        self.wait_loading()
        return result
