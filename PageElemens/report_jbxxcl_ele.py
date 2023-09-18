# -*- coding: utf-8 -*-
# @Time    : 2021/12/27
# @Author  : guanzhong.zhou
# @File    : 报告---基本信息处理页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，订单号文本录入框元素定位
order_num = (
    '.reportBaseInfoProcessing-form-orderCode input')

# 筛选条件，项目号下拉框元素定位
project_num = (
    '.reportBaseInfoProcessing-form-projectId input')
# 筛选条件，选择项目号
project_num_chioce = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="J022"]]')

# 筛选条件，预计实验日期
poolingDate = (
    '.reportBaseInfoProcessing-form-poolingDate input')

# 筛选按钮
search_btn = (
    '.search-card .reportTaskDistribution-btn-onSearch')

# 订单信息数量
all_orders = (
    '//*[@class="sample_receive_detail"]')

# 重置按钮
reset_btn = (
    '.search-card .reportTaskDistribution-btn-reset')

# 修改病历按钮
editMedical_btn = (
    '.report-base-info-processing div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-btn-editMedical')

# 修改病历新弹框，页面title
editMedical_title = (
    '.navbar .el-breadcrumb.app-breadcrumb.breadcrumb-container .no-redirect')
# 添加报告任务
add_report_task = (
    '.el-card__body div.sample_receive_detail:nth-child(1) .reportBaseInfoProcessing-btn-addReportTask')

# 报告任务项-【产品】表单定位
report_project = (
    'div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-table tr:nth-child(1) td.reportBaseInfoProcessing-tableCol-productId')

# 报告任务项-【产品】表单下拉按钮
report_project_btn = (
    'div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-table tr:nth-child(1) td.reportBaseInfoProcessing-tableCol-productId input')

# 报告任务项-【产品】表单下拉选择世和一号
report_project_choice = (
    '//*[@class="vxe-select-option--wrapper"]/div[contains(text(),"世和一号")]')

# 报告任务项-【写入报告的上机样本】表单定位
report_on_board_sample = (
    '.el-card__body div.sample_receive_detail:nth-child(1) .reportBaseInfoProcessing-table tr:nth-child(1) td.reportBaseInfoProcessing-tableCol-sequencingList')

# 报告任务项-【写入报告的上机样本】弹框样本列表，原始样本号列值
report_on_board_sample_lab_num = (
    '.dialog-report-sample .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 报告任务项-【写入报告的上机样本】弹框确认按钮
report_on_board_sample_comfirm = (
    '.dialog-report-sample .el-dialog__footer .qcResult-btn-confirm')

# 报告任务项-【写入报告的不上机样本】表单定位
report_no_board_sample = (
    '.el-card__body div.sample_receive_detail:nth-child(1) .reportBaseInfoProcessing-table tr:nth-child(1) td.reportBaseInfoProcessing-tableCol-noSequencingList')

# 报告任务项-【写入报告的上机样本】弹框样本列表，原始样本号
report_no_board_sample_lab_num = (
    '.dialog-report-sample .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 报告任务项-【写入报告的上机样本】弹框确认按钮
report_no_board_sample_comfirm = (
    '.dialog-report-sample .el-dialog__footer .qcResult-btn-confirm')

# 报告任务项-【选择生信阴信对照】表单定位
choice_bioinformatic_negative = (
    '.el-card__body div.sample_receive_detail:nth-child(1) .reportBaseInfoProcessing-table tr:nth-child(1) td.reportBaseInfoProcessing-tableCol-sampleIdLabCode')

# 报告任务项-【选择生信阴信对照】弹框样本列表，原始样本号
choice_bioinformatic_negative_sample = '.el-dialog__body >div:nth-child(1) >div:nth-child(2) .contrast-sample-left-table .vxe-table--main-wrapper tr:nth-child(1) .vxe-radio--unchecked-icon'

# 报告任务项-【选择生信阴信对照】弹框样本列表，原始样本号
choice_bioinformatic_negative_lab_num='.el-dialog__body >div:nth-child(1) >div:nth-child(2) .contrast-sample-left-table .vxe-table--main-wrapper tr:nth-child(1) td:nth-child(3)'

# 报告任务项-【选择生信阴信对照】弹框确认按钮
choice_bioinformatic_negative_comfirm = (
    '.el-dialog .el-dialog__footer .qcResult-btn-confirm')

# 报告任务项-【报告形式】表单定位
report_style = '.el-card__body div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-tableCol-reportStyle div'

# 报告任务项-【报告形式】表单下拉
report_style_select = '.el-card__body div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-tableCol-reportStyle input'

# 报告任务项-【报告形式】表单下拉选项
report_style_choice = '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="正常"]]'

# 报告任务项-【报告归属】表单定位
report_belongTo = '.el-card__body div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-tableCol-belongTo div'

# 报告任务项-【报告归属】表单下拉
report_belongTo_select = '.el-card__body div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-tableCol-belongTo input'

# 报告任务项-【报告归属】表单下拉选项
report_belongTo_choice = '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="世和"]]'

# 报告任务项-【报告模板】表单定位
report_TemplateName = '.el-card__body div:nth-child(1).sample_receive_detail .reportBaseInfoProcessing-tableCol-reportTemplateName div'

# 报告任务项-【报告模板】弹框，搜索文本录入框
report_TemplateName_input ='.report-template-dialog .el-dialog__body .filter-container input'

# 报告任务项-【报告模板】弹框,搜索按钮
report_TemplateName_search_btn = '.report-template-dialog .el-dialog__body .baseClass-btn-search'

# 报告任务项-【报告模板】弹框搜索结果选择，第一条
report_TemplateName_choice ='.report-template-table .el-table__body-wrapper tbody tr:nth-child(1)'

# 报告任务项-【报告模板】弹框,确认按钮
report_TemplateName_search_comfirm = '.report-template-dialog .el-dialog__footer .el-button--primary'

# 点击查看按钮
click_view = '//*[@class="first_line"]/descendant::div/descendant::a[text()="点击查看"]'
# 点击查看，样本信息列表数
sample_info = '//*[@class="el-dialog__wrapper dialog-sample-info"]/descendant::tbody/tr'

# 点击查看，样本信息弹框确认
click_view_comfirm = '.dialog-sample-info .el-dialog__footer .baseClass-btn-confirm'
# ***********************************************************************
