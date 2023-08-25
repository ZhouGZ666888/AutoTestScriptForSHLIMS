# -*- coding: utf-8 -*-
# @Time    : 2023/08/08
# @Author  : guanzhong.zhou
# @File    : 环化后混合页面元素定位
# -*-*************************************************************************************-*-
"""
环化后混合首页列表元素定位
"""
# lims号检索文本录入框
lims_input = '.common-list-sampleIdLims input'

# 查询按钮
search_btn = '.search-list .baseClass-btn-search'

# 新建任务单按钮
add_task = '.table-list .baseClass-btn-add'

# 页面列表样本
sample_page_list = '//*[@class="sample_receive_detail"]/descendant::tbody/tr'

"""
环化后混合待选表列表元素定位
"""
# 选择sop下拉框
sop_btn = '.select-sop-type input'

# 选择sop下拉框值
sop_choice = '.sopId-unique .el-select-dropdown__wrap >ul >ul:nth-child(1) .el-select-group li:nth-child(1)'

# 任务描述文本框
task_des = '.commonTaskDetail-taskDesc input'

# 备注
desc = '.commonTaskDetail-remarks textarea'

# 核对LIMS号按钮
check_lims_sample_num = '.btn-right .commonTaskDetail-btn-judgeLims'

# 核对LIMS号文本弹框
check_lims_sample_number_textarea = '.dialog-check-sampleIdLims textarea'

# 核对LIMS号文本弹框确认
check_lims_sample_number_confirm = '.dialog-check-sampleIdLims .dialog-footer .baseClass-btn-confirm'

# 待选列表全选按钮
all_choice = '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = '.head-list .baseClass-btn-save'

# 进入明细表按钮，元素定位
enter_detail_list_btn = '.head-list .baseClass-btn-goSchedule'

# 页面成功提示信息
page_success_info = '//*[@class="el-message el-message--success"]/descendant::p'

"""
环化后混合明细表列表元素定位
"""
# 明细表全选按钮
detail_all_choice = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

detail_part_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--indeterminate-icon'

# 明细表选择第一条样本进行分管操作
detail_choice_one_sample = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tr:nth-child(1) td:nth-child(2)'

# 明细表分管按钮
detail_aliquot_sample = '.button-list .baseClass-btn-divide'

# 明细表样本分管弹框全选按钮
aliquot_sample_all_choice = '.common-task-schedule-new .rtl .el-drawer__body .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 明细表样本分管弹框选择分管数量按钮
aliquot_sample_numb = '.divided-drawer-class .baseClass-btn-chooseNum'

# 明细表分管弹框选择分管数量文本录入按钮
aliquot_sample_numb_choice = '.batch-divided .el-input-number__increase'

# 明细表分管弹框选择分管数量确认按钮
aliquot_sample_numb_confirm = '.batch-divided .batch-divided-confirm'

# 明细表分管弹框完成按钮
aliquot_sample_next_step_finsh = '.divided-drawer-class .baseClass-btn-confirm'

# 混合后环化产物明细表总样本数
postcyclmixSchedule_detail_all='.postcyclmixSchedule-tableCol-postcyclmixName'

#混合后环化产物名称表单
postcyclmixSchedule='.vxe-table--body-wrapper tr:nth-child({}) .postcyclmixSchedule-tableCol-postcyclmixName'

#混合后环化产物名称表单录入
postcyclmixSchedule_input='.vxe-table--body-wrapper tr:nth-child({}) .postcyclmixSchedule-tableCol-postcyclmixName input'

# 明细表生成产物按钮
detail_generate_product_btn = '.button-list .baseClass-btn-generate'

# 明细表生成产物弹框确认按钮
generate_product_confirm = '.dialog .el-dialog--center .baseClass-btn-continue'

#明细表批量数据按钮
detail_batch_data_btn='.button-list .baseClass-btn-batch'

# 明细表批量包装余量文本录入框
detail_remaining_sample_pkg_amt_input = '.expPostcyclmixSchedule-formBatchData-remainingSamplePkgAmt input'


# 明细表批量入库类型下拉框
detail_batch_storage_type = '.expPostcyclmixSchedule-formBatchData-depositType input'

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = '//span[text()="余样入库"]'

# 明细表批量数据确认按钮
detail_batch_data_btn_confirm = '.edit-batch-remainingSamplePkgAmt .el-dialog__footer .baseClass-btn-confirm'

# 明细表入库按钮
deposit_into_storage = '.button-list .baseClass-btn-deposit'

# 入库弹框全选按钮
storage_all_choice = '.deposit-drawer .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 入库弹框选择样本盒按钮
batch_paste_sample_box = '.deposit-drawer .deposit-btn-chose-sample-box'

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = '.deposit-drawer .boxSearch-boxName input'

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = '.deposit-drawer .boxSearch-btn-search'

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = '.deposit-drawer .el-table .el-table__body-wrapper tbody tr:nth-child(1)'

# 入库弹框选选择样本盒弹框，确认按钮
select_sample_box_comfirm = '//*[@aria-label="选择样本盒"]/descendant::div[@class="dialog-footer"]/button[2]'


# 批量粘贴盒内位置
batch_copy_BoxPosition_btn = '//span[text()="批量粘贴盒内位置"]'

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = '.dialog-positionBoxCopy .dialog-footer .baseClass-btn-confirm'

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = '.dialog-positionBoxCopy textarea'

# 入库弹框下一步按钮
storage_next = '//*[@aria-label="填写入库信息"]/descendant::div[@class="dialog-footer"]/button[2]'

# 明细表提交按钮
detail_commit = '.button-list .baseClass-btn-commitSample'

# 明细表提交确认提示
detail_commit_confirm = '.dialog-commit .baseClass-btn-confirm'

#明细表提交状态
detail_commit_status=''

# 明细表自动计算按钮
detail_autoComplete_btn = '.button-list .btn-first'

# 明细表保存按钮
detail_save = '.head-list .postcyclmixSchedule-btn-saveResult'

# 明细表进入结果表按钮
detail_enter_result = '.head-list .postcyclmixSchedule-btn-goResults'

# 明细表任务单号
detail_task_id='.header_test'
"""
环化后混合结果表列表元素定位
"""
# 结果表全选按钮
result_all_choice='.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 结果表自动计算按钮
result_autoComplete='.button-list .baseClass-btn-auto-complete'

# 结果表自动计算规则不完整提示
result_autoComplete_tip='.el-message-box__wrapper .el-message-box__btns button'

# 结果表提交样本按钮
result_commit='.button-list .postcyclmixResult-btn-commitSample'
#结果表提交状态
submitType='tr:nth-child(1) .postcyclmixResult-col-isSubmit'
# 结果表提交样本确认弹框按钮
result_commit_confirm='.dialog-result-commit .baseClass-btn-confirm'

# 结果表任务状态
result_task_status='.head-list .el-button--warning'

#结果表任务单号
result_task_id='.header_test'

# 结果表保存按钮
result_save='.head-list .postcyclmixResult-btn-saveResult'

# 结果表完成任务单按钮
result_complete_task_btn='.head-list .postcyclmixResult-btn-completeTask'

# 结果表完成任务单确认按钮
result_complete_task_confirm_btn='.el-message-box__wrapper .el-message-box__btns button:nth-child(2)'

# 结果表返回明细表按钮
result_return_detail='.head-list .postcyclmixResult-btn-backToSchedule'

# 结果表返回明细表确认
result_return_detail_confirm='.dialog-back .baseClass-btn-continue'