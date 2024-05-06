# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guanzhong.zhou
# @File    : 样本处理元素定位
# -*-*************************************************************************************-*-
"""
样本处理首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')
# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-commonTaskListDialog-sampleIdLims input')
# 搜索弹框确认
search_confirm = (
    '.dialog-search .dialog-footer .baseClass-btn-confirm')
# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')
##页面列表样本
sample_page_list = (
    '//div[@class="sample_receive_detail"]/descendant::tbody/tr')
# -*-*************************************************************************************-*-


'''
待选表元素定位
'''
# 选择任务类型点击下拉框
task_type = (
    '.select-task-type input')
# 样本类型选择下拉值，默认第一条
task_type_choice = (
    '.task-type-unique .el-select-dropdown__list li:nth-child(1)')
# 选择sop下拉框
select_sop = (
    '.select-sop-type input')
# 选择sop下拉值
select_sop_choice = (
    '.sopId-unique .el-select-group li:nth-child(1)')

# 实验室值班主管
dutySupervisors = '.createTask_content_choose .extractionDetail-form-dutySupervisors'
# 选择实验室值班主管
select_dutySupervisors = '//*[@class="el-select-dropdown el-popper"]/descendant::span[text()="杜长琬"]'
# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')
# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail.dialog-expMgmt-detail textarea')
# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

# 待选列表全选按钮
all_choice = (
    ' .vxe-table--header-wrapper.body--wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-submit')
# 进入明细表按钮，元素定位
enter_result_list_btn = (
    '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-goSchedule')
# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

# 子SOP样本数量按钮
sopSampleNumber_btn = '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-sopSampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber_input = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber input'

# 子SOP样本数量弹框确认按钮
sopSampleNumber_confirm = '.dialog-sop-sample-number .el-dialog__footer .taskInitial-form-currentStepName'

'''
样本处理明细表元素定位
'''
# 样本列表数据全选按钮

# 生成排序号按钮
create_sort_number = (
    '.button-list .schedule-btn-sortNo')

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 批量入库类型下拉框
batch_storage_type = (
    '.button-list .schedule-btn-batchStorageType')
# 批量入库类型下拉值
batch_actual_data_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')
# 批量实测数据
batch_actual_data = (
    '.button-list .baseClass-btn-batchData')
# 批量实测数据-样本计量（实测）
Acual_sample_amount = (
    '.dialog-experiment-actualSampleAmt input')
# 批量实测数据-包装量（实测）
Actual_sample_package_amount = (
    '.dialog-experiment-actualSamplePkgAmt input')

# 批量实测数据弹框按钮
batch_actual_data_btn = (
    '.dialog-experiment-data .el-dialog__footer .baseClass-btn-confirm')
# 批量余样数据
batch_remaining_data = (
    '.button-list .baseClass-btn-remainData')
# 计量余样录入框
remaining_sample_amount = (
    '.dialog-remain-remainingSampleAmt input')
# 包装余量录入框
remaining_sample_package_amount = (
    '.dialog-remain-remainingSamplePkgAmt input')

# 批量余样弹框确认按钮
batch_remaining_data_confirm = (
    '.dialog-remain-data .el-dialog__footer .baseClass-btn-confirm')

# 目标库位类型下拉框
target_storage_type = (
    '.button-list .baseClass-btn-deposit')

# 目标库位类型下拉值
target_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库" and following-sibling::li[text()="永久库"]]')

# 选择样本盒按钮
select_sample_box = (
    '//*[@class="button-list"]/descendant::button[child::span[text()="选择样本盒"]]')

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-boxSearchDialogForm-boxName input')

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.dialog-box-search .el-table__body-wrapper tr:nth-child(1)')

# 选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.dialog-box-search .dialog-footer .baseClass-btn-confirm')

# 提交按钮
submit_btn = (
    '.button-list .schedule-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .baseClass-btn-confirm')

# 入库按钮
deposit_into_storage = (
    '//*[@class="button-list"]/descendant::button[child::span[text()="入库"]]')

# 入库弹框全选按钮
storage_all_choice = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .dialog-footer .baseClass-btn-next')

detail_labNub = '.vxe-table--fixed-left-wrapper table tbody tr:nth-child(1) td:nth-child(4)'

# 提交状态文本
submit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(16)')

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.dialog-check-storage .checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box .dialog-footer .baseClass-btn-confirm')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.dialog-position-box textarea')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 获取所有样本数量
all_samples = (
    '//*[@class="vxe-table--body-wrapper body--wrapper"]/descendant::tr')

# 盒内位置表单定位
position_in_box = (
    '.vxe-table--body-wrapper tr:nth-child({}) .schedule-tableCol-positionInBox ')

# 盒内位置录入框
position_in_box_input = (
    '.vxe-table--body-wrapper tr:nth-child({}) .schedule-tableCol-positionInBox  input')

# 保存结果按钮
detail_save_result = (
    '.createTask_content .baseClass-btn-save')

# 进入结果表按钮
goResult = (
    '.createTask_content .baseClass-btn-goResult')

'''
样本处理结果表元素定位
'''
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量数据按钮
batch_data = (
    '.button-list .baseClass-btn-batchData')

# 批量数据弹框，产物计量文本
product_amount = (
    '.dialogBatchData-sampleAmt input')

# 批量数据弹框，计量单位下拉框
sample_amount_unit = (
    '.dialogBatchData-sampleAmtUnit input')

# 批量数据弹框，计量单位下拉值
sample_amount_unit_choice = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[4]')

# 批量数据弹框，产物包装量文本框
sample_package_amount = (
    '.dialogBatchData-samplePkgAmt input')

# 批量数据弹框，包装单位下拉框
sampl_package_amount_unit = (
    '.dialogBatchData-samplePkgAmtUnit input')

# 批量数据弹框，包装单位下拉值
sampl_package_amount_unit_choice = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[5]')

# 批量数据弹框,标签打印份数
number_of_labels_printed = (
    '.dialogBatchData-noOfLabels input')

# 批量数据弹框，确认按钮
batch_data_comfirm = (
    '.dialog-batch-data .el-dialog__footer .baseClass-btn-confirm')

# 获取所有样本lims总数
samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(3)')

# 获取所有样本lims号
samples_lims_num = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 获取所有样本实验室号总数
samples_laboratory = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(4)')

# 获取所有样本实验室号
samples_laboratory_nub = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(4)')

# 下一步流向字段定位
result_next_step = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(11)')

# 结果表提交状态文本定位
result_sample_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(12)')

# 提交按钮
result_submit = (
    '.button-list .baseClass-btn-submit')

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseClass-btn-confirm')

# 完成任务单按钮
complete_task_btn = (
    '.createTask_content .baseClass-btn-finish')

# 返回明细表按钮
goback_detail = '.result-experiment-table-height-auto-sample .el-card__body .baseClass-btn-goBack'

# 返回上一页提示框
goback_page_info = '.el-dialog__wrapper .el-dialog__footer .baseClass-btn-continue'

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')
