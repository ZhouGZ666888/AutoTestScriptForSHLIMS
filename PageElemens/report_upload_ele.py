# -*- coding: utf-8 -*-
# @Time    : 2021/12/31
# @Author  : guanzhong.zhou
# @File    : 报告上传页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，订单号文本录入框元素定位
order_num = (
    '.search-card .reportUpLoad-form-orderCode input')

# 筛选条件，项目号下拉框元素定位
project_num = (
    '//*[@class="el-select reportUpLoad-form-projectId el-select--small"]/descendant::input')
# 筛选条件，选择项目号
project_num_chioce = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="J022"]]')

# 筛选条件，预计实验日期
poolingDate = (
    '//*[@class="reportUpLoad-form-preinstallPoolingDate"]/descendant::input')

# 筛选条件，报告分配日期
lastPoolingDate = (
    '.reportUpLoad-form-lastPoolingDate input')

# 筛选按钮
search_btn = (
    '.search-form .reportTaskDistribution-btn-onSearch')

# 全部报告任务单
all_orders = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr')

# 重置按钮
reset_btn = (
    '.search-form .reportTaskDistribution-btn-reset')

# 批量下载报告模板按钮
download_all_btn = (
    '//*[@class="search-card"]/descendant::button[child::span[text()="批量下载报告模板"]]')

#报告归属按钮文本定位
report_belong=(
    '.sample_receive_detail:nth-child(1) .report-upload-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(5) div')

#报告归属下拉文本定位
report_belong_input=(
    '.sample_receive_detail:nth-child(1) .report-upload-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(5) input')

#报告归属下拉值选择
report_belong_choice=(
    '//body/div[@class="el-select-dropdown el-popper"]/descendant::ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[child::span[text()="世和"]]')

# 复审人表单定位
rehearing_person = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr/td[15]/div/div/div')

# 复审人弹框文本录入
rehearing_person_input = (
    '.dialog-choose-user .select-next-processor input')

# 复审人弹框文本录入后选择
rehearing_person_choice = (
    '//ul[@class="el-scrollbar__view el-select-dropdown__list"]/descendant::li[child::span[text()="{}"]]')

# 复审人弹框确认按钮
rehearing_person_comfirm = (
    '.dialog-choose-user .baseClass-btn-confirm')

# 报告文件编辑表单定位
report_file_btn = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr[1]/td[17]/div/button')

# 报告文件上传按钮
report_upload_btn = (
    '.card-report-file .el-upload input')

# 解读文件上传按钮
decode_upload_btn = (
    '.card-decode-file .el-upload input')

# 其他文件上传按钮
other_upload_btn = (
    '.card-other-file .el-upload input')

# 报告文件上传弹框确认按钮
report_upload_comfirm = (
    '.dialog-upload-file .qcResult-btn-confirm')

# 突变文件编辑表单定位
mutation_file_btn = (
    '//*[@class="vxe-table--main-wrapper"]/descendant::tbody/tr/td[18]/div/button')

# 突变文件上传按钮
mutation_file_upload_btn = (
    '.dialog-mutation-file .el-upload input')

# 突变文件上传确认
mutation_file_upload_comfirm = (
    '.dialog-mutation-file .dialog-footer button')

# 完成任务按钮
complete_task = (
    '.sample_receive_detail:nth-child(1) .report-upload-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .btn-task-status')
#完成按钮状态文本定位
complete_status=(
    '.el-card.box-card.is-always-shadow div:nth-child(1).sample_receive_detail .vxe-table--main-wrapper .vxe-table--body-wrapper tbody .btn-task-status')

# 页面提示信息，元素定位
page_info = (
    '//*[@class="el-message el-message--success"]')
