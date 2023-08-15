# -*- coding: utf-8 -*-
# @Time    : 2021/12/29
# @Author  : guanzhong.zhou
# @File    : 报告---报告编写任务分配页面元素定位
# -*-*************************************************************************************-*-

# 筛选条件，订单号文本录入框元素定位
order_nub = (
    '.reportWritingTaskAssignment-form-orderCode input')

# 筛选条件，项目号下拉框元素定位
project_num = (
    '.reportWritingTaskAssignment-form-projectId input')
# 筛选条件，选择项目号
project_num_chioce = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="J022"]]')

# 筛选条件，预计实验日期
poolingDate = (
    '.reportWritingTaskAssignment-form-poolingDate input')

# 筛选按钮
search_btn = (
    '.search-button-list .reportTaskDistribution-btn-onSearch')

# 重置按钮
reset_btn = (
    '.search-button-list .reportTaskDistribution-btn-reset')

# 筛选报告结果
result_report_search = (
    '//*[@class="sample_receive_detail"]/div[1]/div[2]/descendant::tbody/tr')

# 批量选择编写人按钮
select_writer_bulk_btn = (
    '.el-tabs__header #tab-first')

# 编写人选择
select_writer_bulk_choice = (
    '#pane-first div:nth-child(1).reportStaticCard')

# 批量选择审核人按钮
batch_selection_examiner_btn = (
    '.el-tabs__header #tab-second')

# 审核人选择
batch_selection_examiner_choice = (
    '#pane-second div:nth-child(1).reportStaticCard')

# 全选按钮
all_choice = (
    '.sample_receive_detail .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 页面提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')