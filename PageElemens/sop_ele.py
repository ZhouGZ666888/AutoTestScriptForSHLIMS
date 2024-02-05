# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : sop主数据元素定位
# -*-*************************************************************************************-*-


# -*-*****************列表页搜索元素定位# *****************-*-
"""
sop列表页，搜索定位元素
"""
# 列表页搜索按钮
sop_list_search_butten = '.app-container .filter-container button:nth-child(1)'

# 搜索弹框中的模块类型下拉框
sop_list_search_module_type = (
    '//*[@class="el-dialog el-dialog--center" and @aria-label="搜索"]//div[@class="el-input el-input--medium el-input--suffix"]/input')

# 搜索弹框中的模块类型下拉框,选择‘核酸提取’节点作为搜索任务类型
sop_list_search_module = (
    '//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]//descendant::li//span[text()="核酸提取"]')

# 输入完条件后，点击确定按钮
sop_list_search_module_comfirm = (
    '//*[@class="el-dialog el-dialog--center" and @aria-label="搜索"]//button//span[text()="确定"]')

# 搜索完后，勾选已失效的sop选项
sop_list_search_show_obsolete_sop = (
    '//*[@class="el-card__header"]/descendant::span[contains(text(),"展示失效/暂停使用SOP")]')

# -*-*****************新建sop的元素定位# *****************-*-
"""
sop详情页，基础数据填写元素
"""
# 列表页点击新建按钮
sop_list_creat_butten = (
    '//*[@class="el-button el-button--primary el-button--medium"]//span[text()="新建"]')

# 详情页，sop名称输入框
sop_detail_sopname = (
    '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"] //input[@type="text"]')

# 详情页，sop版本号输入框
sop_detail_sopname_version = (
    '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"] //input[@type="text" and preceding-sibling:: div[span[text()="版本号"]]]')

# 详情页，sop核对人输入框
sop_detail_sopname_people = (
    '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"] //input[@type="text" and preceding-sibling:: div[span[text()="核对人"]]]')
# 详情页，sop核对人弹框内的输入框
sop_detail_sopname_people_value = (
    '//*[@class="el-form demo-form-inline el-form--inline"]/descendant::input')
# 详情页，sop核对人弹框内的搜索按钮
sop_detail_sopname_search_button = (
    '//*[@class="el-form demo-form-inline el-form--inline"]/descendant::button')
# 详情页，sop核对人弹框内的搜索结果
sop_detail_sopname_search_value = (
    '//*[@class="el-dialog el-dialog--center"]//div[@class="el-table__body-wrapper is-scrolling-none"]')
# 详情页，sop核对人弹框内的确定按钮
sop_detail_sopname_confirm_button = (
    '//*[@class="el-dialog el-dialog--center" and @aria-label="选择核对人"]//div[@class="el-dialog__footer"]//descendant::button[@class="el-button el-button--primary el-button--medium"]')

# 详情页，sop编码输入框
sop_detail_sopname_code = '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"] //input[@type="text" and preceding-sibling::div[text()="SOP代码"]]'

# 详情页，sop所属模块下拉框
sop_detail_sopname_module = (
    '//*[@class="el-form-item is-required el-form-item--medium"]//input')

# 详情页，sop所属模块下拉框，调用时循环写入
sop_detail_sopname_module_value = '//*[@class="el-select-dropdown el-popper"]//descendant::ul[@class="el-scrollbar__view el-select-dropdown__list"]//descendant::li[@class="el-select-dropdown__item" and span[text()="{}"]]'

# 详情页，选择操作方式下拉框
sop_detail_work_type = '//*[@class="el-select SOPversionDetail-form-operationType el-select--medium"]//input'

# 详情页，选择操作方式下拉框数值
sop_detail_work_type_value = '//*[@class="el-scrollbar__view el-select-dropdown__list"]//li//span[text()="人工"]'

# 详情页，sop对应模块的任务类型下拉框
sop_detail_sopname_type = '//*[@class="el-form-item el-form-item--medium" and descendant::span[text()="对应任务类型"] ]//div[@class="el-input el-input--medium el-input--suffix"]//input'

