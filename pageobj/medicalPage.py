# -*- coding: utf-8 -*-
# @Time    : 2021/12/09
# @Author  : guanzhong.zhou
# @File    : 病历模块页面功能封装
from PageElemens.medical_ele import *
from common.all_path import identificationNo_file_path
from data.sql_action.execute_sql_action import bl_sql
from uitestframework.basepageTools import BasePage
import pandas as pd
from common.logs import log


class MedicalPage(BasePage):
    """
    病历页面基础功能封装
    """

    def search_medical(self):
        """
        点击搜索按钮方法
        """
        self.clicks('css', search_btn)
        self.sleep(0.5)

    def search_by_param(self, text):
        """
        按病历号搜索方法
        :param text: 病历号
        """
        self.input('css', search_medicalNum, text)

    def click_edit_btn(self):
        """
        点击编辑按钮方法
        """
        self.clicks('class_name', edit_btn)

    def click_search_btn(self):
        """
        点击搜索确认方法
        """
        self.clicks('class_name', search_sure_btn)

    def click_add_medical(self):
        """
        点击新增病历方法
        """
        self.clicks('css', add_btn)
        self.wait_loading()

    def input_patientinfo(self, name, identityNo):
        """
        病历中输入患者姓名,身份证信息方法
        :param name: 患者姓名
        :param identityNo: 身份证
        """
        self.input('css', Participants_name, name)
        self.sleep(0.5)
        self.input('css', identificationNo, identityNo)
        self.sleep(1)

    def get_sex(self, r_sex):
        """
        获取患者性别方法
        :return:
        """
        self.click_by_js('css', sex)
        if r_sex == '男':
            self.click_by_js('css', man_sex)
            self.sleep(0.5)
        elif r_sex == '女':
            self.click_by_js('css', woman_sex)
        self.sleep(0.5)

    def smoking_info(self, starttime='', endtime='', durtin='', remark=''):
        """
        录入吸烟史
        :param starttime:开始日期
        :param endtime: 结束日期
        :param durtin: 时长
        :param remark: 备注

        """
        log.info('开始录入吸烟史信息')

        self.sleep(1)
        self.clicks('class_name', smoking_his_add)
        self.sleep(1)
        self.clicks('css', startDateValue)

        self.sleep(1)
        self.input('css', startDateValue_input, starttime)
        log.info('吸烟史开始时间%s:' % starttime)
        self.sleep(1)
        self.clicks('css', endDateValue)
        self.sleep(1)
        self.input('css', endDateValue_input, endtime)
        log.info('吸烟史结束时间%s:' % endtime)
        self.sleep(1)
        self.clicks('css', durationr)
        self.sleep(1)
        self.input('css', durationr_input, durtin)
        log.info('吸烟史时长%s:' % durtin)
        self.sleep(1)
        self.clicks('css', remarks)
        self.sleep(1)
        self.input('css', remarks_input, remark)
        log.info('吸烟史备注%s:' % remark)

        # 选择吸烟频率
        self.sleep(0.5)
        self.clicks('css', smoking_selection)
        self.sleep(0.5)
        self.clicks('class_name', smoking_rates)
        self.sleep(0.5)
        self.clicks('css', rate_list)
        self.sleep(0.5)
        self.clicks('css', choice_rate_btn)
        self.sleep(0.5)

    def drink_info(self, starttime='', endtime='', durtin='', remark=''):
        """
        录入饮酒信息
        """
        log.info('开始录入饮酒史信息')

        self.sleep(0.5)
        self.clicks('class_name', drink_his_add)

        self.sleep(0.5)
        self.clicks('css', drink_starttime)
        self.input('css', drink_starttime_input, starttime)
        log.info('饮酒史开始时间%s:' % starttime)
        # print("输入开始时间{}".format(starttime))
        self.sleep(0.5)
        self.clicks('css', drink_endtime)
        self.sleep(0.5)
        self.input('css', drink_endtime_input, endtime)
        log.info('饮酒史结束时间%s:' % endtime)

        # print("输入开始时间{}".format(endtime))
        self.sleep(0.5)
        self.clicks('css', drink_durationr)
        self.sleep(0.5)
        self.input('css', drink_durationr_input, durtin)
        log.info('饮酒史时长%s:' % durtin)

        # print("输入开始时间{}".format(endtime))
        self.sleep(1)
        self.clicks('css', drink_remark)
        self.sleep(0.5)
        self.input('css', drink_remark_input, remark)
        log.info('吸烟备注%s:' % remark)

        self.sleep(0.5)

        self.clicks('css', drink_selection)
        self.sleep(0.5)
        self.clicks('class_name', drink_rates)
        self.sleep(0.5)
        self.clicks('css', drink_select_rate)
        self.sleep(0.5)
        self.clicks('css', drink_select_rate_btn)
        self.sleep(0.5)

    def clinical_info(self, confirmDate='', reportCancertype=''):
        """
        临床诊断史信息录入
        """
        log.info('开始录入临床诊断史信息')

        self.clicks('class_name', clinical_add)
        self.sleep(0.5)
        self.clicks('class_name', clinical_confirmDate)

        self.input('css', clinical_confirmDate_input, confirmDate)
        log.info('诊断日期%s:' % confirmDate)

        self.sleep(0.5)
        self.clicks('class_name', clinical_reportCancertype)
        self.sleep(0.5)
        self.input('css', clinical_reportCancertype_input, reportCancertype)
        log.info('诊断癌种类型%s:' % reportCancertype)

        self.sleep(0.5)
        self.clicks('css', clinical_selection)
        self.clicks('class_name', clinical_generate_report)
        self.sleep(0.5)

    def operationHistory_info(self, surgeryName=''):
        """
        治疗史信息录入
        """
        log.info('开始录入治疗史信息')

        self.clicks('css', operation_add)
        self.sleep(0.5)
        self.clicks('css', operation_treatmentType)
        self.sleep(0.5)
        self.clicks('css', operation_treatmentType_click)
        self.sleep(0.5)
        self.click_by_js('xpath', operation_treatmentType_select)
        self.sleep(0.5)
        self.clicks('css', operation_surgeryName)
        self.sleep(0.5)
        self.input('css', operation_surgeryName_input, surgeryName)
        log.info('治疗内容%s:' % surgeryName)

        self.sleep(0.5)
        self.clicks('css', operation_generate)
        self.sleep(0.5)

    def parentHistory_info(self, relationship=''):
        """
        家庭病史信息录入
        """
        log.info('开始录入家庭病史信息')

        self.clicks('css', parentHistory_add)
        self.sleep(0.5)
        self.clicks('css', FamilyMedicalHistory_relationship)
        self.sleep(0.5)

        self.input('css', FamilyMedicalHistory_relationship_inout, relationship)
        log.info('患者关系:%s' % relationship)

        self.wait_loading()
        self.click_by_js('xpath', FamilyMedicalHistory_relationship_select)
        self.sleep(0.5)
        self.clicks('css', parentHistory_selection)
        self.sleep(0.5)
        self.clicks('css', parentHistory_generate)
        self.sleep(5)

    def save_medical(self):
        """
        保存病历信息方法

        """
        self.clicks('css', save_btn)
        self.sleep(0.5)
        if self.isDisplayed('css', continue_save2):
            self.clicks('css', continue_save2)

    def continue_save_fun(self):
        """
        身份信息重复，校验后继续保存
        """
        if self.isDisplayed('css', continue_save):
            self.clicks('css', continue_save)

    def get_save_succe_info(self):
        """
        获取保存成功提示信息语
        :return:
        """
        try:
            info = self.get_text('xpath', save_info)
            log.info('获取页面提示信息{}'.format(info))
            return info
        except Exception as e:
            return None

    def get_save_info(self):
        """
        获取保存校验提示语
        :return:
        """
        return self.get_text('xpath', prompt_msg)

    def get_search_result(self):
        """
        点击选择查询结果
        :return:
        """
        self.clicks('css', search_result)

    def delete_search_result(self):
        """
        编辑页面点击删除按钮
        :return:
        """
        self.clicks('class_name', delete_btn)

    def enter_del_reason(self):
        """
        编辑页面点击删除，录入删除理由，点击删除确认
        :return:
        """
        self.input('css', delete_reason, 'This is TestCase!这是测试！')
        self.clicks('css', delete_confirm)
        self.wait_loading()
        self.wait_loading()
        self.sleep(0.5)

    def delete_confirmation(self):
        """
        删除后返回列表搜索已删除的数据
        :return:
        """
        self.clicks('class_name', return_list)
        self.clicks('class_name', return_list_conf)
        self.wait_loading()

    def get_result_text(self):
        """
        获取查询文本信息（暂无数据）
        :return:
        """
        if self.isElementExists('css', search_result):
            return self.get_text('css', search_result)
        else:
            return None

    def get_identificationNo(self):
        """
        身份证Excel中读取身份证信息
        :return: 返回身份证号
        """
        df = pd.read_excel(identificationNo_file_path)
        '''获取总行数'''
        rowsNum = df.shape[0]

        if rowsNum > 1:

            '''获取第一行身份证号码'''
            identificationNos = df.iloc[0].values
            print("读取的身份证号", identificationNos)

            '''从Excel中取第一行的身份证，去数据库查询是否已存在'''
            reslt = self.select_sql(bl_sql.format(identificationNos[0]))
            used_identificationNo = [i[item] for i in reslt for item in i]

            '''查询结果如果为0 ，则表示该身份证信息未被使用，则满足条件，返回该身份证'''
            if used_identificationNo[0] == 0:
                '''取出后删除该行'''
                df.drop(index=[0], axis=0, inplace=True)

                print("Excel中还剩", df.shape[0], "条身份证")

                df.to_excel(identificationNo_file_path, index=None)

                return identificationNos
            else:
                '''若该身份证查询出已有结果，则删除该身份证，程序进入递归查询'''
                df.drop(index=[0], axis=0, inplace=True)

                print("Excel中还剩", df.shape[0], "条身份证")

                df.to_excel(identificationNo_file_path, index=None)

                return self.get_identificationNo()


if __name__ == '__main__':
    s = MedicalPage
    # s.enter_medical()#driver
