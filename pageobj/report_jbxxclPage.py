# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : guanzhong.zhou
# @File    : 报告-基本信息处理模块页面方法封装
from datetime import datetime
from PageElemens.report_jbxxcl_ele import *
from common.DataBaseConfig import executeSql
from common.editYaml import *
from common.all_path import sampledata_path, orderNub_path
from common.screenshot import Screenshot
from data.sql_action.execute_sql_action import ybcl_detail_sql2
from uitestframework.basepageTools import BasePage
from common.logs import log


class ReportBasicInfoProcessingPage(BasePage):
    """
    报告-基本信息任务分配模块页面基础方法封装
    """

    def serach_data(self, ele, value):
        """
        :param ele: 元素定位
        :param value: 搜索条件
        """

        self.input('css', ele, value)  # 定位文本框输入值
        self.sleep(0.5)
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()

    def search_by_project(self):
        """
        按项目号搜索
        :return:返回查询出的订单信息数量
        """
        log.info("按项目号搜索")
        self.clicks('css', project_num)  # 点击项目号搜索项
        self.sleep(0.5)
        self.clicks('xpath', project_num_chioce)  # 点击选中下拉条件
        self.sleep(0.5)
        self.clicks('css', search_btn)  # 点击查询
        self.wait_loading()
        if self.isElementExists('xpath', all_orders):
            allorder = self.findelements('xpath', all_orders)  # 获取查询结果数量
            self.clicks('css', reset_btn)  # 重置查询条件
            return len(allorder)
        else:
            return 0

    def search_by_date(self):
        """
        按预计实验日期查询
        :return: 返回查询出的订单信息数量
        """
        log.info("按预计实验日期查询")
        str_time = datetime.now().strftime('%Y.%m.%d')  # 获取当前时间
        # str_time = '2023.02.10'  # 获取当前时间

        print('预计上机日期')
        self.serach_data(poolingDate, str_time)  # 调用搜索方法
        self.sleep(0.5)
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
        log.info("按订单号搜索")

        order = read_yaml(orderNub_path)  # 订单Excel获取订单号
        print('订单Excel获取订单号', order['order_number'])
        self.serach_data(order_num, order['order_number'])  # 调用搜索方法
        if self.isElementExists('xpath', all_orders):
            allorder = self.findelements('xpath', all_orders)  # 获取查询结果数量
            return len(allorder)
        else:
            return 0

    def edit_sample_info(self):
        """
        批量选择产品、录入写入报告的不上机样本和写入报告的上机样本
        """
        log.info("批量选择产品、录入写入报告的不上机样本和写入报告的上机样本")
        # 选择产品
        lens = self.search_by_order()  # 调用按订单号搜索方法
        print(lens)
        self.sleep(0.5)
        self.click_by_js('css', add_report_task)  # 添加报告任务
        self.wait_loading()
        self.clicks('css', report_project)  # 报告任务项-【产品】表单定位
        self.clicks('css', report_project_btn)  # 报告任务项-【产品】表单下拉按钮
        self.clicks('xpath', report_project_choice)  # 报告任务项-【产品】表单下拉选择世和一号
        self.wait_loading()

        # 录入写入报告的上机样本
        log.info("录入写入报告的上机样本")
        self.report_sample(report_on_board_sample, report_on_board_sample_lab_num, 'PB')

        # 录入写入报告的不上机样本
        log.info("录入写入报告的不上机样本")
        self.report_sample(report_no_board_sample, report_no_board_sample_lab_num, 'BC')

    def bioinformatic_negative(self):
        """
        选择生信阴性对照
        """
        log.info("选择生信阴性对照")
        # 报告任务项-【选择生信阴信对照】表单定位
        self.click_by_js('css', choice_bioinformatic_negative)
        self.wait_loading()

        # 获取一条写入报告的上机样本的实验室号
        bioinformatic_negative = self.get_text('css', choice_bioinformatic_negative_lab_num)
        print('获取一条写入报告的上机样本的实验室号', bioinformatic_negative)
        datas = read_yaml(sampledata_path)
        datas["bioinformatic_negative_lab_num"] = bioinformatic_negative
        save_yaml(sampledata_path,datas)
        print("写入后的数据", datas)

        # 报告任务项-【选择生信阴信对照】弹框样本列表，勾选右侧样本第一条
        self.clicks('css', choice_bioinformatic_negative_sample)
        self.sleep(0.5)
        # 报告任务项-【选择生信阴信对照】弹框点击添加按钮
        self.clicks('css', choice_bioinformatic_negative_comfirm)
        self.wait_loading()

    def choice_report_style(self):
        """
        选择报告形式
        """
        lens = self.search_by_order()  # 调用按订单号搜索方法
        print(lens)
        self.sleep(0.5)
        self.click_by_js('css', add_report_task)  # 添加报告任务
        self.wait_loading()
        log.info("选择报告形式")
        self.clicks('css', report_style)  # 报告任务项-【报告形式】表单定位
        self.clicks('css', report_style_select)  # 报告任务项-【报告形式】表单下拉
        self.clicks('xpath', report_style_choice)  # 报告任务项-【报告形式】表单下拉选项
        self.sleep(1)

    def choice_report_belongTo(self):
        """
        选择报告归属
        """
        log.info("选择报告归属")
        self.clicks('css', report_belongTo)  # 报告任务项-【报告归属】表单定位
        self.clicks('css', report_belongTo_select)  # 报告任务项-【报告归属】表单下拉
        self.clicks('xpath', report_belongTo_choice)  # 报告任务项-【报告归属】表单下拉选项
        self.sleep(1)

    def choice_report_TemplateName(self):
        """
        选择报告模板
        """
        log.info("选择报告模板")
        self.clicks('css', report_TemplateName)  # 报告任务项-【报告模板】表单定位
        self.input('css', report_TemplateName_input, '世和')  # 报告任务项-【报告模板】弹框，搜索文本录入框
        self.clicks('css', report_TemplateName_search_btn)  # 报告任务项-【报告模板】弹框,搜索按钮
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("报告基本信息处理页面，勾选报告任务，点击报告模版弹框，选择报告模板","选择报告模版成功")

        self.clicks('css', report_TemplateName_choice)  # 报告任务项-【报告模板】弹框搜索结果选择，第一条
        self.clicks('css', report_TemplateName_search_comfirm)  # 报告任务项-【报告模板】弹框,确认按钮
        self.wait_loading()
        self.sleep(1)

    def update_medical(self):
        """
        点击修改病历，打开并进入病历修改页面，获取页面title
        :return: 返回病例页面title
        """
        page_title = None
        log.info("点击修改病历，打开并进入病历修改页面，获取页面title")
        now_handle = self.get_current_window_handle()  # 获取当前页面句柄
        self.clicks('css', editMedical_btn)  # 点击进入修改病历页面
        self.wait_loading()

        all_handles = self.get_all_windows()  # 获取所有句柄
        for handle in all_handles:  # 判断非当前句柄
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的病历页面
                self.switch_to_window(handle)
                self.sleep(1)
                page_title = self.get_text('css', editMedical_title)  # 获取病例页面title
                self.close()
        self.sleep(1)
        # 切换到旧窗口句柄，回到原页面
        self.switch_to_window(now_handle)
        self.sleep(1)

        return page_title

    def click_to_view(self):
        """
        点击并查看样本信息
        :return:返回样本数量
        """
        log.info("点击并查看样本信息")
        self.clicks('xpath', click_view)
        self.wait_loading()
        sapmles_num = self.findelements('xpath', sample_info)
        self.clicks('css', click_view_comfirm)
        self.sleep(0.5)
        return len(sapmles_num)

    def report_sample2(self, ele, lab_num, sample_type):
        """
        写入报告的上机样本和写入报告的不上机样本方法封装（内部血浆）
        """
        log.info("写入报告的上机样本和写入报告的不上机样本方法封装")
        self.click_by_js('css', ele)  # 报告任务项-【写入报告的上机样本】表单定位
        self.wait_loading()

        log.info("数据库取出样本处理结果表中的样本号和实验室号")
        # 读取存在临时文件中的样本处理结果表任务单号
        taskID_nub = read_yaml(sampledata_path)
        sql_data = self.select_sql(ybcl_detail_sql2.format(taskID_nub['sampleprocessing_reportprocess_taskid']))
        laboratory_list = [(i['sample_main_lab_code']) for i in sql_data]
        print(laboratory_list)

        # 先判断第一条是否符合要求，第一条后就要开始滚动下拉进行判断了
        laboratorys = self.get_text('css', lab_num.format(1))  # 获取写入报告的上机样本弹框第一行样本原始样本号信息
        print("获取的页面原始样本号", laboratorys)
        # 判断样本号是否符合需要的要求，且实验室号和原始样本号一致
        if laboratorys[:2] == sample_type and laboratorys in laboratory_list:
            self.clicks('css', lab_num.format(1))  # 判断为true则选中

        laboratorys = self.get_text('css', lab_num.format(2))  # 获取写入报告的上机样本弹框第二行样本原始样本号信息
        print("获取的页面原始样本号", laboratorys)
        if laboratorys[:2] == sample_type and laboratorys in laboratory_list:  # 判断样本号是否符合需要的要求，且实验室号和原始样本号一致
            self.clicks('css', lab_num.format(2))  # 判断为true则选中

        self.executeJscript(
            'document.querySelector(".dialog-report-sample .vxe-table--main-wrapper .vxe-table--body-wrapper.body--wrapper").scrollTop=100')

        # 下面为滚动下拉进行判断
        nubs = 3
        scoll = True
        last_lab = None
        try:
            while scoll:
                # 因为弹框每次只显示11条数据，所以需要一边滑动下拉，一边进行数据判定；第一次下拉100xp后，后面每次下拉50xp，把每行都排在第二行的位置上
                laboratorys = self.get_text('css', lab_num.format(2))
                self.sleep(0.5)
                # 判断是否符合条件（内部血浆）
                if laboratorys != last_lab:  # 判定当前取值是否与上次一样，以此来判断是否下拉到底
                    if laboratorys[:2] == sample_type and laboratorys in laboratory_list:
                        print("获取的页面原始样本号", laboratorys)
                        self.click_by_js('css', lab_num.format(2))
                        self.sleep(0.5)
                else:
                    # 判断下拉是否到底，到底则按照下标开始取数判定
                    for i in range(1, 10):
                        laboratorys = self.get_text('css', lab_num.format(i + 2))
                        if laboratorys[:2] == sample_type and laboratorys in laboratory_list:
                            print('最后，来了，点它')
                            self.clicks('css', lab_num.format(i + 2))
                            self.sleep(0.5)
                    scoll = False

                self.executeJscript(
                    'document.querySelector(".dialog-report-sample .vxe-table--main-wrapper .vxe-table--body-wrapper.body--wrapper").scrollTop=50*{}'.format(
                        nubs))
                nubs += 1
                last_lab = laboratorys
                print("上一个原始样本号", last_lab)
        except  Exception as s:
            print(s)
        self.clicks('css', report_on_board_sample_comfirm)
        self.wait_loading()

    def report_sample(self, ele, lab_num, sample_type):
        """
        写入报告的上机样本和写入报告的不上机样本方法封装（内部血浆）
        """
        log.info("写入报告的上机样本和写入报告的不上机样本方法封装")
        self.click_by_js('css', ele)  # 报告任务项-【写入报告的上机样本】表单定位
        self.wait_loading()

        log.info("数据库取出样本处理结果表中的样本号和实验室号")
        # 读取存在临时文件中的样本处理结果表任务单号
        taskID_nub = read_yaml(sampledata_path)
        sql_data = executeSql.test_select_limsdb(ybcl_detail_sql2.format(taskID_nub['sampleprocessing_reportprocess_taskid']))
        laboratory_list = [(i['sample_main_lab_code']) for i in sql_data]
        print(laboratory_list)

        # 下面为滚动下拉进行判断
        used_list = []
        nubs = 1
        scoll = True
        try:
            while scoll:
                for i in range(0, 11):
                    # 每页展示11条数据，每条数据为50个像素，每次下拉11条数据的像素，即11*50个像素；再下拉11条数据后，在页面上从第1条开始读数
                    laboratorys = self.get_text('css', lab_num.format(i + 1))
                    print(laboratorys)
                    self.sleep(0.5)
                    # 判断是否符合条件（内部血浆）
                    if laboratorys[:2] == sample_type  and laboratorys not in used_list and any(laboratorys.strip()[:10] in ele for ele in laboratory_list):  #
                        # 判定当前取值是否与上次一样，以此来判断是否下拉到底
                        print('发现样本，%s' % laboratorys)
                        self.click_by_js('css', lab_num.format(i + 1))
                        self.sleep(0.5)
                        used_list.append(laboratorys)
                        scoll = False
                        break
                    elif laboratorys in used_list:  # 到底页后，判断是数据否已加入列表
                        scoll = False

                self.executeJscript(
                    'document.querySelector(".dialog-report-sample .vxe-table--main-wrapper .vxe-table--body-wrapper.body--wrapper").scrollTop=50+550*{}'.format(
                        nubs))
                nubs += 1
        except  Exception as s:
            print(s)
        self.clicks('css', report_on_board_sample_comfirm)
        self.wait_loading()
