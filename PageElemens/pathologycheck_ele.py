# -*- coding: utf-8 -*-
# @Time    : 2021/11/22
# @Author  : guanzhong.zhou
# @File    : 病理检验元素定位
# -*-*************************************************************************************-*-
'''
病理检验首页列表元素定位
'''
# 搜索按钮，元素定位
search = (
    '.filter-container .baseClass-btn-search')

# 搜索弹框，按lims号搜素文本框，元素定位
search_lims_sample_num = (
    '.dialog-search-task .search-form-sampleIdLims input')
# 搜索弹框，确认按钮，元素定位
search_confirm = (
    '.dialog-search-task .el-dialog__footer .baseClass-btn-confirm')

# 新建按钮，元素定位
add = (
    '.filter-container .baseClass-btn-add')

# 编辑按钮，元素定位
edit = (
    '.filter-container .baseClass-btn-edit')

# 删除按钮，元素定位
delete = (
    '//*[@class="filter-container"]/button[4]')

# 页面列表样本
sample_num = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-
'''
待选表元素定位
'''
# 选择任务类型下拉按钮，元素定位
task_type = (
    '.el-form.el-form--label-left > div:nth-child(1) input')

# 选择任务类型下拉值，格式化选择某一条，元素定位
task_type_chioce = (
    '.task-type-unique li:nth-child({})')

# 选择SOP下拉按钮，元素定位
select_sop = (
    '.el-form.el-form--label-left > div:nth-child(2) input')

# 选择sop下拉值，默认选择第一条，元素定位
select_sop_chioce = (
    '.sop-type-unique .el-select-group li:nth-child(1)')

# 核对lims样本号按钮，元素定位
check_lims_sample_number = (
    '.createTask_content_choose .btn-check-sampleIdLims')

# 核对lims样本号弹框，文本录入框，元素定位
check_lims_sample_number_textarea = (
    '.dialog-check-sampleIdLims .check-sampleIdLims-input textarea')

# 核对lims样本号弹框确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-check-sampleIdLims .dialog-footer .baseClass-btn-confirm')

# 样本明细全选按钮，元素定位
all_chioce = (
    '.createTask_content_table .vxe-table--header-wrapper thead .vxe-checkbox--unchecked-icon')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.createTask_content_choose .baseClass-btn-saveTask')

# 进入结果表按钮，元素定位
enter_result_list_btn = (
    '.createTask_content_choose .baseClass-btn-goResult')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

# -*-*************************************************************************************-*-
'''
HE病理结果表元素定位
'''
# 删除样本按钮，元素定位
delete_selected_task = (
    '.button-list .btn-delete-task')

# ********批量实验数据********* #
# 批量实验数据按钮，元素定位
batch_laboratory_data = (
    '.button-list .btn-batch-data')

# 坏死细胞比例（%）文本录入框，元素定位
necrotic_cell_ratio = (
    '.pathologyHeResult-form-tumourCellNecroLvl input')

# 质控结果下拉选择，元素定位
quality_control_result = (
    '.pathologyHeResult-form-sectionQuality input')

# 质控结果下拉选择值，元素定位
quality_control_result_value = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="合格"]]')

# 检验结果下拉选择，元素定位
test_result = (
    '.pathologyHeResult-form-examingResult input')

# 检验结果下拉选择值，元素定位
test_result_value = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="通过"]]')

# 标签打印份数文本框，元素定位
number_of_labels_printed = (
    '.pathologyHeResult-form-stickNumber input')

#染片保存位置
stained_sections_socation = (
    '.pathologyHeResult-form-stainedSectionsLocation input')

# 批量实验数据，确认按钮
confirm_btn = (
    '.dialog-batch-data .el-dialog__footer .baseClass-btn-confirm')

# ********批量实验员/日期数据********* #

# 批量实验员/日期按钮，元素定位
batch_laboratory_personnel_data = (
    '.button-list .btn-show-experimenter')

# 实验员文本录入，元素定位
laboratory_personnel = (
    '.experimenter-form-assistant input')

# 实验员选择，默认第一条，元素定位
laboratory_personnel_value = (
    '.el-autocomplete-suggestion__list li:nth-child(1)')

# 实验日期文本框，元素定位
laboratory_test_date = (
    '.experimenter-form-examingDateValue input')

# 批量实验员/日期，确认按钮，元素定位
batch_laboratory_personnel_data_confirm = (
    '.dialog-experimenter .dialog-footer .baseClass-btn-confirm')


# ********批量诊断者/日期数据********* #
# 批量诊断者/日期按钮，元素定位
batch_diagnosis_data = (
    '.button-list .btn-show-experimenterDate')

# 诊断者文本录入，元素定位
batch_diagnosis = (
    '.experimenter-form-assistant input')

# 诊断者选择，默认第一条，元素定位
batch_diagnosis_value = (
    '.el-autocomplete-suggestion__list li:nth-child(1)')

# 实验日期文本框，元素定位
diagnosed_date = (
    '.experimenter-form-examingDateValue input')

