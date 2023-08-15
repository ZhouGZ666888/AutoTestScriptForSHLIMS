# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 流转表定位元素
# -*-*************************************************************************************-*-

# -*-*****************单样本流转表元素定位# *****************-*-
"""
【样本筛选】功能的元素定位
"""
#页面样本筛选按钮
sample_search_button=(
    '.task_btn .taskInitial-btn-searchVisible')

#筛选弹框中【订单号】的输入框
search_lims_code=(
    '.search-form-sampleIdLims input')

#订单输入框点击后，右侧新弹开的文本框,输入框
search_order_code_text=(
    '.draw-sampleId-lims .el-textarea.el-input--medium textarea')

#点击输入框的确定按钮
search_order_code_confirm=(
    '.draw-sampleId-lims .drawer-footer .el-button--primary')

#点击最外层的确定按钮
lzb_search_confirm=(
    '.dialog-search-sample .dialog-footer .baseClass-btn-confirm')

#点击全选全选富集节点的复选框
poolling_check_box=(
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="文库富集"]/preceding-sibling::span')

#点击【修改预计生成时间】按钮
modify_pretime_button=(
    '.task_btn div:nth-child(6) .taskInitial-btn-showPredict')

#弹框中输入日期
modify_pretime_value=(
    '.taskInitial-form-libquantEstimatedGeneratedTime input')

#输入日期后，点击确定按钮
modify_pretime_confirm=(
    '.dialog-predict-time .dialog-footer .baseClass-btn-confirm')

