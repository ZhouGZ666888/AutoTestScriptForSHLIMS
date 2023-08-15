# -*- coding: utf-8 -*-
# @Time    : 2021/12/27
# @Author  : guanzhong.zhou
# @File    : 基本信息任务分配页面元素定位
# -*-*************************************************************************************-*-
# 页面全选按钮
all_choice = (
    '.reportTaskDistribution-table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 批量是否处理按钮
batch_processed_btn = (
    '.action-button-list .reportTaskDistribution-btn-is_expedited')
# 批量选择负责人
batch_choice_person_charge = (
    '.action-button-list .reportTaskDistribution-btn-addUser')

# 批量选择负责人弹框录入负责人
charge_person_input = (
    '.dialog-choose-user input')

# 批量负责人弹框选择
charge_person_choice = (
    '//body/child::div[@class="el-select-dropdown el-popper"]/descendant::li[1]')

# 批量负责人弹框确定按钮
batch_choice_person_charge_comfirm = (
    '.dialog-choose-user .el-dialog__footer .baseClass-btn-confirm')

# 批量删除负责人
batch_delete_person_charge = (
    '.action-button-list .reportTaskDistribution-btn-deleteUser')

# 筛选按钮
search_btn = (
    '.search-form .search-button-list .reportTaskDistribution-btn-onSearch')

# 筛选条件-订单号文本录入框
order_num = (
    '.reportTaskDistribution-form-orderCode input')


# 页面提示信息，元素定位
page_info=(
    '//*[@class="el-message el-message--success"]')