# -*- coding: utf-8 -*-
# @Time    : 2021/11/10
# @Author  : guanzhong.zhou
# @File    : 订单模块元素定位


# 搜索订单按钮，元素定位
search_order = (
    '.app-main .baseClass-btn-search')

# 新增订单按钮，元素定位
add_orders = (
    'baseClass-btn-add')

# 编辑订单按钮，元素定位
edit_order = (
    '.baseClass-btn-edit')

# 搜索弹框订单号文本录入框
search_order_input = (
    '.orderList-dialogSearch-orderCode input')

# 搜索弹框确认按钮
search_order_comfirm = (
    '.dialog-search .baseClass-btn-confirm')

# 订单列表第一条订单，
first_order = (
    '.el-table--enable-row-hover.el-table--enable-row-transition .el-table__body-wrapper tr:nth-child(1)')

"""
新增弹框元素
"""
# 新增订单号输入框，元素定位
order_num_input = (
    '.dialog-created .orderList-dialogCreated-orderCode input')

# 患者姓名输入框，元素定位
patient_name_input = (
    '.dialog-created .orderList-dialogCreated-patientName input')

# 新增订单确认按钮，元素定位
add_confirm = (
    '.baseClass-btn-confirm')

"""
编辑订单元素
"""
# 保存按钮，元素定位
save_button = (
    '.app-main .baseClass-btn-handleSavaBefore')

# 选择癌种类型，元素定位
cancer_type_chioce = (
    '.orderDetail-formBaseInfo-reportCancerType input')
# 选择癌种（肠癌）
cancer_type = (
    '.el-select-dropdown__list ul[value="RCST"] .el-select-group li:nth-child(5)')

# 选择电子病历号文本框，元素定位
ele_patient_number = (
    '.orderDetail-formBaseInfo-patientId input')
####选择病历弹框####


# 病历搜索项【用户名】
patient_name = (
    '.orderDetail-dialogChoiceMedical-patientName input')

# 病历搜索项【身份证号】
identification_numb = (
    '.dialog-ChoiceMedical .orderDetail-dialogChoiceMedical-identificationNoWildCard input')

# 病历搜索按钮
search_num_button = (
    '.dialog-ChoiceMedical .baseClass-btn-search')

# 生成新病历按钮，元素定位
new_case = (
    'orderDetail-dialogChoiceMedical-btnAddMedicalInfo')

# 选择已存在的、类似的关联病历
similar_case = (
    '.dialog_table .el-table__body-wrapper tr:nth-child(1)')

# 选择病历后确认按钮，元素定位
ele_chioce_confirm = (
    '.dialog-ChoiceMedical .baseClass-btn-confirm')

# 选择关联病历后点击确认，弹出解除关联确认弹框，确认按钮，元素定位
chioce_and_confirm = (
    '.el-message-box .el-message-box__btns button:nth-child(2)')

# 报告是否体现医院信息下拉选择，元素定位
is_hospital_info_displayed = (
    '.orderDetail-formMedicalBaseInfo-isDisplayHos input')

# 报告是否体现医院信息下拉选择，选项确认【是】，元素定位
hospital_info_displayed = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[1]')

# 报告寄送人选择文本框
report_receiver_button = (
    ".orderDetail-formMedicalBaseInfo-defaultRptRcv input")

# 报告寄送人选择，默认选择第一个(患者家属)
report_receiver = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="患者家属"]]')

#报告是否寄送纸质版下拉框
formMedicalBaseInfo='.orderDetail-formMedicalBaseInfo-isSendPaper input'

#报告是否寄送纸质版下拉框选择
formMedicalBaseInfoChoice='/html/body/div[last()]/div[1]/div[1]/ul/li[1]'

####选择主订单号弹框####


# 选择主订单号文本框，元素定位
#选择所属套餐
productPkgId=(
    '.orderDetail-formMedicalBaseInfo-productPkgId input')
#所属套餐下拉值
productPkgId_choice=(
    '//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/descendant::li[span[text()="脉搏计划"]]')

#动态检测次数
pulseplanCount=(
    '.orderDetail-formMedicalBaseInfo-pulseplanCount input')


main_order_number = (
    '.orderDetail-formMedicalBaseInfo-pulseplanParent input')

# 主订单号弹框选择主订单号，默认选择第一条
chioce_main_order_number = (
    '.dialogChoice-MainOrder .el-table__body-wrapper tr:nth-child(1)')

# 选择主订单号确认按钮
chioce_main_order_number_confirm = (
    '.dialogChoice-MainOrder  .el-dialog__footer .baseClass-btn-confirm')

# 添加联系人按钮，元素定位
add_new_contact = (
    '.orderDetail-tableColContact-btnAddOrderContactList')

# 联系人姓名，元素定位
contact_name = (
    '.el-card__body .el-table__body-wrapper tr:nth-child(1) .orderDetail-tableColContact-contactName')
# 联系人姓名文本录入，元素定位
contact_name_inout = (
    '.el-card__body .el-table__body-wrapper tr:nth-child(1) .orderDetail-tableColContact-contactName input')

# 联系人电话表单定位
contact_tel_numb = (
    '.el-card__body .el-table__body-wrapper tr:nth-child(1) .orderDetail-tableColContact-contactMobile')
# 联系人电话文本录入
contact_tel_numb_input = (
    '.el-card__body .el-table__body-wrapper tr:nth-child(1) .orderDetail-tableColContact-contactMobile input')

# chioce_contact_county = ("//span[contains(text(),'本溪市')]")
# 联系人详细地址
contact_address = (
    '//*[@class="orderDetail-tableColContact-addrStreet"]/div/div/div/div/input')

####选择送检医生弹框####

# 选择送检医生文本框，元素定位
chioce_physician = (
    '.select-doctor-name.el-input input')

# 医生列表根据科室查询
search_by_department = (
    '.orderDetail-dialogChoiceDoctor-departmentName input')

# 录入查询条件后，查询按钮
physician_search_button = (
    '.el-button.baseClass-btnBaseClass-search')

# 选择查询结果，默认选中第一条
chioce_department = (
    '.dialog-choiceDoctor .dialog_table .el-table__body-wrapper tr:nth-child(1)')

# 选择医生后确认按钮
chioce_physician_confirm = (
    '.dialog-choiceDoctor .el-dialog__footer .baseClass-btn-confirm')

# 修改销售按钮
sales_information = '//button/span[text()="修改销售"]'

#修改销售弹框文本录入
sales_input='.dialog-change-order .orderDetail-formSalesInfo-salesName input'


# 选择销售人员，默认选中第一条
chioce_sale = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[1]')

# 应收金额弹框文本
payment_due = (
    '.orderDetail-formSalesInfo-paymentDue input')

# 修改后的金额
fee_after_amendment = (
    '.orderDetail-dialogChangeFee-amend input')

# 修改理由
amendment_reason = (
    '.orderDetail-dialogChangeFee-amend_cause textarea')

# 修改金额确认
change_fee_confirm = (
    '.orderDetail-dialogChangeFee-title .el-dialog__footer .baseClass-btnBaseClass-confirm')

# 保存成功提示信息
save_success_info = (
    '.el-message.el-message--success')

