# -*- coding: utf-8 -*-
# @Time    : 2021/12/07
# @Author  : guanzhong.zhou
# @File    : 文库富集元素定位
# -*-*************************************************************************************-*-
"""
文库富集首页列表元素定位
"""
# 搜索按钮
search = (
    '//*[@class="filter-container"]/descendant::button[descendant::span[text()="搜索"]]')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '//*[@aria-label="搜索"]/descendant::input[preceding-sibling::div[text()="LIMS样本号"]]')

# 搜索弹框确认
search_confirm = (
    '//*[@class="el-dialog el-dialog--center"]/div[@class="el-dialog__footer"]/descendant::button[child::span[text()="确定"]]')

# 建库电子实验记录待签字交接提示
electronic_experiment_record_signed_tips = '.el-dialog__wrapper .dialog-handover .el-dialog__footer button'

# 新增按钮
add_sample_process_task = (
    '//*[@class="filter-container"]/descendant::button[descendant::span[text()="新建"]]')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-
# 点板号：PCR-DN-220117-006
# 箱码:BX00004542
# 管码：DF0000049843
"""
待选表元素定位,
"""
# 任务描述文本录入框
task_description = (
    '.taskDetail-taskDesc input')

# 选择sop下拉框
select_sop = (
    '.select-sop-type input')

# 选择sop下拉值,m默认选择第一条
select_sop_choice = (
    '.sopId-unique .el-select-dropdown__wrap .el-select-group li:nth-child(1)')
# 选择实验室值班主管下拉框
select_dutySupervisors = (
    '.extractionDetail-form-dutySupervisors input')

# 选择实验室值班主管下拉框下拉值
select_dutySupervisors_choice = (
    '/html/body/div[last()]/div[1]/div[1]/ul/li[1]')
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

# 子SOP样本数量按钮
sopSampleNumber_btn = '.createTask_content_choose .commonTaskDetail-commonTaskDetailBtn-sopSampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber'

# 子SOP样本数量弹框录入项
sopSampleNumber_input = '.dialog-sop-sample-number .el-dialog__body .taskInitial-dividedDialogTableCol-sampleNumber input'

# 子SOP样本数量弹框确认按钮
sopSampleNumber_confirm = '.dialog-sop-sample-number .el-dialog__footer .taskInitial-form-currentStepName'

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
文库富集明细表元素定位
"""

# 列表全选按钮
detail_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 样本数据获取样本数据总数量
all_samples = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 样本数据获取样本lims号
all_sample_lims = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(2)')

# *****************入库类型选择、批量粘贴导入**************

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.button-list .enrichmentSchedule-btn-handleStorage')

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')

# 批量粘贴导入按钮
batch_paste_import_package = (
    '.button-list .enrichmentSchedule-btn-showDialogChannel')

# 批量粘贴导入弹框文本编辑框
batch_paste_import_package_textarea = (
    '.el-dialog.el-dialog--center.dialog-channel textarea')

# 明细表批量粘贴导入弹框确认按钮
batch_paste_import_package_comfirm = (
    '.el-dialog.el-dialog--center.dialog-channel .dialog-footer .qcResult-btn-confirm')
# 明细表批量粘贴导入弹框确认后index不一致提示框
batch_paste_import_package_comfirm_contiune = (
    '//*[@class="createTask schedule-experiment-table-height-auto-enrich"]/child::div[@class="el-dialog__wrapper"]/child::div[@aria-label="提示"]/child::div[@class="el-dialog__footer"]/descendant::button')

# *********************************************表单录入**********************************************
# 生成结果按钮
create_result = (
    '.schedule-experiment-table-height-auto-enrich .button-list .enrichmentSchedule-btn-handleGeneration')

# 提交按钮
submit_btn = (
    '.button-list .baseClass-btn-submit')

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

#自动判断子文库录入情况
automatic_judge_sublibrary_entry_btn='.button-list .baseClass-btn-subLibEntryStatus'




# /************************入库****************************
# 入库按钮
deposit_into_storage = (
    '.button-list .baseClass-btn-storage')

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

"""
文库富集结果表元素定位
"""
# 样本列表数据全选按钮
result_all_choice = (
    '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量导入数据按钮
result_batch_paste_import = (
    '.createTask_content .sampleDetail_header .button-list .enrichmentResults-btn-batchCopy')

# 批量粘贴导入弹框文本编辑框
result_batch_paste_import_package_textarea = (
    '.el-dialog.el-dialog--center.dialog-channel textarea')

# 明细表批量粘贴导入弹框确认按钮
result_batch_paste_import_package_comfirm = (
    '.el-dialog.el-dialog--center.dialog-channel .dialog-footer .qcResult-btn-confirm')

# 生成上机分组号
create_sequencing_group_number = (
    '.createTask_content .sampleDetail_header .button-list .enrichmentResults-btn-generateSqcNum')

# 获取所有样本lims号
result_samples_lims = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(4)')

# 获取所有样本富集名称
result_enrichment_library_name = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) '
    'td:nth-child(6)')

# 选中全部样本数量,用来计总数
result_samples_for_total = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tbody tr')

# 选中全部样本，依次获取，用来对依次获取的样本进行表单数据录入
result_samples_all = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(13)')

# 提交按钮
result_submit = (
    '.sampleDetail_header .button-list .border_size.enrichmentResults-btn-submit')

# 结果表是否已提交文本定位
result_sumbit_status = (
    '.createTask_content_table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(16)')

# 返回明细表
goback_detail = '.result-experiment-table-height-auto .baseClass-btn-goSchedule'

# 返回明细表确认
goback_page_info = '.el-dialog__wrapper .el-dialog__footer .baseClass-btn-continue'

# 提交确认按钮
result_submit_comfirm = (
    '.dialog-result-commit .dialog-footer .baseClass-btn-confirm')

# 完成任务单按钮
result_complete_task_btn = (
    '.result-experiment-table-height-auto-enrich .createTask_content .baseClass-btn-completeTask')

# 完成任务单提示弹框确认按钮
result_complete_task_comfirm = (
    '//div[@class="el-message-box__wrapper"]/descendant::button[child::span][2]')

# 任务单号
task_id = (
    '//*[@class="el-card__header"]/div/div/div[2]/span[1]')

# 明细表任务单号
detail_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 结果表任务单号
result_task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')

