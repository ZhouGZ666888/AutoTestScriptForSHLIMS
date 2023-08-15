# -*- coding: utf-8 -*-
# @Time    : 2022/02/09
# @Author  : guanzhong.zhou
# @File    : 样本项目信息修改元素定位
# -*-*************************************************************************************-*-
"""
样本项目信息修改首页列表元素定位
"""
# 搜索按钮
search = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索弹框lims号录入文本
search_lims_sample_num = (
    '.search-form-sampleIdLims input')

# 搜索弹框实验室号录入文本
search_labrary_sample_num = (
    '.search-form-labCode input')

# 搜素弹框确认
search_confirm = (
    '.dialog-search-taskInfo .el-dialog__footer .baseClass-btn-confirm')

# 新增按钮
add_task_btn = (
    '.app-container .filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '.project-table .el-table__body-wrapper tbody tr')

# -*-*************************************************************************************-*-

"""
新建
"""
# -修改理由文本录入框
change_reason = (
    '.reason-input textarea')

# 修改理由弹框，下一步按钮
next_step = (
    '.dialog-create-task > .el-dialog__footer .baseClass-btn-next')

#选择待修改样本-按lims号检索tab页
search_by_lims_tab=(
    '.dialog-select-needChange #tab-0')

# 选择待修改样本-按lims号检索文本录入框
search_by_lims = (
    '.dialog-select-needChange .lims-textarea textarea')

#选择待修改样本-按实验室号检索tab页
search_by_labCode_tab=(
    '.dialog-select-needChange #tab-1')

# 选择待修改样本-按实验室号检索文本录入框
search_by_labCode = (
    '.dialog-select-needChange .lab-textarea textarea')

# 选择待修改样本-下一步按钮
search_sample_comfirm = (
    '.dialog-select-needChange .el-dialog__footer .baseClass-btn-next')

# 项目信息确认/修改/提交弹框，导出按钮
download_sampleInfo_btn = (
    '.dialog-check-project .el-dialog__body .export-btn')

#项目信息确认/修改/提交弹框，下一步按钮
download_sampleInfo_comfirm = (
    '.dialog-check-project .el-dialog__footer .baseClass-btn-next')

#项目信息确认/修改/提交，导入按钮
upload_sampleInfo_btn=(
    '.dialog-submit .el-dialog__body input')

#项目信息确认/修改/提交，提交修改任务单
sampleProjectInfo_submit=(
    '.dialog-submit .el-dialog__footer .baseClass-btn-submit')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]')