# 批量诊断者/日期，确认按钮，元素定位
batch_diagnosis_data_confirm = (
    '.dialog-experimenter .dialog-footer .baseClass-btn-confirm')


# 搜索文本框，元素定位
search_input = (
    '.button-list .input-with-search input')

# 搜索确认按钮，元素定位
search_btn = (
    '.button-list .baseClass-btn-search')

# 全选按钮，元素定位
result_all_chioce = (
    '.vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 获取表格所有样本的肿瘤细胞比例列
all_sample = (
    '.createTask_content_table .vxe-table--body-wrapper tr .pathologyHeResult-tableCol-tumourCellRadio  ')

# 单个获取表格所有样本的Tumor cell content列
all_sample_one_by_one = (
    '.createTask_content_table .vxe-table--body-wrapper tr:nth-child({}) .pathologyHeResult-tableCol-tumourCellRadio  ')

# 单个获取表格所有样本的Tumor cell content列的文本录入框
all_tumor_cell_content_input = (
    '.createTask_content_table .vxe-table--body-wrapper tr:nth-child({}) .pathologyHeResult-tableCol-tumourCellRadio   input')

# 提交完成按钮，元素定位
submit_success = (
    '.button-list .btn-submit')

# 结果表保存
result_save = (
    '.createTask_content .baseClass-btn-save')

# -*-*************************************************************************************-*-
'''
PD-L1(28-8)病理结果表元素定位
'''

# ********选择癌种********* #
# 选择癌种信息弹框，元素定位
batch_cancer_type_pd = (
    '.button-list .btn-cancer-type')

# 癌种类型选择下拉框
cancer_type = (
    '.dialog-cancerType input')

# 癌种下拉类型值选择，第三条
cancer_type_chioce = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="其他"]]')

# 癌种选择弹框，确认按钮
cancer_type_confirm = (
    '.dialog-cancerType .dialog-footer .baseClass-btn-confirm')

# ********批量实验数据*********************************** #
# 批量实验数据按钮，元素定位
batch_laboratory_data_pd = (
    '.button-list .btn-experimentData')

# TPS文本录入
tps = (
    '.experimental-form-tpsRadio input')

# CPS文本录入
cps = (
    '.experimental-form-cps input')

# 标签打印份数文本框，元素定位
number_of_labels_printed_pd = (
    '.experimental-form-stickNumber input')

# 活肿瘤细胞数目≥100个为合格,下拉选择弹框
Number_of_viable_tumor_cell = (
    '.experimental-form-tcnIsMoreThen100 input')

# 活肿瘤细胞数目≥100个为合格,下拉值选择
Number_of_viable_tumor_cell_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="是"]]')

# 质控片染色结果下拉按钮
quality_contol_sample_staining_result = (
    '.experimental-form-sectionQuality input')

# 质控片染色结果下拉按钮值选择
quality_contol_sample_staining_result_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="合格"]]')

# 测试结果下拉按钮
test_result_pd = (
    '.experimental-form-examingResult input')

# 测试结果下拉值选择按钮
test_result_pd_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="通过"]]')

# 批量实验数据弹框确认按钮
batch_laboratory_data_pd_confirm = (
    '.dialog-enter-experimental .el-dialog__footer .baseClass-btn-confirm')

# ********批量实验员/日期数据********* #

# 批量实验员/日期按钮，元素定位
batch_laboratory_personnel_data_pd = (
    '.button-list .btn-show-experimenter')

# 实验员文本录入，元素定位
laboratory_personnel_pd = (
    '.user-form-labAssistantName input')

# 实验员选择，默认第一条，元素定位
laboratory_personnel_value_pd = (
    '.el-autocomplete-suggestion__list li:nth-child(1)')

# 实验日期文本框，元素定位
laboratory_test_date_pd = (
    '.user-form-examingDateValue input')

# 批量实验员/日期，确认按钮，元素定位
batch_laboratory_personnel_data_confirm_pd = (
    '.dialog-user .el-dialog__footer .baseClass-btn-confirm')

# ********批量诊断者/日期数据********* #
# 批量诊断者/日期按钮，元素定位
batch_diagnosis_data_pd = (
    '.button-list .btn-show-experimenterDate')

# 诊断者文本录入，元素定位
batch_diagnosis_pd = (
    '.diagnosis-form-userName input')

# 诊断者选择，默认第一条，元素定位
batch_diagnosis_value_pd = (

    '.el-autocomplete-suggestion__list li:nth-child(1)')
# 实验日期文本框，元素定位
diagnosed_date_pd = (
    '.diagnosis-form-dateValue input')

# 批量诊断者/日期，确认按钮，元素定位
batch_diagnosis_data_confirm_pd = (
    '.dialog-diagnosis .el-dialog__footer .baseClass-btn-confirm')

# 提交完成按钮，元素定位
submit_success_pd = (
    '.button-list .btn-submit')

# 保存按钮，元素定位
result_save_pd = (
    '.app-main .baseClass-btn-save')

# 全选按钮选择
all_chioce_pd = (
    '.vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
