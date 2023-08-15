# -*- coding: utf-8 -*-
# @Time    : 2021/09/10
# @Author  : guanzhong.zhou
# @File    : 病历模块元素定位


"""列表页元素"""
# 查询按钮，元素定位
search_btn = (
    '.filter-container .medicalList-btn-search')
# 新增按钮，元素定位
add_btn = (
    '.filter-container .medicalList-btn-created')
# 编辑按钮，元素定位
edit_btn = (
    'medicalList-btn-edit')
# 查询框确认按钮，元素定位
search_sure_btn = (
    'baseClass-btn-confirm')
# 查询框电子病历号文本录入框，元素定位
search_medicalNum = (
    '.medicalList-dialogSearch-patientId input')
# 查询结果（取第一条）
search_result = (
    'div.medicalList-table > div:nth-child(3) >table>tbody>tr:nth-child(1) > td:nth-child(1)')

"""
患者信息
"""
# 参检人姓名，元素定位
Participants_name = (
    '.medicalDetail-formPatientInfo-patientName input')
# 性别下拉框，元素定位
sex = (
    '.medicalDetail-formPatientInfo-gender input')
# 未知性别
unknown_sex = (
    '.gender-unique .el-scrollbar .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')
# 男性性别，元素定位
man_sex = '.gender-unique .el-scrollbar .el-scrollbar__view.el-select-dropdown__list li:nth-child(2)'
man_sex1='//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="男性"]]'

# 女性性别，元素定位
woman_sex = (
    '.gender-unique .el-scrollbar .el-scrollbar__view.el-select-dropdown__list li:nth-child(3)')
# 身份号码，元素定位
identificationNo = (
    '.medicalDetail-formPatientInfo-identificationNo input')
"""
吸烟史
"""
# 吸烟史-新增按钮，元素定位
smoking_his_add = (
    'medicalDetail-tableColSmoking-add')
# 吸烟史-删除按钮，元素定位
smoking_his_del = (
    'medicalDetail-tableColSmoking-delete')

# 吸烟史-选择频率按钮，元素定位
smoking_rates = (
    'medicalDetail-tableColSmoking-choiceFrequency')
# 频率列表，元素定位
rate_list = (
    '#app .smokeTable .dialog-select-frequency .el-table__body-wrapper tr:nth-child(1)')

# 选择频率确认按钮，元素定位
choice_rate_btn = (
    '.smokeTable .dialog-select-frequency .baseClass-btn-confirm')

# 明细勾选框按钮，元素定位
smoking_selection = (
    '#smokeTable .el-table__header-wrapper .el-table-column--selection .el-checkbox__input span')

# 新增吸烟明细-开始日期，元素定位
startDateValue = (
    'td.medicalDetail-tableColSmoking-startDateValue')
# 开始日期文本，元素定位
startDateValue_input = (
    'td.medicalDetail-tableColSmoking-startDateValue .show-edit input:nth-child(1)')

# 新增吸烟明细-结束日期
endDateValue = (
    'td.medicalDetail-tableColSmoking-endDateValue')
# 结束日期文本，元素定位
endDateValue_input = (
    'td.medicalDetail-tableColSmoking-endDateValue .show-edit input:nth-child(1)')

# 新增吸烟明细-时长，元素定位
durationr = (
    'td.medicalDetail-tableColSmoking-duration')
# 吸烟时长文本，元素定位
durationr_input = (
    'td.medicalDetail-tableColSmoking-duration .show-edit input:nth-child(1)')

# 新增吸烟明细-备注，元素定位
remarks = (
    'td.medicalDetail-tableColSmoking-remarks')
# 备注文本，元素定位
remarks_input = (
    'td.medicalDetail-tableColSmoking-remarks .show-edit input:nth-child(1)')

"""
饮酒史
"""
# 新增明细按钮，元素定位
drink_his_add = (
    'medicalDetail-tableColDrink-add')
# 删除选中，元素定位
drink_his_del = (
    'medicalDetail-tableColDrink-delete')
