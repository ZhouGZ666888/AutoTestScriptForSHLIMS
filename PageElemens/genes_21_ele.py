# -*- coding: utf-8 -*-
# @Time    : 2021/12/16
# @Author  : guanzhong.zhou
# @File    : 21基因元素定位
# -*-*************************************************************************************-*-
"""
21基因首页列表元素定位
"""
# 搜索按钮
search = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-commonTaskListDialog-sampleIdLims input')

# 搜素弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-confirm')

# 新增按钮
add_task = (
    '.app-container .filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-


"""
21基因待选表元素定位
"""
# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值,m默认选择第一条
select_sop_choice = (
    '.sopId-unique .el-select-group__wrap .el-select-group li:nth-child(1)')

# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')

# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail textarea')

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

# 待选列表全选按钮
all_choice = (
    '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-submit')

# 进入明细表按钮，元素定位
enter_detail_list_btn = (
    '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

# ***********************************************************************************************************#
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
#                                          21基因明细表元素定位                                                 #
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
#                                                                                                            #
# ***********************************************************************************************************#


# 列表全选按钮
detail_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 样本数据获取样本数据总数量
all_samples = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

#获取样本lims号
samples_lims=(
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(2)')

# Qubit浓度（实测）ng/μL*表单定位
actual_qubit_concentration = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualConsistenceAmt.errCell')

# Qubit浓度（实测）ng/μL*表单录入
actual_qubit_concentration_input = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualConsistenceAmt.errCell > div >div >input')

# 体积（实测）μL*表单定位
actual_volume = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualVolumeAmt.errCell')

# 体积（实测）μL*文本录入
actual_volume_input = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualVolumeAmt.errCell> div >div >input')

# 总量（实测）ng*表单定位
actual_total_amount = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualTotalAmt.errCell')

# 总量（实测）ng*文本录入
actual_total_amount_input = (
    'table > tbody > tr:nth-child({}) > td.vxe-body--column.col--center.col--edit.col--ellipsis.geneSchedule-tableCol-actualTotalAmt.errCell > div >div > input')

# 合并分析按钮
merge = (
    '.createTask_content .sampleDetail_header .geneSchedule-btn-merge')

# 合并分析弹框选择主数据
merge_main_sample = (
    '.dialog-merge .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1) td:nth-child(1)')

# 合并分析弹框选择主数据确认
merge_main_btn = (
    '.dialog-merge .el-dialog__footer .baseClass-btn-confirm')

# 合并分析弹框确认继续
merge_main_continue_btn = (
    '.dialog-attention .el-dialog__footer .baseClass-btn-continue')

#明细表提交按钮
detail_submit_btn=(
    '.createTask_content .sampleDetail_header .baseClass-btn-submit')

#明细表提交确认按钮
detail_submit_comfirm=(
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 保存结果按钮
detail_save_result = (
    '.createTask_content .baseClass-btn-save')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask_content .baseClass-btn-goResult')

# /************************入库****************************
# 入库按钮
deposit_into_storage = (
    '.button-list .libconstructionSchedule-btn-storage')

# 入库弹框全选按钮
storage_all_choice = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 入库弹框选择入库类型下拉框
target_storage_type = (
    '.dialog-check-storage .checkStorageDialog-btn-targetLocation')

# 入库弹框选择入库类型下拉值（临时库）
target_storage_type_value = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库"]')

# 入库弹框选择样本盒按钮
batch_paste_sample_box = (
    '.dialog-check-storage .checkStorageDialog-btn-selectBox')

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-boxSearchDialogForm-boxName input')

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.dialog-box-search .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)')

# 入库弹框选选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.dialog-box-search .dialog-footer .baseClass-btn-confirm')

# 入库弹框样本总数
all_select_sample_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(7)')

# 入库弹框盒内位置
detail_position_in_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7)')

# 入库弹框盒内位置文本框
detail_position_in_box_input = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7) input')

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.dialog-check-storage .checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box .dialog-footer .baseClass-btn-confirm')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.dialog-position-box textarea')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .dialog-footer .baseClass-btn-next')





"""
21基因结果表元素定位
"""

# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

#21基因结果分析按钮
result_analysis=(
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .type--button')

#算法版本下拉框定位
aly=(
    '.aly-form-sopId input')

#算法版本下拉值
aly_choice=(
    '.sopId-unique .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

#对照基因组Cq平均值
refCqAvgValue=(
    '.aly-form-refCqAvgValue input')

#21基因结果内参平均值是否合格下拉框
isEligible=(
    '.aly-form-isEligible input')

#21基因结果内参平均值是否合格下拉值
isEligible_choice=(
    '.isEligible-unique .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

# RSU值
rsu=(
    '.aly-form-rsuValue input')

#RS值
rs=(
    '.aly-form-rsValue input')

#批量导入数据按钮
batchImport=(
    '.is-always-shadow .baseClass-btn-batchImport')

#批量导入数据录入框
batchImport_input=(
    '.dialog-channel textarea')

#批量导入数据弹框确认按钮
batchImport_comfirm=(
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

#21基因分析任务信息页保存按钮
twentyonegene_analysis_save=(
    '.app-main .filter-container .baseClass-btn-save')

#21基因分析任务信息页完成按钮
twentyonegene_analysis_complete=(
    '.app-main .filter-container .baseClass-btn-finish')

# 21基因分析任务信息页面导入成功提示信息
import_data=(
    '.el-message.el-message--success.el-message-fade-enter-active.el-message-fade-enter-to')

# 结果表提交按钮
result_submit = (
    '.sampleDetail_header .button-list .geneResults-btn-submit')

# 结果表提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .el-dialog__footer .qcResult-btn-confirm')



# 完成任务单按钮
result_complete_task_btn = (
    '.sampleDetail_header .button-list .geneResults-btn-completeTask')

# 完成任务单提示弹框确认按钮
result_complete_task_comfirm = (
    '//div[@class="el-message-box__wrapper"]/descendant::button[child::span][2]')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
detail_task_status = (
    '.createTask .clearfix div span:nth-child(3)')
