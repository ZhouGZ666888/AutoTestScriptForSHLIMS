# -*- coding: utf-8 -*-
# @Time    : 2022/02/08
# @Author  : guanzhong.zhou
# @File    : 数据修改模块页面功能封装


import yaml
from common.all_path import sampledata_path
from common.editYaml import read_yaml
from common.screenshot import Screenshot
from PageElemens.DataEdit_sjxg_ele import *
from uitestframework.basepageTools import BasePage
from common.logs import log


class DataChangePage(BasePage):
    """
    数据修改页面方法封装
    """

    # 打开指定页面
    def enter_function_page(self, url):
        """进入指定url页面"""
        js = 'window.open("{}");'
        self.executeJscript(js.format(url))
        self.wait_loading()

    # 查询数据修改模块任务单信息
    def search_task(self):
        """
        查询数据修改模块任务单信息
        :returns search_task_status,search_task_id
        """
        urldata = read_yaml(sampledata_path)
        task_id = urldata["datachange_extraction_taskId"]
        application_num = urldata["application_num"]

        log.info('临时文件取出存入的提取任务单号{}'.format(task_id))

        log.info('点击查询按钮')
        self.clicks('css', search_btn)
        self.sleep(0.5)

        log.info("搜索条件录入来源任务单号")
        self.input('css', srcTaskId, task_id)

        self.clicks('css', comfirm_btn)
        self.wait_loading()
        self.sleep(0.5)
        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("在搜索框中，根据任务单号进行搜索","搜索结果为该任务单下对应任务")

        log.info("获取查询结果，任务单号及任务单状态")
        search_task_id = self.get_text('css', first_task_id)
        search_task_status = self.get_text('css', first_task_status)
        # 返回单状态和任务单号
        return search_task_status, search_task_id,application_num

    def edit_task(self):
        """数据修改审核操作"""
        log.info("通过待办任务页面，进入数据修改待办tab页")
        if self.isElementExists('css', datachange_tab):
            self.clicks('css', datachange_tab)

        log.info("进入数据修改待办tab页,点击进入按钮")
        self.clicks('css', enter_datachange)
        self.sleep(0.5)

        log.info("待办页面进入数据修改页面，弹出新页面，切换至新页面，并关闭旧页面")
        now_handle = self.get_current_window_handle()
        all_handles = self.get_all_windows()
        for handle in all_handles:
            if handle != now_handle:
                # 切换到新窗口句柄，即新打开的页面
                self.close()
                self.switch_to_window(handle)
                self.wait_loading()
        self.sleep(0.5)

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("点击待办任务页面，进入数据修改审核页面","进入数据修改待审核页")

        log.info('点击审核')
        self.clicks('css', complete_edit)
        self.wait_loading()
        self.sleep(0.5)

        log.info('获取审核后的申请单号和状态')
        application_num = self.get_text('css', application_number)
        application_status = self.get_text('css', task_status)

        log.info('将获取的申请单号写入临时文件')
        application_num = application_num[5:].strip()
        urldata = read_yaml(sampledata_path)
        urldata["application_num"] = application_num
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)
        print("写入后的临时文件内容：", urldata)

        return application_status[3:].strip()

    # 核酸提取明细表数据修改操作
    def extraction_detail_datachange(self):
        """
        核酸提取明细表数据修改操作
        """
        # 将提取明细表任务单号写入临时文件
        taskstatus = self.get_text('css', detail_task_id)
        task_id = taskstatus[5:].strip()
        print(task_id)
        urldata = read_yaml(sampledata_path)
        urldata["extraction_taskId"] = task_id
        with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
            yaml.safe_dump(urldata, fs, allow_unicode=True)

        log.info('点击数据修改按钮')
        self.clicks('css', datachange)
        self.sleep(0.5)

        log.info('选择要修改的样本数据，点击发起修改')
        self.clicks('css', first_sample)  # 核酸提取明细表，数据列表第一条样本
        self.sleep(0.5)
        self.clicks('css', startChange)  # 数据修改-发起修改按钮
        self.wait_loading()

        # 这里调用自定义截图方法
        Screenshot(self.driver).get_img("选择数据后点击发起审核按钮","弹出进行审核确认弹框")

        log.info('发起修改弹框，指定审核人下拉框')
        self.click_by_js('css', placeHolder_select_btn)

        log.info('发起修改弹框，选择审核人：董国奇')
        self.clicks('xpath', choice_placeHolder.format('董国奇'))

        log.info('发起修改弹框，录入修改原因')
        self.input('css', dataChangeReason_reason, '测试-数据修改')

        log.info('发起修改弹框，点击下一步按钮')
        self.clicks('css', next_step)
        self.sleep(0.5)

        log.info('数据修改弹框，点击全选按钮')
        self.clicks('css', all_choice)

        log.info('数据修改弹框，点击批量实测数据')
        self.clicks('css', batchData_btn)
        self.sleep(0.5)

        log.info('数据修改弹框-批量实测数据弹框，录入修改后的样本进入量')
        self.input('css', usedTotalAmt, 6)

        log.info('数据修改弹框-批量实测数据弹框，选择包装单位')
        self.clicks('css', samplePkgAmtUnit)
        self.sleep(0.5)
        self.clicks('xpath', samplePkgAmtUnit_choice)
        self.sleep(0.5)
        self.clicks('css', batchData_comfirm)
        self.sleep(0.5)

        log.info('数据修改弹框-完成&提交申请')
        self.clicks('xpath', complete_submit_btn)
        self.wait_loading()


    def batch_submit_for_review(self):
        """
        切换登录用户进行审核
        """
        log.info('点击页面退出登录按钮，切换登录用户')
        self.click_by_js('css', logout_btn)
        self.sleep(1)
        self.click_by_js('xpath', logout_choice)
        self.sleep(1)