# 选择频率按钮，元素定位
drink_rates = (
    'medicalDetail-tableColDrink-choiceFrequency')
# 饮酒史全选按钮
drink_selection = (
    '#drinkTable .el-table__header-wrapper .el-table-column--selection .el-checkbox__input span')

# 开始日期待输入，元素定位
drink_starttime = (
    '#drinkTable .el-table__body-wrapper td:nth-child(2)')
# 开始日期文本框，元素定位
drink_starttime_input = (
    '#drinkTable .el-table__body-wrapper td:nth-child(2) .editCell input')

# 结束时间待输入，元素定位
drink_endtime = (
    '#drinkTable .el-table__body-wrapper td:nth-child(3)')

# 结束日期文本框，元素定位
drink_endtime_input = (
    '#drinkTable .el-table__body-wrapper td:nth-child(3) .editCell input')

# 时长待输入，元素定位
drink_durationr = (
    '#drinkTable .el-table__body-wrapper td:nth-child(4)')

# 时长文本框，元素定位
drink_durationr_input = (
    '#drinkTable .el-table__body-wrapper td:nth-child(4) .editCell input')

# 备注待输入，元素定位
drink_remark = (
    '#drinkTable .el-table__body-wrapper td:nth-child(6)')
# 备注文本框，元素定位
drink_remark_input = (
    '#drinkTable .el-table__body-wrapper td:nth-child(6) .editCell input')

# 选择频率选项，元素定位
drink_select_rate = (
    '#app .drinkTable .dialog-select-frequency .el-table__body-wrapper tr:nth-child(1)')
# 选择频率确认按钮，元素定位
drink_select_rate_btn = (
    '.drinkTable .dialog-select-frequency .baseClass-btn-confirm')

"""
临床诊断史
"""
# 临床诊断新增，元素定位
clinical_add = (
    'medicalDetail-tableColClinical-add')
# 临床诊断删除，元素定位
clinical_del = (
    'medicalDetail-tableColClinical-delete')
# 临床诊断生成描述报告，元素定位
clinical_generate_report = (
    'medicalDetail-tableColClinical-generate')

# 临床诊断全选按钮，元素定位
clinical_selection = (
    '#CDHistory .vxe-table--fixed-left-wrapper .vxe-cell--checkbox > span:nth-child(2)')
# 临床诊断确诊日期，元素定位
clinical_confirmDate = (
    'medicalDetail-tableColClinical-confirmDate')
# 临床诊断确诊日期输入，元素定位
clinical_confirmDate_input = (
    '.medicalDetail-tableColClinical-confirmDate input')

# 临床诊断癌种简称，元素定位
clinical_reportCancertype = (
    'medicalDetail-tableColClinical-reportCancerType')
# 临床诊断癌种简称输入，元素定位
clinical_reportCancertype_input = (
    '.medicalDetail-tableColClinical-reportCancerType input')

# 临床诊断是否疑似，元素定位
clinical_isDoubt = (
    'medicalDetail-tableColClinical-isDoubt')
# 临床诊断是否疑似输入，元素定位
clinical_isDoubt_input = (
    'medicalDetail-tableColClinical-isDoubt')
# 临床诊断癌种类型，元素定位

# 临床诊断癌种类型选择，元素定位

# 临床诊断TNM，元素定位
clinical_cancerTnm = (
    'medicalDetail-tableColClinical-cancerTnm')

# 临床诊断TNM选择，元素定位
clinical_cancerTnm_chiose = (
    '#CDHistory .el-card__body .card-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(7)  .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')
# 临床诊分期，元素定位
clinical_cancerStaging = (
    'medicalDetail-tableColClinical-cancerStaging')
# 临床诊断分期选择，元素定位


"""
治疗史
"""

# 治疗史新增，元素定位
operation_add = (
    '#operationHistory .medicalDetail-tableColOperation-add')
# 治疗史删除，元素定位
operation_delete = (
    '#operationHistory .medicalDetail-tableColOperation-delete')
