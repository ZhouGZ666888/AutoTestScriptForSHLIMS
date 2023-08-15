# -*- coding: utf-8 -*-
# @Time    : 2022/02/08
# @Author  : guanzhong.zhou
# @File    : 数据修改页面元素定位
# -*-*************************************************************************************-*-

"""
首页面元素定位
"""
# 查看按钮
edit_btn = (
    '.filter-container .baseClass-btn-edit')

# 搜索按钮
search_btn = (
    '.filter-container .baseClass-btn-search')

# 搜索弹框，来源任务单号文本框
srcTaskId = (
    '.dialog-search-component .dataChangeList-form-srcTaskId input')

# 搜索弹框，LIMS样本号文本框
sampleIdLims = (
    '.dialog-search-component .dataChangeList-form-sampleIdLims input')

# 搜索弹框，确认按钮
comfirm_btn = (
    '.dialog-search-component .el-dialog__footer .baseClass-btn-confirm')

# 页面列表第一条任务单任务单号文本定位
first_task_id = (
    '.el-card__body .sample_receive_detail .el-table__body-wrapper tbody tr:nth-child(1) td:nth-child(1)')

# 页面列表第一条任务单任务单状态文本定位
first_task_status = (
    '.el-card__body .sample_receive_detail .el-table__body-wrapper tbody tr:nth-child(1) td:nth-child(6)')

# 待办任务，数据修改审核tab页
datachange_tab = (
    '#tab-fourth')

# 待办任务，数据审核进入按钮
enter_datachange = (
    '.el-tabs__content #pane-fourth .el-table__body-wrapper tbody tr:nth-child(1) .baseClass-btn-enter')

# 数据修改详情，完成审核按钮
complete_edit = (
    '.app-container .filter-container .dataChangeDetail-btn-handleCommit')

# 数据修改详情，任务状态信息
task_status = (
    '.el-card.box-card .el-card__header span:nth-child(3)')

# 数据修改详情，申请单号
application_number = (
    '.el-card.box-card .el-card__header span:nth-child(1)')

# 核酸提取模块，数据修改按钮
datachange = (
    '.createTask_content .sampleDetail_header .extractionSchedule-btn-dataChange')

# 核酸提取模块，明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 核酸提取明细表，数据列表第一条样本
first_sample = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# 核酸提取模块，数据修改-发起修改按钮
startChange = (
    '.sampleDetail_header .button-list .extractionSchedule-btn-startChange')

# 发起修改弹框，指定审核人下拉框
placeHolder_select_btn = (
    '.dialog-data-change .el-dialog__body .baseClass-placeHolder-select input')

# 发起修改弹框，选择审核人
choice_placeHolder = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="{}"]]')

# 发起修改弹框，修改原因
dataChangeReason_reason = (
    '.dialog-data-change .el-dialog__body .dataChangeReason-reason textarea')

# 发起修改弹框，下一步按钮
next_step = (
    '.dialog-data-change .el-dialog__footer .baseClass-btn-next')

# 数据修改弹框，全选按钮
all_choice = (
    '.el-dialog .el-dialog__body .createTask_content_table_1 .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 数据修改弹框，批量实测数据按钮
batchData_btn = (
    '.el-dialog .el-dialog__body .button-list .border_size')

# 数据修改弹框，批量实测数据弹框，样本进入量
usedTotalAmt = (
    '.dialog-multi-data .multiData-multiDataDialogForm-usedTotalAmt input')

# 数据修改弹框，批量实测数据弹框，包装单位
samplePkgAmtUnit = (
    '.dialog-multi-data .multiData-multiDataDialogForm-samplePkgAmtUnit input')

# 数据修改弹框，批量实测数据弹框，包装单位下拉选择
samplePkgAmtUnit_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="管"]]')

# 数据修改弹框，批量实测数据弹框,确认按钮
batchData_comfirm = (
    '.dialog-multi-data .el-dialog__footer .baseClass-btn-confirm')

# 数据修改 - 数据修改详情弹框，完成&提交申请按钮
complete_submit_btn = (
    '//*[@aria-label="数据修改 - 数据修改详情"]/descendant::button[child::span[text()="完成&提交申请"]]')


# 退出登录按钮
logout_btn = '.navbar .right-menu div:nth-child(2) span'

# 退出登录
logout_choice = '//ul/li[child::span[text()="退出登录"]]'
