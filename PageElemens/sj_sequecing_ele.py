# -*- coding: utf-8 -*-
# @Time    : 2021/12/15
# @Author  : guanzhong.zhou
# @File    : 上机元素定位
# -*-*************************************************************************************-*-
"""
上机首页列表元素定位
"""
# 搜索按钮
search = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索上机批次号
seqBatchNo = (
    '.dialogSearch-form-seqBatchNo input')

# 搜索弹框确认按钮
search_comfirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-confirm')

# 新增按钮
add_task = (
    '.app-container .filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-


"""
待选表元素定位
"""
# 任务类型
task_type = '.el-form--label-left >div:nth-child(1) input'

# 任务类型选择
task_type_choice_illumina = '//span[text()="illumina上机"]'
task_type_choice_huada = '//span[text()="华大上机"]'

# 上机批次号
sequencing_batch_number = (
    '.sequencingDetail-form-seqBatchNo input')

#芯片号
chipNo='.createTask_content_choose .sequencingDetail-form-chipNo input'


# 选择测序仪按钮
instrument = (
    '.createTask_content_choose .baseClass-btn-instrument')

# 选择测序仪弹框，选择第一条
instrument_choice = (
    '.multi-table-dialog .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')

# 选择测序仪弹框，确认按钮
instrument_comfirm = (
    '.multi-table-dialog .dialog-footer .qcResult-btn-confirm')

# 运行模式
runningMode = (
    '.sequencingDetail-form-runningMode input')

# 运行模式选择第一条
runningMode_choice = (
    '.running-mode-unique .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

# 实际上机时间
seqStartTime = (
    '.sequencingDetail-form-seqStartTime input')

# 任务描述
task_des = (
    '.sequencingDetail-form-taskDesc input')

# 选择浓度调整SOP弹框按钮
select_concentration_adjusted_sop = (
    '.sequencingDetail-form-adjustedSopId input')

# 选择浓度调整SOP,默认选第一条
select_concentration_adjusted_sop_choice = (
    '.adjusted-sop-unique .el-scrollbar__view.el-select-dropdown__list ul:nth-child(1) .el-select-group li:nth-child(1)')

# 选择上机SOP
select_sequecing_sop = (
    '.sequencingDetail-form-sopId input')

# 选择上机SOP,默认第二条(避免与选择浓度调整SOP重复)
select_sequecing_sop_choice = (
    '.sop-id-unique .el-scrollbar__view.el-select-dropdown__list ul:nth-child(1) .el-select-group li:nth-child(2)')

# 浓度调整实验员输入框
concentration_adjustment_laboratory_personnel = (
    '.sequencingDetail-form-adjustExperimenter input')

# 浓度调整实验员选择
concentration_adjustment_laboratory_personnel_choice = (
    '.experimenter-adjust-unique .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

# 上机实验员输入框
sequencing_laboratory_personnel = (
    '.sequencingDetail-form-experimenter input')

# 上机实验员选择
sequencing_laboratory_personnel_choice = (
    '.experimenter-id-unique .el-scrollbar__view.el-select-dropdown__list li:nth-child(1)')

# 样本lims号表单定位
lims_number = '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child({}) td:nth-child(2)'
lims_numbers = (
    '//*[@class="createTask_content_table"]/descendant::div[@class="vxe-table--main-wrapper"]/div[@class="vxe-table--body-wrapper body--wrapper"]/descendant::tbody/tr/td[descendant::span[text()="{}"]]')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-submit')

# 点击子SOP样本数量按钮,浓度调整SOP
sopSampleNumber1 = '.createTask_content_choose  div:nth-child(10) .commonTaskDetail-commonTaskDetailBtn-sopSampleNumber'

# 点击子SOP样本数量按钮,上机SOP
sopSampleNumber2 = '.createTask_content_choose  div:nth-child(13) .commonTaskDetail-commonTaskDetailBtn-sopSampleNumber'

# 子SOP样本数量弹框全选按钮
sopnub_all_choice = '.dialog-sop-sample-number .el-dialog__body .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 子SOP批量样本数量
showEProVisible = '.dialog-sop-sample-number .taskInitial-btn-showEProVisible'

# 子sop批量样本数量录入
sopsampleNumInput = '.dialog-sample-number input'

# 子sop批量样本数量录入后确认
sopsampleNumInput_confirm = '.dialog-sample-number .baseClass-btn-confirm'

# 子SOP样本数量弹框确认按钮
sopSampleNumber_confirm = '.dialog-sop-sample-number .taskInitial-form-currentStepName'

# 进入明细表按钮，元素定位
enter_detail_list_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

"""
上机明细表浓度调整前元素定位
"""
# 待选列表全选按钮
before_concentration_adjustment_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 浓度调整前自动计算按钮
before_concentration_adjustment_auto_calculate = (
    '.sampleDetail_header .button-list .border_size.baseClass-btn-autoComplete')

# 浓度调整前生成结果按钮
before_concentration_adjustment_create_concentration_adjustment_result = (
    '.sampleDetail_header .button-list .border_size.sequencingPreResult-btn-generationBefore')

# 浓度调整前提交按钮
before_concentration_adjustment_submit = (
    '.sampleDetail_header .button-list .border_size.baseClass-btn-submit')

# 浓度调整前提交确认按钮
before_concentration_adjustment_submit_comfirm = (
    '.dialog-commit-confirm .dialog-footer .qcResult-btn-confirm')

# 浓度调整前下一步按钮
before_concentration_adjustment_next = (
    '.createTask_content .baseClass-btn-next')

# 提交状态表单定位
before_concentration_sumbit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(12)')

# /************************入库******************************************************************************

# 浓度调整前入库按钮
before_concentration_adjustment_deposit_into_storage = (
    '.sampleDetail_header .button-list .border_size.sequencingPreResult-btn-storage')

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

# *****************分管******************************************************************************************

# # 分管按钮
# aliquot_sample = (
#     '//button[@class="el-button border_size ultrafracSchedule-btn-divideSample el-button--primary el-button--mini" and child::span[text()="Aliquot sample"]]')
# # 分管弹框全选按钮
# aliquot_sample_all_choice = (
#     '//*[@class="el-dialog el-dialog--center dialog-divided dialog-divide-sample-data"]/descendant::span[preceding-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--checked-icon"] and parent::span[@title="vxe.table.allTitle"] and following-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--indeterminate-icon"]]')
# # 分管弹框分管数文本录入
# aliquot_number = (
#     '//*[@class="dividedDialog-dividedDialogForm-vitroNumber el-input el-input--small el-input-group el-input-group--prepend"]/descendant::input')
# # 分管弹框分管数文本录入后批量填入按钮
# aliquot_number_batch_edit = (
#     '//*[@class="el-button dividedDialog-dividedDialogBtn-batchEdit el-button--primary el-button--small" and child::span[text()="batch edit"]]')
# # 分管弹框下一步按钮
# aliquot_sample_next = (
#     '//*[@class="el-dialog el-dialog--center dialog-divided dialog-divide-sample-data"]/descendant::button[preceding-sibling::button[child::span[text()="cancel"]]]')
#
# # 封管最后步骤弹框全选
# aliquot_sample_last_step_all_choice = (
#     '//*[@class="el-dialog el-dialog--center dialog-divided-next"]/descendant::span[preceding-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--checked-icon"] and parent::span[@title="vxe.table.allTitle"] and following-sibling::span[@class="vxe-checkbox--icon vxe-checkbox--indeterminate-icon"]]')
#
# # 分管弹框最后步骤下拉框
# aliquot_sample_last_step = (
#     '//button[@class="el-button border_size el-button--primary el-button--mini el-dropdown-selfdefine " and descendant::span]')
#
# # 分管弹框最后步骤下拉值选择
#
# # 明细表分管弹框分管后确认按钮
# aliquot_sample_last_step_comfirm = (
#     '//*[@aria-label="Aliquot sample"]/descendant::button[child::span[text()="comfirm"]]')


"""
上机浓度调整后样本明细元素定位
"""
# *****************入库类型选择、批量粘贴导入**************

# 浓度调整后明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.sampleDetail_header .button-list .sequencingResults-btn-batchStorageType')

# 浓度调整后明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

# 浓度调整后明细表数据全选按钮
after_concentration_adjustment_all_choice = (
    '.vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 浓度调整后明细表填入上机信息
after_concentration_adjustment_enter_sequencing_information = (
    '.sampleDetail_header .button-list .sequencingResults-btn-showDialogUseComputer')

# 浓度调整后明细表批量数据
after_concentration_adjustment_datch_data = (
    '.sampleDetail_header .button-list .sequencingResults-btn-batchData')

# 浓度调整后明细表批量数据
hd_detail_adjustment_datch_data = (
    '.sampleDetail_header .button-list .sequencingSchedule-btn-batchData')

# 华大选择FC代码下拉框
ha_showFC = '.sampleDetail_header .button-list .sequencingSchedule-btn-showFC'

#华大自动计算标签
hd_autoCompleteLabel='.sampleDetail_header .button-list .baseClass-btn-autoCompleteLabel'

#华大生成上机分组号
hd_generateNo='.sampleDetail_header .button-list .sequencingSchedule-btn-generateNo'

#华大上机确认上机按钮
hd_sequencingSchedule_confirm='.sampleDetail_header .button-list .sequencingSchedule-btn-confirm'

#华大上机生成samplesheet
hd_sequencingSchedule_sampleSheet='.sampleDetail_header .button-list .sequencingSchedule-btn-sampleSheet'

#华大上机提交
hd_detail_sumbit='.sampleDetail_header .button-list .baseClass-btn-submit'

#华大上机提交确认
hd_detail_sumbit_confirm='.dialog-commit-confirm .qcResult-btn-confirm'

# 华大选择FC代码
ha_showFC_choice = '//li[text()="A"]'

#华大结果表添加条目
hd_result_add_tips='.createTask_content_1 .qcResult-btn-add'

#华大结果表完成任务单
hd_result_complete_task='.baseClass-btn-completeTask'

# 浓度调整后明细表批量数据,耗用量录入
after_concentration_adjustment_datch_data_used_amount = (
    '.dialogSequenceData-dialogSequenceDataForm-seqUsedVolumeAmt input')

# 浓度调整后明细表批量数据,测序读长
after_concentration_adjustment_datch_data_sequencer_read_length = (
    '.dialogSequenceData-dialogSequenceDataForm-seqReadLen input')

# 浓度调整后明细表批量数据弹框确认
after_concentration_adjustment_datch_data_comfirm = (
    '.dialog-sequence-data .el-dialog__footer .baseClass-btn-confirm')

# 浓度调整后明细表生成上机分组号
after_concentration_adjustment_create_sequencing_group_number = (
    '.sampleDetail_header .button-list .sequencingResults-btn-generateNo')

# 浓度调整后明细表自动计算
after_concentration_adjustment_auto_calculate = (
    '.sampleDetail_header .button-list .baseClass-btn-autoComplete')

# 浓度调整后明细表确认上机
after_concentration_adjustment_confirm_sequencing = (
    '.sampleDetail_header .button-list .sequencingResults-btn-confirm')

# 浓度调整后明细表生成Samplesheet按钮
after_concentration_adjustment_create_samplesheet = (
    '.sampleDetail_header .button-list .sequencingResults-btn-sampleSheet')

# 浓度调整后明细表生成Samplesheet弹框选择模板（默认【Hiseq4000 | Hiseq X | Novaseq XP模式双标签】）
after_concentration_adjustment_create_samplesheet_choice = (
    '//div[contains(text(),"XP模式双标签")]')

# 华大上机选择模版
hd_create_samplesheet_choice = (
    '//div[contains(text(),"华大T7标准模式双标签")]')

# 浓度调整后明细表生成Samplesheet弹框确认按钮
after_concentration_adjustment_create_samplesheet_comfirm = (
    '.dialog-sample-sheet .el-dialog__footer .qcResult-btn-confirm')

# 浓度调整后明细表生成Samplesheet后提示框确认按钮
after_concentration_adjustment_create_samplesheet_info_comfirm = (
    '.dialog-sampleSheet-msg .el-dialog__footer .qcResult-btn-confirm')

# 浓度调整后明细表保存
after_concentration_adjustment_save = (
    '.createTask .baseClass-btn-save')

# 浓度调整后明细表提交
after_concentration_adjustment_submit = (
    '.sampleDetail_header .button-list .baseClass-btn-submit')

# 浓度调整后明细表提交确认按钮
after_concentration_adjustment_submit_comfirm = (
    '.dialog-commit-confirm .dialog-footer .qcResult-btn-confirm')

# 浓度调整后明细表入库
after_concentration_adjustment_deposit_into_Storage = (
    '.sampleDetail_header .button-list .sequencingResults-btn-storage')

# 提交状态表单定位
after_concentration_sumbit_status = (
    '.vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(15)')

# 浓度调整后明细表进入结果表按钮
after_concentration_adjustment_submit_enter_the_result_list = (
    '.createTask .baseClass-btn-goResult')

# **************************************************************************#
#                                                                           #
#                                                                           #
#                                                                           #
#                          结果表                                            #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
# **************************************************************************#
# 结果表上传结果按钮
result_submit_result_btn = (
    '.createTask .qcResult-btn-importResult')

# 结果表上传结果弹框上传标签
result_samples_number = (
    '.dialog-upload .el-dialog__body .upload-demo input')

# 结果表上传结果弹框导入后上传按钮
result_samples_upload = (
    '.dialog-upload .el-dialog__footer .baseClass-btn-upload')

# 完成任务单按钮
result_complete_task_btn = (
    '.createTask .is-justify-end .baseClass-btn-completeTask')

# 浓度调整前明细表任务单号
before_concentration_detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 浓度调整后明细表任务单号
after_concentration_detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')
