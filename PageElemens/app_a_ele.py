# -*- coding: utf-8 -*-
# @Time    : 2023/08/08
# @Author  : guanzhong.zhou
# @File    : AAP-A页面元素定位
# -*-*************************************************************************************-*-
"""
AA-A首页列表元素定位
"""
# lims号检索文本录入框
lims_input = '.sample_receive_detail .el-table__body-wrapper tbody tr:nth-child(1) td:nth-child(4)'

# 查询按钮
search_btn = '.search-list .search-list-btns .el-button--primary'

# 新建任务单按钮
add_task = '.table-list .table-header button'

# 页面列表样本
sample_page_list = '//*[@class="sample_receive_detail"]/descendant::tbody/tr'

"""
AA-A待选表列表元素定位
"""
# 选择sop下拉框
sop_btn = '.task_info_form >form >div >div:nth-child(1) input'

# 选择sop下拉框值
sop_choice = '//*[@class="el-select-dropdown el-popper"]/descendant::span[text()="APP-A"]'

# 任务描述文本框
task_des = '.task_info_form >form >div >div:nth-child(3) input'

# 备注
desc = '.task_info_form >form >div >div:nth-child(4) textarea'

# 核对LIMS号按钮
check_lims_sample_num = '.task_info_form .body-btns .btn-right button:nth-child(2)'

# 核对LIMS号文本弹框
check_lims_sample_number_textarea = '.el-dialog--center textarea'

# 核对LIMS号文本弹框确认
check_lims_sample_number_confirm = '//*[@aria-label="核对LIMS样本号"]/descendant::button[4]'

# 待选列表全选按钮
all_choice = '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = '.head-list button:nth-child(1)'

# 进入明细表按钮，元素定位
enter_detail_list_btn = '.head-list button:nth-child(2)'

# 页面成功提示信息
page_success_info = '//*[@class="el-message el-message--success"]/descendant::p'

"""
AA-A明细表列表元素定位
"""
# 明细表全选按钮
detail_all_choice = '.createTask_content .show--head .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 明细表选择第一条样本进行分管操作
detail_choice_one_sample = '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--body-wrapper tr:nth-child(1) td:nth-child(2)'

# 明细表分管按钮
detail_aliquot_sample = '//span[text()="样本分管"]'

# 明细表样本分管弹框全选按钮
aliquot_sample_all_choice = '.common-task-schedule-new .rtl .el-drawer__body .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 明细表样本分管弹框选择分管数量按钮
aliquot_sample_numb = '//span[text()="选择分管数量"]'

# 明细表分管弹框选择分管数量文本录入按钮
aliquot_sample_numb_choice = '.batch-divided .el-input-number__increase'

# 明细表分管弹框选择分管数量确认按钮
aliquot_sample_numb_confirm = '.common-task-schedule-new >div:nth-child(4) .el-dialog__footer .el-button--primary'

# 明细表分管弹框下一步填写分管信息按钮
aliquot_sample_next_step = '//span[text()="下一步填写分管信息"]'

# 明细表分管弹框下一步填写分管信息弹框全选按钮
aliquot_sample_next_step_all_choice = '.common-task-schedule-new >div:nth-child(4) >div:nth-child(3) .divided-drawer .el-drawer__body .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 明细表分管弹框下一步填写分管信息弹框最后步骤下拉框
aliquot_sample_next_step_choice = '//span[text()=" 最后步骤 "]'

# 明细表分管弹框下一步填写分管信息弹框最后步骤下拉框选择下拉值
aliquot_sample_next_step_choice_value = '//body/ul[2]/li[1]'

# 明细表分管弹框下一步填写分管信息完成按钮
aliquot_sample_next_step_finsh = '//span[text()="完 成"]'

# 明细表生成产物按钮
detail_generate_product = '.button-list .btn-row-btns button:nth-child(2)'

# 明细表生成产物弹框全选按钮
detail_generate_product_all_choice = '.common-task-schedule-new >div:nth-child(5) >div:nth-child(1) .divided-drawer ' \
                                     '.el-drawer__body .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'

