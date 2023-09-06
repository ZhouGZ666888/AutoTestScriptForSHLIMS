# -*- coding: utf-8 -*-
# @Time    : 2021/12/02
# @Author  : guanzhong.zhou
# @File    : 超声破碎元素定位
# -*-*************************************************************************************-*-
'''
超声破碎首页列表元素定位
'''
# 搜索按钮
search = (
    '.app-main .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.commonTaskList-commonTaskListDialog-sampleIdLims input')

# 搜索弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-confirm')

# 新增按钮
add_sample_process_task = (
    '.app-main .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-


'''
待选表元素定位
'''
# 任务类型下拉框
task_type = (
    '.select-task-type input')

# 样本类型选择下拉值，默认第一条
task_type_choice = (
    '.task-type-unique .el-select-dropdown__list li:nth-child(1)')

# 操作方式下拉框
OperationType = '.ultrafracDetail-form-wpOperationType input'

# 操作方式下拉框下拉值
OperationType_choice ='//span[text()="人工单管"]'

# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值
select_sop_choice = (
    '.sopId-unique .el-select-group__wrap .el-select-group li:nth-child(1)')

#副操实验员编辑按钮
slaverUser_btn='.extractionDetail-btn-slaverUser'

#副操实验员录入
slaverUser_input='//*[@aria-label="副操实验员"]/descendant::input'

#副操实验员选择
slaverUser_choice='//span[text()="周官钟"]'

#副操实验员录入检索添加按钮
slaverUser_add_btn='//*[@aria-label="副操实验员"]/descendant::button[2]'

#副操实验员录入检索添加后选择
slaverUser_choice_='//*[@aria-label="副操实验员"]/descendant::div[contains(text(),"周官钟")]'

#副操实验员录入检索选择后确认
slaverUser_confirm_btn='//*[@aria-label="副操实验员"]/descendant::button[5]'


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

'''
超声破碎明细表元素定位
'''
# 样本列表数据全选按钮

# 生成排序号按钮
create_sort_number = (
    '.button-list .ultrafracSchedule-btn-sortNo')

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 列表第一条数据
first_sample = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# *****************分管**************

# 分管按钮
aliquot_sample = (
    '.button-list .ultrafracSchedule-btn-divideSample')

# 分管弹框全选按钮
aliquot_sample_all_choice = (
    '.dialog-divide-sample-data .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 分管弹框分管数文本录入
aliquot_number = (
    '.dividedDialog-dividedDialogForm-vitroNumber input')

# 分管弹框分管数文本录入后批量填入按钮
aliquot_number_batch_edit = (
    '.dividedDialog-dividedDialogBtn-batchEdit')

# 分管弹框下一步按钮
aliquot_sample_next = (
    '.dialog-divide-sample-data .dialog-footer .baseClass-btn-next')

# 封管最后步骤弹框全选
aliquot_sample_last_step_all_choice = (
    '.dialog-divided-next .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 分管弹框最后步骤下拉框
aliquot_sample_last_step = (
    '.dialog-divided-next .divided-btn-lastStep')

# 分管弹框最后步骤下拉值选择
aliquot_sample_last_step_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="上机"]')

# 修改项目信息
changeProject = (
    '.dialog-divided-next .divided-btn-changeProject')
# 修改项目信息全选按钮
changeProject_choice = (
    '.dialog-select-project .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 修改项目信息弹框确认按钮
changeProject_comfirm = (
    '.dialog-select-project .el-dialog__footer .baseClass-btn-confirm')

#样本分管选择上机平台按钮
sequencing_platform='.dialog-divided-next .divided-btn-sequencing_platform'

#样本分管选择上机平台下拉值选择
sequencing_platform_choice='//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="Illumina"]'

# 明细表分管弹框分管后确认按钮
aliquot_sample_last_step_comfirm = (
    '.dialog-divided-next .dialog-footer .baseClass-btn-confirm')

# 选择优化项目弹框全选按钮
dialog_parOpt_all_choice = (
    '.dialog-parOpt .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 选择优化项目按钮
dialog_parOpt_btn = (
    '.parOptDialog-parOptDialogBtn-selectProject1')

# 选择优化项目弹框录入
dialog_parOpt_input = (
    '.parOptDialog-parOptDialogForm-query input')

# 选择优化项目弹框搜索
dialog_parOpt_search = (
    '.dialog-parOpt-next .baseClass-btn-search')

# 选择优化项目弹框选择第一条
dialog_parOpt_choice = (
    '.dialog-parOpt-next .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# 选择优化项目弹框确定
dialog_parOpt_comfirm = (
    '.dialog-parOpt-next .dialog-footer .baseClass-btn-confirm')

# 选择优化项目外层弹框弹框确定按钮
dialog_parOpt_comfirm_comfirm = (
    '.dialog-parOpt .dialog-footer .baseClass-btn-confirm')

# *****************入库类型选择**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = '.button-list .ultrafracSchedule-btn-batchStorageType'

# 明细表批量入库类型下拉值
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

# *****************批量数据**************

# 明细表批量数据按钮
detail_batch_data = (
    '.button-list .baseClass-btn-batchData')
# 明细表批量数据，包装余量
detail_remaining_sample_package_amount = (
    '.ultrafracSchedule-dialogBatchData-remainingSamplePkgAmt input')
# 明细表批量数据，样本进入量
detail_used_sample_amount = (
    '.ultrafracSchedule-dialogBatchData-usedTotalAmt input')
# 明细表批量数据，样本进入体积
detail_sample_package_amount_unit = (
    '.ultrafracSchedule-dialogBatchData-usedVolumeAmt input')

# 明细表批量数据弹框，确认按钮
detail_batch_data_comfirm = (
    '.dialog-batchData .el-dialog__footer .baseClass-btn-confirm')

# 自动计算按钮
detail_auto_calculate = (
    '.button-list .baseClass-btn-autoComplete')

# 自动计算部分表格有值提示信息
detail_auto_calculate_info = (
    '.el-message-box__wrapper .el-message-box__btns button')

# 提交按钮
submit_btn = (
    '.sampleDetail_header .button-list .ultrafracSchedule-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer button')

# 入库按钮
deposit_into_storage = (
    '.button-list .ultrafracSchedule-btn-storage')

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

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.dialog-check-storage .checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box .dialog-footer .baseClass-btn-confirm')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.dialog-position-box textarea')

# 入库弹框样本总数
all_select_sample_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(7)')

# 入库弹框盒内位置
position_in_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7)')

# 入库弹框盒内位置文本框
position_in_box_input = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7) input')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .dialog-footer .baseClass-btn-next')

# 明细表提交状态文本定位
submit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(13)')

# 返回明细表
goback_detail = '.createTask_content  .is-justify-end .baseClass-btn-goSchedule'
# 返回明细表确认
goback_page_info = '.el-dialog__wrapper .el-dialog__footer .baseClass-btn-continue'

# 保存结果按钮
detail_save_result = (
    '.createTask .baseClass-btn-save')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask .baseClass-btn-goResult')

"""
超声破碎结果表元素定位
"""
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 修改产物类型
result_change_product_type = (
    '.sampleDetail_header .button-list .ultrafracResults-btn-changeResultType')
# 修改产物类型弹框数据选择，默认选择第一条
result_change_product_type_choice = (
    '//*[@class="el-dialog el-dialog--center dialog-product-type"]/descendant::tr[child::td[div[text()="石蜡组织DNA"]]]')
# 修改产物类型弹框数据选择，确认
result_change_product_type_comfirm = (
    '.dialog-product-type .dialog-footer .baseClass-btn-confirm')
# 修改产物类型，类型不一致提示框确认按钮
result_change_product_type_continue_comfirm = (
    '.el-dialog--center.dialog-msg .el-dialog__footer .baseClass-btn-confirm')
# *****************批量数据****************************************
# 批量数据按钮
result_batch_data = (
    '.sampleDetail_header .button-list .ultrafracResults-btn-batchData')
# 批量数据弹框，产物包装量
result_sample_package_amount = (
    '.ultrafracResults-page-samplePkgAmt input')
# 批量数据弹框，包装单位下拉框
result_sample_package_amount_unit = (
    '.ultrafracResults-page-samplePkgAmtUnit input')
# 批量数据弹框，包装单位下拉值（管 ）
result_sample_amount_unit_choice = (
    '//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/descendant::li[child::span[text()="管"]]')

# 批量数据弹框，标签打印份数文本框
result_number_of_labels_printed = (
    '.ultrafracResults-page-noOfLabels input')

# 批量数据弹框，确认按钮
result_batch_data_comfirm = (
    '.el-dialog__wrapper.dialog-batchData .el-dialog__footer .baseClass-btn-confirm')

# 获取所有样本lims号
result_samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 获取所有样本实验室号
result_samples_laboratory = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(4)')

# 盒内位置表单定位
result_position_in_box = (
    '.vxe-table--main-wrapper .vxe-table--body-wrapper tr:nth-child({}) .ultrafracResults-tableCol-positionInTmpBox  ')

# 盒内位置文本录入框定位
result_position_in_box_input = (
    '.vxe-table--main-wrapper .vxe-table--body-wrapper tr:nth-child({}) .ultrafracResults-tableCol-positionInTmpBox input')

# 选中全部样本数量,用来计总数
result_samples_for_total = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr')

# 获取样本表单文本值，进行下一步流程比对
result_samples_all = (
    '.vxe-table--main-wrapper .vxe-table--body-wrapper tr:nth-child({})')

# 结果表自动计算按钮
result_auto_calculate = (
    '.button-list .ultrafracResults-btn-autoComplete')

# 结果表自动计算提示框确认按钮
result_auto_calculate_promote = (
    '.el-message-box__wrapper .el-message-box__btns button')

# 提交按钮
result_submit = (
    '.button-list .ultrafracResults-btn-submit')

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseClass-btn-confirm')

# 结果表提交状态文本定位
result_sample_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(12)')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask_content .baseClass-btn-completeTask')

# 任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')