# 详情页，sop对应模块的实验模块下拉框，默认选择第一个选项(方法外我去循环加sop)
sop_detail_sopname_type_value = ('//*[@class="el-select-dropdown__wrap el-scrollbar__wrap"]//ul//li['
                                 '@class="el-select-dropdown__item"]//span[text()="{}"]')

# 详情页，sop填写备注描述
sop_detail_sopname_decription = (
    '//*[@class="el-textarea el-input--medium el-input--suffix"]/textarea')

# 详情页，sop填写文件编号
sop_detail_sopname_fileNo = (
    '//*[@class="sopVersionDetail-form-fileNo el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

# 详情页，sop填写文件名
sop_detail_sopname_filename = (
    '//*[@class="sopVersionDetail-form-fileName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

# 详情页，SAVE按钮
sop_detail_save_butten = (
    '//*[@class="SOPversionDetail_header"]//button[@class="el-button el-button--primary el-button--medium"]//span[text()="保存"]')

"""
sop详情页，产物样本类型数据填写元素
"""

# 详情页，sop点击新增产物按钮
sop_detail_product = (
    '//*[@class="el-card SOPversionDetail_info_box-card is-always-shadow"]//button[@class="el-button border_size el-button--primary el-button--mini"]')

# 详情页，sop点击新增产物按钮,原始样本类型按钮
sop_detail_original_sample_type = (
    '.SOPversionDetail_info_box-card .el-card__body .el-table__body-wrapper tbody tr td:nth-child(1) .el-icon-search')

# 详情页，sop点击新增产物按钮,原始样本类型按钮,点击后的弹框，搜索输入框（输入：其他血浆），选择首选项
sop_detail_original_sample_type_search_result = (
    ' .el-table--scrollable-y .el-table__body-wrapper tbody tr:nth-child(1)')

# 详情页，点击确定按钮
sop_detail_original_sample_type_search_comfirm = ('//*[@aria-label="原样类型"]//descendant::button[4]')

# 详情页，sop点击新增产物按钮,产物样本类型按钮
sop_detail_product_sample_type = (
    '.SOPversionDetail_info_box-card .el-card__body .el-table__body-wrapper tbody tr td:nth-child(2) .el-icon-search')

# 详情页，sop点击新增产物按钮,原始样本类型按钮,点击后的弹框，选择首选项
sop_detail_product_sample_type_search_result = (
    ' .el-table--scrollable-y .el-table__body-wrapper tbody tr:nth-child(1)')

# 详情页，点击确定按钮
sop_detail_product_sample_type_search_comfirm = ('//*[@aria-label="产物类型"]//descendant::button[4]')

# 详情页，点击新增步骤按钮
sop_detail_add_step = (
    '//*[@class="el-button border_size baseClass-btn-add-stepList el-button--primary el-button--mini"]')
# 详情页，点击步骤编号输入框
sop_detail_step_num = (' .SOPversionDetail-sopSteps .vxe-table--body-wrapper tbody td:nth-child(1) input')
# 详情页，点击同步步骤编号按钮
sop_detail_add_restep = (
    '//*[@class="el-button border_size baseClass-btn-edit-synchronization el-button--primary el-button--mini"]')

# 使用JS让页面滑动到最顶端
scroll_view = 'document.getElementsByClassName("SOPversionDetail_info")[0].scrollTop=0'

# 点击生效按钮
sop_effect_button = ('//*[@class="el-button border_size el-button--primary el-button--mini"]//span[text()="确定生效"]')
# 弹框中点击确认按钮
sop_effect_button_confirm = ('//*[@aria-label="提示"]//button[@class="el-button el-button--primary el-button--medium"]')
# 点击返回列表按钮
sop_go_back_list_button = (
    '//*[@class="el-button el-button--default el-button--medium"]/i')
# 点击确认返回列表
sop_go_back_list_button_confirm = (
    '//*[@class="el-button el-button--primary el-button--medium" and span[contains(.,"继续")]]')
