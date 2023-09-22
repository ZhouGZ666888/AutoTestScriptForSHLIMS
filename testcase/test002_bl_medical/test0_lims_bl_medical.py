import unittest, re, ddt
from common.all_path import medicalinfo_path, orderNub_path
from common.enter_tab import EnterTab
from common.screenshot import Screenshot
from pageobj.medicalPage import MedicalPage
from common.editYaml import read_yaml, save_yaml
from common.Main import MyTest
from common.logs import log


@ddt.ddt
class LimsMedical(MyTest):
    # 定义类属性
    datas = read_yaml(medicalinfo_path)

    orderinfo = read_yaml(orderNub_path)

    def setUp(self) -> None:
        self.mp = MedicalPage(self.driver)

    def test01_add_medical(self):
        """
        测试新建病历并保存(包含几个史的新增信息)
        """
        self.initialize()

        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)

        log.info('进入新增模块')
        self.mp.click_add_medical()

        log.info('读取新的身份证')
        add_identificationNo = self.mp.get_identificationNo()
        log.info('录入患者姓名，身份证信息')
        self.mp.input_patientinfo(name=add_identificationNo[1], identityNo=add_identificationNo[0])
        log.info('录入吸烟史')
        self.mp.smoking_info(starttime=self.datas['starttime'], endtime=self.datas['endtime'],
                             durtin=self.datas['durtin'],
                             remark=self.datas['remark'])

        log.info('录入饮酒史')
        self.mp.drink_info(starttime=self.datas['starttime'], endtime=self.datas['endtime'],
                           durtin=self.datas['durtin'],
                           remark=self.datas['remark'])

        log.info('录入临床诊断史')
        self.mp.clinical_info(confirmDate=self.datas['confirmDate'],
                              reportCancertype=self.datas['reportCancertype'])

        log.info('治疗史信息录入')
        self.mp.operationHistory_info(surgeryName=self.datas['surgeryName'])

        log.info('家庭病史信息录入')
        self.mp.parentHistory_info(relationship=self.datas['relationship'])

        log.info('保存病历')
        self.mp.save_medical()
        self.mp.wait_loading()
        Screenshot(self.driver).get_img("病历详情页面，录入病历信息后，点击保存按钮","保存病历成功")
        # 获取新建病历号
        result = self.driver.execute_script(
            'return document.getElementsByClassName("medicalDetail-formPatientInfo-patientId")[0].getElementsByClassName("el-input__inner")[0].value')
        print('获取新建病历号', result)

        # 将获取的新建病历号更新到订单和病例信息表yaml文件中
        self.orderinfo['name'] = add_identificationNo[1]
        self.orderinfo['identificationNo'] = add_identificationNo[0]
        self.orderinfo["medicalnum_no"] = result
        save_yaml(orderNub_path, self.orderinfo)

        self.assertIsNotNone(result)

    def test02_medical_Missing_information(self):
        """
        测试新增病历，校验身份证、姓名必填未填时，保存提示信息
        """
        log.info('登录系统，进入病历页面')

        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)
        log.info('进入新增模块')
        self.mp.click_add_medical()
        log.info('录入空的患者姓名和身份证')
        self.mp.input_patientinfo(name='', identityNo='')
        log.info('保存病历')
        self.mp.save_medical()
        result = re.search(r'请输入正确的姓名、性别、证件号码', self.mp.get_source)
        self.assertIsNotNone(result)

    def test03_medical_identification_repeat(self):
        """
        测试新建病历，身份证重复时，系统做出校验
        """

        EnterTab.enter_crm(self.basepage)

        log.info('进入新增模块')
        self.mp.click_add_medical()

        log.info('录入患者姓名，身份证信息')
        self.mp.input_patientinfo(name=self.orderinfo['name'],
                                  identityNo=self.orderinfo['identificationNo'])

        log.info('保存病历')
        self.mp.save_medical()
        self.mp.wait_loading()
        result = re.search(r'系统内已存在相同身份证号的病历', self.mp.get_source)
        self.mp.refresh()

        self.assertIsNotNone(result)

    def test04_search_medical(self):
        """
        测试根据病历号检索功能
        """
        EnterTab.enter_crmorder(self.basepage)
        EnterTab.enter_crm(self.basepage)
        log.info('点击搜索')
        self.mp.search_medical()

        log.info('搜索病历号')
        self.mp.search_by_param(self.orderinfo['medicalnum_no'])

        log.info('点击确定')
        self.mp.click_search_btn()
        self.mp.wait_loading()

        log.info('获取查询结果，进行断言')
        result = re.search(self.orderinfo['medicalnum_no'], self.mp.get_source)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
