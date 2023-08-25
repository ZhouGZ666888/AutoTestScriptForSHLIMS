# -*- coding: utf-8 -*-
# @Time    : 2021/12/08
# @Author  : guanzhong.zhou
# @File    : 文库定量元素定位
# -*-*************************************************************************************-*-
"""
文库定量首页列表元素定位
"""
# 搜索按钮
search = (
    '.filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.dialogSearch-form-poolingName input')

# 搜素弹框确认
search_confirm = (
    '.dialog-search .dialog-footer .baseClass-btn-confirm')

# 新增按钮
add_sample_process_task = (
    '.filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

electronic_experiment_record_signed_tips = '.el-dialog__wrapper .dialog-handover .el-dialog__footer button'

# -*-*************************************************************************************-*-


"""
待选表元素定位
"""
# 定量类型下拉框
quantification_type = (
    '.select-task-type input')

# 定量类型下拉值选择，单梯度定量
quantification_type_choice = (
    '//*[@class="el-select-dropdown el-popper task-type-unique"]/descendant::li[child::span[text()="单梯度定量"]]')

# 任务描述文本录入框
task_description = (
    '.taskDetail-taskDesc input')

# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值,m默认选择第一条
select_sop_choice = (
    '.sopId-unique .el-select-dropdown__wrap.el-scrollbar__wrap .el-select-group li:nth-child(1)')

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

# 子SOP样本数量按钮
sopSampleNumber_btn = '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-sopSampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber_input = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber input'

# 子SOP样本数量弹框确认按钮
sopSampleNumber_confirm = '.dialog-sop-sample-number .el-dialog__footer .taskInitial-form-currentStepName'

"""
文库定量明细表元素定位
"""

# 列表全选按钮
detail_all_choice = (
    '.normal-table .createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 列表全选按钮(存在有部分数据被选中的情况下)
detail_all_choice2 = (
    '.normal-table .createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--indeterminate-icon')

# 样本数据获取样本数据总数量
detail_all_samples = (
    '.normal-table .createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 样本数据获取样本lims号
all_sample_lims_number = (
    '.normal-table .createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-chlid({})')

# 样本数据获取样本富集名称
enrichment_name = (
    '.normal-table .createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 样本数据获取样本上机分组号
all_Sequencing_group_number = (
    '.normal-table .createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) .libquantSchedule-tableCol-sqcGroupNum')

#  余样包装量表单
remaining_sample_package_amount = (
    '//*[@class="createTask_content_table quantification-sample-list"]/descendant::tr[{}]/td[13]')

#  余样包装量表单录入
remaining_sample_package_amount_input = (
    '//*[@class="createTask_content_table quantification-sample-list"]/descendant::tr[{}]/td[13]/div/div/input')
# *****************分管**************

# 分管按钮
aliquot_sample = (
    '//button[@class="el-button border_size ultrafracSchedule-btn-divideSample el-button--primary el-button--mini" and child::span[text()="Aliquot sample"]]')

# 分管弹框全选按钮
aliquot_sample_all_choice = (
    '//*[@class="el-dialog el-dialog--center dialog-divided dialog-divide-sample-data"]/descendant::span[preceding-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--checked-icon"] and parent::span[@title="vxe.table.allTitle"] and following-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--indeterminate-icon"]]')

# 分管弹框分管数文本录入
aliquot_number = (
    '//*[@class="dividedDialog-dividedDialogForm-vitroNumber el-input el-input--small el-input-group el-input-group--prepend"]/descendant::input')

# 分管弹框分管数文本录入后批量填入按钮
aliquot_number_batch_edit = (
    '//*[@class="el-button dividedDialog-dividedDialogBtn-batchEdit el-button--primary el-button--small" and child::span[text()="batch edit"]]')

# 分管弹框下一步按钮
aliquot_sample_next = (
    '//*[@class="el-dialog el-dialog--center dialog-divided dialog-divide-sample-data"]/descendant::button[preceding-sibling::button[child::span[text()="cancel"]]]')

# 封管最后步骤弹框全选
aliquot_sample_last_step_all_choice = (
    '//*[@class="el-dialog el-dialog--center dialog-divided-next"]/descendant::span[preceding-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--checked-icon"] and parent::span[@title="vxe.table.allTitle"] and following-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--indeterminate-icon"]]')

# 分管弹框最后步骤下拉框
aliquot_sample_last_step = (
    '//button[@class="el-button border_size el-button--primary el-button--mini el-dropdown-selfdefine " and descendant::span]')

# 分管弹框最后步骤下拉值选择

# 明细表分管弹框分管后确认按钮
aliquot_sample_last_step_comfirm = (
    '//*[@aria-label="Aliquot sample"]/descendant::button[child::span[text()="comfirm"]]')

# *****************入库类型选择、批量粘贴导入**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    'div.el-card__body > div.createTask_content > div.sampleDetail_header > div.button-list> div:nth-child(5) > button')

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

# ****************************SR数据批量导入********************************************
# sr数据导入按钮
sr_data_batch_paste_import = (
    '.sampleDetail_header .button-list .libquantSchedule-btn-srCopy')

# sr数据导入文本框
sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# sr数据导入弹框确认按钮
sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# ****************************非SR数据批量导入*******************************************
# 非sr数据导入按钮
non_sr_data_batch_paste_import = (
    '.sampleDetail_header .button-list .libquantSchedule-btn-noSrCopy')

# 非sr数据导入文本框
non_sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# 非sr数据导入弹框确认按钮
non_sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# *******单梯度***********************************************
# *******单梯度***********************************************
# *******单梯度***********************************************
# *******单梯度***********************************************
# *******单梯度***********************************************
# *******单梯度***********************************************
# *******单梯度***********************************************
# 单梯度sr数据导入按钮
single_gradientsr_data_batch_paste_import = (
    '.single-card .createTask_content .libquantSchedule-btn-srCopy')

# 单梯度sr数据导入文本框
single_gradientsr_sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# 单梯度sr数据导入弹框确认按钮
single_gradientsr_sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# *******单梯度***********************************************

# 单梯度非sr数据导入按钮
single_gradientsr_non_sr_data_batch_paste_import = (
    '.single-card .createTask_content .libquantSchedule-btn-noSrCopy')

# 单梯度非sr数据导入文本框
single_gradientsr_non_sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# 单梯度非sr数据导入弹框确认按钮
single_gradientsr_non_sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# ******************************其他表单数据录入******************************************************

# 批量选择样本按钮
batch_select_sample = (
    '.sampleDetail_header .button-list .baseClass-btn-batchSelect')

# 批量选择样本弹框录入文本框
batch_select_sample_input = (
    '.dialog-input-lims .batch-sample-textarea textarea')

# 批量选择样本弹框录入文本框确认按钮
batch_select_sample_comfirm = (
    '.dialog-input-lims .dialog-footer .qcResult-btn-confirm')

# 选择测序仪按钮
select_sequencer = (
    '.sampleDetail_header .button-list .libquantSchedule-btn-showInstrumentId')

# 选择测序仪弹框，选择第一条数据
select_sequencer_choice = (
    '.multi-table-dialog .el-dialog__body .dialog-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# 选择测序仪弹框确认按钮
select_sequencer_comfirm = (
    '.multi-table-dialog .dialog-footer .qcResult-btn-confirm')

# 选择FC代码下拉框
select_fc_code = (
    '.sampleDetail_header .button-list .libquantSchedule-btn-showFC')

# 选择FC代码下拉值
select_fc_code_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="A"]')

# 填入上机信息
sequencing_information = (
    '.sampleDetail_header .button-list .libquantSchedule-btn-showDialogUseComputer')

# 填入上机信息,上机日期录入框
estimated_sequencing_date = (
    '.dialogUseComputer-form-estimatedSqcTime input')

# 填入上机信息，预设lane号文本框
preset_lane_number = (
    '.dialogUseComputer-form-preinstallLaneNum input')

# 填入上机信息弹框确认按钮
sequencing_information_comfirm = (
    '.batch-edit-dialog .dialog-footer .el-button--primary')

# 自动计算按钮
auto_calculate = (
    '.sampleDetail_header .button-list .baseClass-btn-autoComplete')

# 生成上机分组号按钮
create_sequencing_group_number = (
    '.button-list .libquantSchedule-btn-generateNo')

# 生成结果按钮
create_result = (
    '.button-list .libquantSchedule-btn-generate')

# 明细表提交按钮
detail_submit = (
    '.sampleDetail_header .button-list .baseClass-btn-submit')

# 明细表提交按钮确认按钮
detail_submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# /************************入库****************************
# 入库按钮
deposit_into_storage = (
    '.button-list .libquantSchedule-btn-storage')

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

# 提交状态文本定位
detail_sumbit_status = (
    '.createTask_content .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(14)')

# 样本列表滚动条
scroll_line = (
    '//*[@class="vxe-table--border-line"]')

# 保存结果按钮
detail_save_result = (
    '.createTask .baseClass-btn-save')

# 进入结果表按钮
enter_result_list_btn = (
    '.createTask .baseClass-btn-goResult')

"""
文库定量结果表元素定位
"""
# 样本列表数据全选按钮
result_all_choice = (
    '.normal-table  .createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 结果表sr数据导入按钮
result_sr_data_batch_paste_import = (
    '.sampleDetail_header .button-list .libquantResults-btn-srCopy')

# sr数据导入文本框
result_sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# sr数据导入弹框确认按钮
result_sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# 非sr数据导入按钮
result_non_sr_data_batch_paste_import = (
    '.sampleDetail_header .button-list .libquantResults-btn-noSrCopy')

# 非sr数据导入文本框
result_non_sr_data_batch_paste_import_input = (
    '.dialog-channel .el-input--medium textarea')

# 非sr数据导入弹框确认按钮
result_non_sr_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# 获取所有样本上机分组号号
result_samples_group_number = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 获取所有样本lims号
result_samples__number = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(2)')

# 获取总样本
result_all_sample = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 获取下一步流程文本
next_step = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(12)')

# 标准品批量导入按钮
result_standard_sample_import_btn = (
    '.standard-card .button-list .enrichmentResults-btn-batchCopy')

# 标准品批量导入弹框文本
result_standard_sample_data_batch_paste_import_input = (
    '.dialog-channel .el-dialog__body textarea')

# 标准品批量导入弹框确认按钮
result_standard_sample_data_batch_paste_import_comfirm = (
    '.dialog-channel .el-dialog__footer .qcResult-btn-confirm')

# 保存按钮
result_save = (
    '.createTask .menu .baseClass-btn-save')

# 提交按钮
result_submit = (
    '.sampleDetail_header .button-list .libquantResults-btn-submit')

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseClass-btn-confirm')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask .menu .baseClass-btn-completeTask')

# 返回明细表
goback_detail = '.createTask .baseClass-btn-goSchedule'

# 返回明细表确认
goback_page_info = '.dialog-goBack .el-dialog__footer .baseClass-btn-continue'

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')
