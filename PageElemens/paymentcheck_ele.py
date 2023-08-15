# -*- coding: utf-8 -*-
# @Time    : 2021/11/11
# @Author  : guanzhong.zhou
# @File    : 款项核对模块元素定位


# 订单号查询文本框，元素定位
orderId = (
    '.search-card .payment-form-orderCode input')

# 订单号查询录入框，元素定位
order_number = (
    '.order-textarea.el-textarea.el-input--medium textarea')

# 订单号查询录入弹框确认按钮，元素定位
order_search_comfirm_btn = (
    '.dialog-order-id .el-dialog__footer .baseClass-btn-confirm')

# 筛选按钮，元素定位
screen_button = (
    '.search-button-list .baseClass-btn-search')


# 筛选结果，取第一个结果，元素定位
body_list = (
    '.sample_receive_detail tbody tr:nth-child(1)')

# 修改状态按钮，元素定位
statue_button = (
    '.search-button-list .baseClass-btn-changeStatus')

#选择确认状态按钮（默认已确认），元素定位
chioce_status_button=(
    '/html/body/ul/li[2]')
# ('//*[@id="dropdown-menu-5308"]/li[2]')

# 保存按钮，元素定位
save_button = (
    '.search-button-list .baseClass-btn-save')

# 保存成功提示信息
save_success_info = (
    '//*[@class="el-message el-message--success"]')
