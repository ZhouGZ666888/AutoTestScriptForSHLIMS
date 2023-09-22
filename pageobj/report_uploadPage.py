# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : guanzhong.zhou
# @File    : 报告上传模块页面方法封装

from datetime import datetime
import openpyxl
from PageElemens.report_upload_ele import *
from common.editYaml import *
from common.all_path import  sampledata_path, mutation_file_path, excel_doc_file_path, \
    orderNub_path
from common.screenshot import Screenshot
from uitestframework.basepageTools import BasePage
from common.logs import log
import pandas as pd


def create_upload_path():

    order_nub  = read_yaml(orderNub_path)  # 读取订单号信息
    file_name = "报告上传文件" + str(order_nub['name']) + "_" + str(order_nub['order_number'])  # 新建Excel文件，以读取的患者姓名和订单号为文件名
    return file_name


class ReportUploadPage(BasePage):
    """
    报告-基本信息任务分配模块页面基础方法封装
    """

    def search_by_poolingdate(self):
        """
        根据预计实验日期查询
        :return: 返回查询结果数量
        """
        log.info("根据预计实验日期查询")
        str_time = datetime.now().strftime('%Y.%m.%d')  # 获取当前时间
        # str_time = "2023.02.10"  # 获取当前时间

        print('预计上机日期', str_time)
        self.input('xpath', poolingDate, str_time)  # 调用搜索方法
        self.sleep(0.5)
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', all_orders):
            allorder = self.findelements('xpath', all_orders)  # 获取查询结果数量
            self.clicks('css', reset_btn)  # 重置查询条件
            return len(allorder)
        else:
            return 0

    def search_by_assignmentDate(self):
        """
        根据报告分配日期查询
        :return: 返回查询结果数量
        """
        log.info("根据报告分配日期查询")
        str_time = datetime.now().strftime('%Y.%m.%d')  # 获取当前时间
        # str_time = "2023.02.10"  # 获取当前时间

        self.input('css', lastPoolingDate, str_time)  # 调用搜索方法
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', all_orders):
            allorder = self.findelements('xpath', all_orders)  # 获取查询结果数量
            self.clicks('css', reset_btn)  # 重置查询条件
            return len(allorder)
        else:
            return 0

    def search_by_order(self):
        """
        按订单号搜索
        :return:返回查询出的订单信息数量
        """

        order = read_yaml(orderNub_path)
        log.info("按订单号搜索:%s"%order['order_number'])
        self.input('css', order_num, order['order_number'])
        self.click_by_js('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', all_orders):
            allorder = self.findelements('xpath', all_orders)  # 获取查询结果数量
            return len(allorder)
        else:
            return 0

    def select_report_belong(self):
        """
        报告归属下拉选择
        """
        # 先按照订单号搜索任务
        self.search_by_order()
        log.info('报告归属下拉选择“世和')
        self.search_by_order()
        self.clicks('css', report_belong)
        self.sleep(0.5)
        self.clicks('css', report_belong_input)
        self.sleep(0.5)
        self.clicks('xpath', report_belong_choice)
        self.sleep(1)
        self.wait_loading()

    def choice_rehearing_person(self):
        """
        选择复审人
        :return:返回页面提示信息
        """
        log.info("选择复审人")

        self.executeJscript(
            'document.getElementsByClassName("vxe-table--body-wrapper")[0].scrollLeft=1250')
        self.sleep(0.5)
        self.clicks('xpath', rehearing_person)  # 复审人表单定位
        self.sleep(0.5)
        self.clicks('css', rehearing_person_input)
        self.input('css', rehearing_person_input, '周官钟')  # 复审人弹框文本录入
        self.sleep(1)
        self.clicks('xpath', rehearing_person_choice.format('周官钟'))  # 复审人弹框文本录入后选择
        self.clicks('css', rehearing_person_comfirm)
        pageinfo = self.get_save_info()  # 获取页面提示信息
        self.sleep(3)
        return pageinfo

    def upload_report_file(self):
        """
        上传报告文件
        """
        log.info("上传报告文件")
        self.clicks('xpath', report_file_btn)  # 点击报告文件编辑按钮
        self.sleep(1)
        # 上传报告文件
        # 执行JS，修改上传控件样式，由不显示变为显示，以便上传文件
        self.executeJscript(
            "document.querySelector('.card-report-file .el-upload input').style.setProperty('display','block','important');")

        # 上传报告文件需要包含患者姓名和订单号，分别取出保存为文件名
        file_name = create_upload_path()
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'test_sheet1'
        ws.cell(row=1, column=2).value = 1

        wb.save(excel_doc_file_path + '/' + '{}.xlsx'.format(file_name))  # 保存文件

        report_file_path = os.path.abspath(excel_doc_file_path + '/' + '{}.xlsx'.format(file_name))
        self.input('css', report_upload_btn, report_file_path)  # 用send_keys方法上传文件
        report_info = self.get_save_info()
        Screenshot(self.driver).get_img("报告上传弹框，点击上传报告文件，上传报告文件","上传报告文件成功")
        self.sleep(1)
        return report_info

    def upload_read_file(self):
        # 上传解读文件
        log.info("上传解读文件")
        file_name = create_upload_path()
        self.executeJscript(
            "document.querySelector('.card-decode-file .el-upload input').style.setProperty('display','block','important');")
        # 创建TXT类型的解读文件
        with open(excel_doc_file_path + '/' + '{}_解读文件.txt'.format(file_name), 'w', encoding='utf-8') as f:
            f.write('自动化测试解读文件上传')
        decode_file_path = os.path.abspath(excel_doc_file_path + '/' + '{}_解读文件.txt'.format(file_name))
        self.input('css', decode_upload_btn, decode_file_path)  # 用send_keys方法上传文件
        decode_info = self.get_save_info()
        Screenshot(self.driver).get_img("报告上传弹框，点击上传解读文件，上传解读文件","上传解读文件成功")
        self.sleep(1)
        return decode_info
        # 这里调用自定义截图方法

    def upload_other_file(self):
        """上传其他文件"""
        log.info("上传其他文件")
        self.executeJscript(
            "document.querySelector('.card-other-file .el-upload input').style.setProperty('display','block','important');")
        # 创建doc类型的其他文件
        with open(excel_doc_file_path + '/' + '自动化测试其他文件上传.doc', 'w', encoding='utf-8') as f:
            f.write('自动化测试解读文件上传')
        other_file_path = os.path.abspath(excel_doc_file_path + '/' + '自动化测试其他文件上传.doc')
        self.input('css', other_upload_btn, other_file_path)  # 用send_keys方法上传文件

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告上传弹框，点击上传其他文件，上传其他文件","上传其他文件成功")
        self.sleep(1)

        self.clicks('css', report_upload_comfirm)  # 上传文件弹框确认按钮
        self.wait_loading()
        self.sleep(1)

    def update_mutation_file(self):
        """
        突变文件上传
        """
        log.info("突变文件上传")
        self.clicks('xpath', mutation_file_btn)  # 突变文件编辑表单定位
        self.wait_loading()

        self.executeJscript(
            "document.querySelector('.dialog-mutation-file .el-upload input').style.setProperty('display','block','important');")

        # 用send_keys方法上传文件
        # 读取基本信息处理模块存储的实验室号
        testdata = read_yaml(sampledata_path)
        df = pd.read_csv(mutation_file_path, encoding='utf-8')
        df.loc[:, 'id'] = testdata['bioinformatic_negative_lab_num']  # 把读取的实验室号写入到突变模板中
        df.to_csv(mutation_file_path, index=False, encoding='utf-8')

        self.input('css', mutation_file_upload_btn, mutation_file_path)

        # 这里调用自定义截图方法

        self.sleep(1)
        mutation_file_info = self.get_save_info()
        Screenshot(self.driver).get_img("点击上传突变文件按钮，上传突变文件，上传突变文件","上传突变文件成功")
        self.clicks('css', mutation_file_upload_comfirm)
        self.sleep(1)
        print("突变文件上传", mutation_file_info)
        return mutation_file_info

    def complete_report_task(self):
        """
        完成报告任务
        """
        log.info("完成报告任务")
        self.clicks('css', complete_task)
        self.wait_loading()
        self.sleep(1)
        pageinfo = self.get_text('css', complete_task)
        return pageinfo

    def get_save_info(self):
        """
        获取数据操作后，页面给出的提示信息语
        Submit successfully
        review successfully
        """
        log.info('获取页面提示信息')
        if self.isElementExists('xpath', page_info):
            return self.get_text('xpath', page_info)
        else:
            return None
if __name__ == '__main__':
    s=create_upload_path()
    print(s)