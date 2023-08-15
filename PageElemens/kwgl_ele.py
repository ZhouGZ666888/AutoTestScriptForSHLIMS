# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 盒位管理元素定位
# -*-*************************************************************************************-*-


"""
库位管理列表页，新增功能
"""

#列表页新增按钮（临时库）
kwgl_list_add_ls_button=('//*[@class="el-button filter-item baseClass-btn-add el-button--primary el-button--medium"]')

#新增临时库，点击输入库位名称
kwgl_list_add_ls_name=('//*[@class="dialogSave00-form-storageName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]/input')

#新增临时库，下拉框选择库位位置
kwgl_list_add_ls_location_select=('//*[@class="el-select dialogSave00-form-positionCode el-select--medium"]')

#新增临时库，下拉框选择库位位置，这里我们指定A7位置
kwgl_list_add_ls_location=('//*[@class="el-scrollbar__view el-select-dropdown__list"]//descendant::li//span[text('
                           ')="A106"]')

#新增临时库，这里我们位置描述信息
kwgl_list_add_ls_location_desc=('//*[@class="dialogSave00-form-positionDesc el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]/input')

#新增临时库，添加使用人信息,编辑按钮
kwgl_list_add_ls_user=('//*[@class="el-button baseClass-btn-changeManager el-button--primary el-button--medium"]')

#新增临时库，添加使用人信息,编辑按钮，输入使用人姓名
kwgl_list_add_ls_username=('//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]/input')

#输入使用人姓名后选择联想结果
kwgl_list_add_ls_username_search=('//*[@class="el-scrollbar__view el-autocomplete-suggestion__list"]')


#新增临时库，添加使用人信息,编辑按钮，输入使用人姓名,点击添加按钮
kwgl_list_add_ls_username_add_butoon=('//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]')

#新增临时库，输入姓名后，点击确定
kwgl_list_add_ls_username_add_confirmn=('//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')

#新增临时库，所有信息填写完毕后，点击确定按钮
kwgl_list_add_ls_confirm=('//*[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]')


"""
库位管理列表页，搜索功能
"""

#列表页，点击搜索按钮
kwgl_list_search_button=('//*[@class="el-button filter-item baseClass-btn-search el-button--primary el-button--medium"]')

#搜索弹框中，输入指定库位信息
kwgl_list_search_name=('//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]/input')

kwgl_list_search_confirm=('//*[@class="el-dialog__footer"]//following-sibling::button[@class="el-button el-button--primary el-button--medium"]')