# 治疗史生成报告描述，元素定位
operation_generate = (
    '#operationHistory .medicalDetail-tableColOperation-generate')
# 治疗史类型，元素定位
operation_treatmentType = (
    '#operationHistory .medicalDetail-tableColOperation-treatmentType')
# 治疗史类型选中，元素定位
operation_treatmentType_click = (
    '#operationHistory .medicalDetail-tableColOperation-treatmentType input')
# 治疗史类型录入，元素定位
# operation_treatmentType_select = (
#     '.select-treatment-type .vxe-table--ignore-clear .vxe-select-option--wrapper div:nth-child(1)')
operation_treatmentType_select = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="用药治疗史"]]')

# 治疗史开始日期，元素定位
operation_startDate = (
    '#operationHistory .medicalDetail-tableColOperation-startDate')



# 治疗史是否至今，元素定位
# 治疗史是否至今录入，元素定位
# 治疗史截止日期，元素定位
# 治疗史截止日期录入，元素定位
# 治疗史药物标准化名称，元素定位
# 治疗史药物标准化名称录入，元素定位
# 治疗史新增治疗内容，元素定位
operation_surgeryName = (
    '.medicalDetail-tableColOperation-surgeryName')
# 治疗史--治疗内容录入，元素定位
operation_surgeryName_input = (
    '#operationHistory .medicalDetail-tableColOperation-surgeryName input')

# 治疗史新增用药周期数
# 治疗史新增用药周期数录入，元素定位
# 治疗史新增周期单位，元素定位
# 治疗史新增周期单位录入，元素定位
# 治疗史新增疗效，元素定位
# 治疗史新增疗效录入，元素定位
# 治疗史新增备注，元素定位
# 治疗史新增备注录入，元素定位


"""
家庭病史
"""
# 家庭病史新增明细，元素定位
parentHistory_add = (
    '#parentHistory .medicalDetail-tableColOperation-add')
# 家庭病史删除，元素定位
# 家庭病史生成报告描述，元素定位
parentHistory_generate = (
    '#parentHistory .medicalDetail-tableColOperation-generate')

# 家庭病史患者关系，元素定位
FamilyMedicalHistory_relationship = (
    '#parentHistory .el-table__body-wrapper tr:nth-child(1) .medicalDetail-tableColFamilyMedicalHistory-relationship')

# 家庭病史患者关系录入，元素定位
FamilyMedicalHistory_relationship_inout = (
    '#parentHistory .el-table__body-wrapper tr:nth-child(1) .medicalDetail-tableColFamilyMedicalHistory-relationship input')

# 家庭病史患者关系选中，元素定位
FamilyMedicalHistory_relationship_select = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="祖父"]]')
# 家庭病史全选按钮，元素定位
parentHistory_selection = (
    '#parentHistory .card-table .el-table__header-wrapper span > span')

# 页面保存按钮，元素定位
save_btn = (
    '.main-container .baseClass-btn-handleSavaBefore')

# 保存成功结果提示语，元素定位
save_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')
prompt_msg = (
    '//*[@class="el-message el-message--info"]/p')

#身份证信息与当前出生日期不符
brithday_error=(
    '.dialog-msg .el-dialog__footer .btn-continue-save')

# 身份证重复继续保存确认按钮，元素定位
continue_save = (
    '.dialog-repeat-medical .medicalDetail-repeatDialog-save')

continue_save2 = (
    '.dialog-msg .dialog-footer .btn-continue-save ')




'''编辑页面元素'''
# 删除按钮
delete_btn = (
    'baseClass-btn-delete')

# 删除理由文本框
delete_reason = (
    '.dialogDelete-dialogBoxDelete-title textarea')
# 删除理由确认按钮
delete_confirm = (
    '.dialogDelete-dialogBoxDelete-title .baseClass-btn-save')
# 删除页面，返回列表按钮
return_list = (
    'baseClass-btn-cancel')
# 返回列表确认按钮
return_list_conf = (
    'baseClass-btn-continue')
