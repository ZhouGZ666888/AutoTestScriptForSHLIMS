# -*- coding: utf-8 -*-
# @Time    : 2022/01/24
# @Author  : guanzhong.zhou
# @File    : MGMT模块元素定位


"""
MGMT首页列表元素定位
"""
# 搜索按钮
search = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-commonTaskListDialog-sampleIdLims input')

# 搜索弹框确认
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
MGMT待选表元素定位
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
    '.commonTaskDetail-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

#################################################
#                                               #
#                   明细表                       #
#                                               #
#                                               #
#################################################
# 列表全选按钮
detail_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 样本数据获取样本数据总数量
all_samples = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')


# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# *****************入库类型选择**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.button-list .mgmtSchedule-btn-batchStorageType')

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

#自动计算
autoComplete=(
    '.sampleDetail_header .button-list .baseClass-btn-autoComplete')

#自动计算有值时提示框
autoComplete_tip=(
    '.el-message-box__wrapper .el-message-box__btns button')

# 提交按钮
detail_submit_btn = (
    '.sampleDetail_header .button-list .baseClass-btn-submit')

# 提交弹框确认按钮
detail_submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')


# /************************入库****************************
# 入库按钮
deposit_into_storage = (
    '.sampleDetail_header .button-list .mgmtSchedule-btn-storage')

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

#提交状态文本定位
detail_sumbit_status=(
    '.createTask_content .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(15)')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 保存结果按钮
detail_save_result = (
    '.createTask .baseClass-btn-save')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask .baseClass-btn-goResult')
#################################################
#                                               #
#                   结果表                       #
#                                               #
#                                               #
#################################################

# 列表全选按钮
result_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量质检结果按钮
ultrafracResults=(
    '.sampleDetail_header .button-list .ultrafracResults-btn-qcResult')

#质检结果下拉选择
ultrafracResults_chioice=(
    '//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="合格"]')

#批量结果判读按钮
judgeResult=(
    '.sampleDetail_header .button-list .mgmtResults-btn-judgeResult')

#批量结果判读选项
judgeResult_choice=(
    '//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="否"]')

#自动计算按钮
result_autoComplete=(
    '.sampleDetail_header .button-list .el-button-group > button')

#自动计算有值提示
result_autoComplete_tips=(
    '.el-message-box__wrapper .el-message-box__btns button')


#完成任务单
complete_task=(
    '.createTask_content .baseClass-btn-completeTask')

#保存结果
result_save=(
    '.createTask_content .baseClass-btn-save')

#提交按钮
result_sumbit=(
    '.sampleDetail_header .button-list .geneResults-btn-submit')

#提交弹框实验室审核人
laboratory_auditor=(
    '.dialog-result-commit input')

#实验室审核人选择
laboratory_auditor_choice=(
    '.el-select-dropdown.el-popper .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

#提交确认按钮
result_sumbit_comfirm=(
    '.dialog-result-commit .el-dialog__footer .baseClass-btn-confirm')

#样本提交状态
sample_statue=(
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(15)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
detail_task_status = (
    '.createTask .clearfix div span:nth-child(3)')