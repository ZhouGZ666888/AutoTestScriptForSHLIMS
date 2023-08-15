# -*- coding: utf-8 -*-
# @Time    : 2022/03/22
# @Author  : guanzhong.zhou
# @File    : sr样本信息登记
# -*-*************************************************************************************-*-

"""
首页列表元素定位
"""
# 搜索按钮
search_btn = (
    '.app-container .filter-container .baseClass-btn-search')

# 编辑按钮
edit_btn = (
    '.app-container .filter-container .baseClass-btn-edit')

# 搜索lims号文本框
search_lims = (
    '.dialog-search .srSampleList-dialog-sampleIdLims input')

# 搜索弹框确认按钮
search_comfirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-confirm')

# sr样本信息导入
sr_sample_imp = (
    '.app-container .filter-container .baseClass-btn-sampleImport')

# sr样本信息导入框
sr_sample_imp_input=(
    '.dialog-upload .el-upload--text input')

#sr样本信息导入框，上传按钮
sr_sample_imp_upload=(
    '.el-dialog.dialog-upload .el-dialog__footer .baseClass-btn-upload')

#sr样本导入列表，第一条数据
choice_imp_sr_sample=(
    '.sample_receive_detail .el-table__body-wrapper tbody tr:nth-child(1)')

# 子文库信息导入
sr_childrenImport = (
    '.app-container .filter-container .baseClass-btn-childrenImport')

#页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

"""
外部样本信息登记详情页
"""
# 子文库信息导入
btn_childrenImport = (
    '.sr-btn-childrenImport')

#子文库信息导入框
sr_childrenImport_input=(
    '.dialog-upload .el-upload--text input')

#子文库信息导入框，上传按钮
sr_childrenImport_upload=(
    '.el-dialog.dialog-upload .el-dialog__footer .baseClass-btn-upload')

#外部样本搜索弹框
sr_form_sampleIdLims=(
    '.sr-form-sampleIdLims .el-button.el-button--default.el-button--medium')

#外部样本搜索弹框,lims号输入框
sr_form_sampleIdLims_lims=(
    '.dialogLims-form-sampleIdLims input')

#外部样本搜索弹框,外部样本号输入框
sr_form_sampleIdExternal_lims=(
    '.dialogLims-form-sampleIdExternal input')

#外部样本搜索弹框，搜索按钮
sr_search_btn=(
    '.baseClass-btn-search')

#搜索结果选择第一条
sr_search_choice=(
    '.el-dialog__body .el-table--enable-row-transition .el-table__body-wrapper tbody tr:nth-child(1)')

#外部样本搜索弹框，关闭按钮
close_btn=(
    '.dialog-lims .baseClass-btn-close')

# 外部样本信息登记详情页，保存按钮
save_btn=(
    '.SrSampleDetail .SrSampleDetail_header .baseClass-btn-save')