# 明细表生成产物弹框批量生成产物数量按钮
detail_generate_product_numb_btn = '//span[text()="批量生成产物数量"]'

# 明细表生成产物弹框批量生成产物数量录入框
detail_generate_product_numb_input=''

# 明细表生成产物弹框批量生成产物数量确认按钮
generate_product_numb_confirm = '.common-task-schedule-new >div:nth-child(5) .el-dialog__footer .el-button--primary'

# 明细表生成产物弹框确认按钮
generate_product_confirm = ''

# 明细表批量包装余量按钮
detail_remaining_sample_pkg_amt = ''

# 明细表批量包装余量文本录入框
detail_remaining_sample_pkg_amt_input = ''

# 明细表批量包装余量文本录入确认按钮
detail_remaining_sample_pkg_amt_confirm = ''

# 明细表批量入库类型下拉框
detail_batch_storage_type = ''

# 明细表批量入库类型下拉值,选余样入库
detail_batch_storage_type_choice = '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]'

# 明细表入库按钮
deposit_into_storage = ''

# 入库弹框全选按钮
storage_all_choice = '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon'

# 入库弹框选择入库类型下拉框
target_storage_type = '.dialog-check-storage .checkStorageDialog-btn-targetLocation'

# 入库弹框选择入库类型下拉值（临时库）
target_storage_type_value = '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库"]'

# 入库弹框选择样本盒按钮
batch_paste_sample_box = '.dialog-check-storage .checkStorageDialog-btn-selectBox'

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = '.boxSearch-boxSearchDialogForm-boxName input'

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = '.dialog-box-search .baseClass-btn-search'

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = '.dialog-box-search .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)'

# 入库弹框选选择样本盒弹框，确认按钮
select_sample_box_comfirm = '.dialog-box-search .dialog-footer .baseClass-btn-confirm'

# 入库弹框样本总数
all_select_sample_box = '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(7)'

# 入库弹框盒内位置
detail_position_in_box = '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7)'

# 入库弹框盒内位置文本框
detail_position_in_box_input = '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7) input'

# 批量粘贴盒内位置
batch_copy_BoxPosition = '.dialog-check-storage .checkStorageDialog-btn-batchCopyBoxPosition'

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = '.dialog-position-box .dialog-footer .baseClass-btn-confirm'

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = '.dialog-position-box textarea'

# 入库弹框下一步按钮
storage_next = '.dialog-check-storage .dialog-footer .baseClass-btn-next'

# 明细表提交按钮
detail_commit = ''

#明细表提交状态
detail_commit_status=''

# 明细表自动计算按钮
detail_autoComplete = ''

# 明细表批量粘贴导入按钮
detail_batch_paste_import_package = ''

# 明细表批量粘贴导入弹框文本录入框
detail_batch_paste_import_package_input = ''

# 明细表批量粘贴导入弹框确定按钮
detail_batch_paste_import_package_input_confirm = ''

# 明细表保存按钮
detail_save = ''

# 明细表进入结果表按钮
detail_enter_result = ''


"""
AA-A结果表列表元素定位
"""
# 结果表全选按钮
result_all_choice=''

# 结果表生成AAP-A产物名称按钮
result_generate_app=''

# 结果表批量粘贴导入按钮
result_batch_paste_import_package=''

# 结果表批量粘贴弹框文本录入框
result_batch_paste_import_package_input=''

# 结果表批量粘贴弹框确认按钮
result_batch_paste_import_package_confirm=''

# 结果表自动计算按钮
result_autoComplete=''

# 结果表提交样本按钮
result_commit=''

# 结果表提交样本确认弹框按钮
result_commit_confirm=''

# 结果表任务状态
result_task_status=''

# 结果表保存按钮
result_save=''

# 结果表完成任务单按钮
result_complete_task=''

# 结果表返回明细表按钮
result_return_detail=''

# 结果表返回明细表确认
result_return_detail_confirm=''