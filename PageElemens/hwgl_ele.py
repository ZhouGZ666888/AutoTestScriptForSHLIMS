# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 盒位管理元素定位
# -*-*************************************************************************************-*-

# -*-*****************列表页搜索元素定位# *****************-*-
"""
盒位管理列表页，搜索功能
"""
#列表页搜索按钮
hwgl_list_search_button=('//*[@class="el-button filter-item baseClass-btn-search el-button--primary el-button--medium"]')

#列表页搜索按钮,搜索弹框中，盒子输入框
hwgl_list_search_box_name=('//*[@class="dialogBoxSearch-form-boxName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

#搜索弹框中，点击确认按钮
hwgl_list_search_confirm=('//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

"""
盒位管理列表页，删除功能
"""
#列表中，选择一个盒子
hwgl_list_first_data=('//*[@class="el-table__body-wrapper is-scrolling-none"]//descendant::td[1]')
#列表中，选择删除按钮
hwgl_list_detel=('//*[@class="el-button filter-item baseClass-btn-delete el-button--primary el-button--medium"]')

#如果有盒子里有样本，系统会toast提示不能删，这个提示元素为
hwgl_list_detel_toast=('//*[@class="el-message__content"]')

#删除弹框中，填入删除理由，点击确定
hwgl_list_detel_reason=('//*[@class="el-textarea el-input--medium"]//textarea')
hwgl_list_detel_confirm=('//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

"""
盒位管理列表页，新增功能
"""

#新增按钮
hwgl_list_add=('//*[@class="el-button filter-item baseClass-btn-edit el-button--primary el-button--medium"]')


#填写新建的样本盒数量
hwgl_list_num=('//*[@class="batchCreate-form-boxNum el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')
#填写完数量后，点击确定
hwgl_list_num_confirm=('//*[@class="el-button baseClass-btn-next el-button--primary el-button--medium"]')
#新弹框中，点击【样本盒名称】输入框
hwgl_detail_box_name='.dialog-box .el-dialog__body .create-table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(2)'
#点击输入框后，输入信息
hwgl_detail_box_name_value='.dialog-box .el-dialog__body .create-table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(2) input'
#点击选择样本盒规格的输入框
hwgl_detail_box_size='.dialog-box .el-dialog__body .create-table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(3)'
#空白位置，录入名称后点击
other_position='.dialog-box .el-dialog__body .create-table .vxe-table--main-wrapper .vxe-table--header-wrapper table tr th:nth-child(2)'
#再点击对应的下拉框
hwgl_detail_box_size_select='.dialog-box .el-dialog__body .create-table .vxe-table--main-wrapper .vxe-table--body-wrapper table tbody tr:nth-child(1) td:nth-child(3) input'
#下拉框弹框后，选择指定的规格
hwgl_detail_box_size_value='//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]//li[@class="el-select-dropdown__item" ]/span[contains(text(),"9*9")]'
#下拉框弹框后，选择指定的规格,点击确定按钮
hwgl_detail_box_add_confirm=('//*[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]//span')












