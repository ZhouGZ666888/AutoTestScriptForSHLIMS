# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 盒位管理元素定位
# -*-*************************************************************************************-*-

# ===================样本盒移库的元素如下===========================

"""
移盒管理列表页，新增任务单功能
"""
# 列表页，点击新增按钮
ybhyk_list_add_button = '//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]'

# 弹框中，选择样本盒下拉框，再选择选项
ybhyk_list_select_transfer_type = '//*[@class="el-select moveCreated-form-transferType el-select--medium"]'
ybhyk_list_select_transfer_type_value = '//*[@class="el-scrollbar__view el-select-dropdown__list"]//span[contains(.,"样本盒")]'

# 弹框中，选择库外到临时库下拉框，再选择选项
ybhyk_list_select_transfer_flow = '//*[@class="el-select moveCreated-form-transferFlow el-select--medium"]'
ybhyk_list_select_transfer_flow_value = '//*[@class="el-scrollbar__view el-select-dropdown__list"]//span[contains(.,"库外到临时库")]'
# 弹框中，选择完后点击确认按
ybhyk_list_select_confirm = '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

"""
移盒详情页，搜索要移的盒子功能
"""
# 点击选择盒子搜索按钮
ybhyk_detail_search_box = '//*[@class="el-button baseClass-btn-search-box el-button--primary el-button--small"]'

# 弹框中，点击输入框
ybhyk_detail_search_box_name = '//*[@class="searchBox-name el-input el-input--medium el-input-group el-input-group--prepend"]//input'

# 新弹框中，点击右侧弹出的输入框
ybhyk_detail_enter_value = '//*[@class="el-textarea el-input--medium"]/textarea'

# 输入盒子信息后，点击确定
ybhyk_detail_enter_value_confirm = '//*[@class="drawer-footer"]//descendant::button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

# 右侧弹框关闭后，点击最终搜素的确认按钮
ybhyk_detail_search_confirm = '//*[@class="dialog-footer"]//descendant::button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium" and preceding-sibling::button]'

# 搜索完毕后，检查列表中是否有数据（前面有复选框即代表有数据）
ybhyk_detail_search_result = '//*[@class="vxe-body--row height_50"]//descendant::span'

# 勾选这个复选框
ybhyk_detail_search_checkbox = '//*[@class="vxe-table--header-wrapper body--wrapper"]//descendant::span//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]'

# 勾选盒子后，点击加入明细表
ybhyk_detail_add_to_list = '//*[@class="el-button baseClass-btn-addToSchedule el-button--primary el-button--small"]'

# 点击进入明细表
ybhyk_detail_go_to_list = '//*[@class="el-button baseClass-btn-goSchedule el-button--primary el-button--small"]'
"""
加入明细表后，进入明细表操作
"""
# 进入明细表后，先点击保存接口
ybhyk_detail_list_save_button = '//*[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]'

# 勾选已经加入明细表的数据，点击复选框
ybhyk_detail_list_select_checkbox = '//*[@class="vxe-table--header-wrapper body--wrapper"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]'

# 勾选已经加入明细表的数据，点击选择库位的按钮
ybhyk_detail_list_select_storage = '//*[@class="el-button baseClass-btn-storage el-button--primary el-button--small"]'

# 选择库位弹框中输入指定的库位信息
ybhyk_detail_list_select_storage_value = '//*[@class="el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input'

# 选择库位弹框中输入指定的库位信息,点击搜索
ybhyk_detail_list_select_storage_search = '//*[@class="el-col el-col-3 el-col-offset-1"]//button[@class="el-button el-button--primary el-button--medium"]'

# 搜索完毕后，点击搜索结果
ybhyk_detail_list_select_result = '//*[@class="el-table el-table--fit el-table--striped el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table--medium"]//descendant::td'

# 点击确认
ybhyk_detail_list_select_confirm = '//*[@class="el-dialog__footer" ]//span//button[@class="el-button el-button--primary el-button--medium"]'

# 点击提交按钮
ybhyk_detail_list_submit = '//*[@class="el-button baseClass-btn-submit el-button--primary el-button--medium" ]'

"""
样本/盒移位列表页，搜索任务单功能
"""
# 搜索盒位信息在哪个任务单，搜索按钮
ybhyk_list_search_box = '//*[@class="el-button baseClass-btn-searchBox el-button--primary el-button--medium" ]'

# 搜索弹框中，输入盒子信息
ybhyk_list_search_boxname = '//*[@class="box-form-sampleBoxName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix" ]//input'

# 搜索弹框中，输入盒子信息,点击确定
ybhyk_list_search_boxname_confirm = '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium" ]'

# 搜索完成后，校验搜索结果是否存在
ybhyk_list_search_result = '//*[@class="el-table__body-wrapper is-scrolling-none"]//descendant::td'

# ===================样本移库的元素如下===========================

"""
移样本管理列表页，新增功能
"""
# 列表页，点击新增按钮
ybyk_list_add_button = '//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]'

# 弹框中，选择样本盒下拉框，再选择选项
ybyk_list_select_transfer_type = '//*[@class="el-select moveCreated-form-transferType el-select--medium"]'
ybyk_list_select_transfer_type_value = '//*[@class="el-scrollbar__view el-select-dropdown__list"]//span[text()=("样本")]'

# 弹框中，选择库外到临时库下拉框，再选择选项
ybyk_list_select_transfer_flow = '//*[@class="el-select moveCreated-form-transferFlow el-select--medium"]'
ybyk_list_select_transfer_flow_value = '//*[@class="el-scrollbar__view el-select-dropdown__list"]//span[contains(.,"临时库到临时库")]'
# 弹框中，选择完后点击确认按钮
ybyk_list_select_confirm = '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

"""
进入明细表前操作
"""

# 点击【样本筛选】按钮
ybyk_detail_select_button = '//*[@class="el-button baseClass-btn-searchSample el-button--primary el-button--small"]'
# 点击LIMS号搜索框
ybyk_detail_sample_enter = '//*[@class="sampleSearch-form-sampleIdLims el-input el-input--medium el-input-group el-input-group--prepend"]//input'
# 点击右侧弹框中的输入框
ybyk_detail_sample_value = '//*[@class="sampleId-lims-input el-textarea el-input--medium"]//textarea'
# 输入完数据后，点击确定按钮
ybyk_detail_sample_confirm = '//*[@class="draw-sampleId-lims"]//section//button[@class="el-button el-button--primary el-button--medium"]'
# 点击确定按钮，确认搜索
ybyk_detail_sample_search_confirm = '//*[@class="el-dialog el-dialog--center dialog-sample-search"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
# 勾选点击复选框（这里我们每次就选择第一个样本了）
ybyk_detail_select_checkbox = '//*[@class="vxe-table--body"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]'
# 勾选样本后，点击加入明细表
ybyk_detail_add_to_list = '//*[@class="el-button baseClass-btn-addToSchedule el-button--primary el-button--small"]'
# 点击进入明细表
ybyk_detail_go_to_list = '//*[@class="el-button baseClass-btn-goSchedule el-button--primary el-button--small"]'

"""
加入明细表后，进入明细表操作
"""
# 进入明细表后，先点击保存接口
ybyk_detail_list_save_button = '//*[@class="el-button baseClass-btn-save el-button--primary el-button--medium"]'

# 勾选已经加入明细表的数据，点击复选框
ybyk_detail_list_select_checkbox = '//*[@class="vxe-table--fixed-left-wrapper"]//table[@class="vxe-table--header"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]'
# 点击选择盒位的按钮
ybyk_detail_list_select_storage = '//*[@class="el-button baseClass-btn-selectBox el-button--primary el-button--small"]'

# 选择库位弹框中输入指定的盒子信息
ybyk_detail_list_select_storage_value = '//*[@class="searchBox-form-boxName el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input'

# 选择库位弹框中输入指定的盒位信息,点击搜索
ybyk_detail_list_select_storage_search = '//*[@class="el-button baseClass-btn-search el-button--primary el-button--medium"]'

# 搜索完毕后，点击搜索结果
ybyk_detail_list_select_result = '//*[@class="el-table el-table--fit el-table--striped el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table--medium"]//descendant::td'

# 点击确认
ybyk_detail_list_select_confirm = '//*[@class="el-dialog__footer"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium" and preceding-sibling::button ]'

# 滑动表格滑条后，锁定表格最后一个单元格位置，注意这里使用last()方法
ybyk_detail_list_box_position = '//*[@class="vxe-table--body-wrapper body--wrapper"]//descendant::tr//td[last()]'

# 输入盒位信息
ybyk_detail_list_box_position_value = '//*[@class="vxe-table--body-wrapper body--wrapper"]//descendant::tr//td[last()]//input'

# 点击提交按钮
ybyk_detail_list_submit = '//*[@class="el-button baseClass-btn-submit el-button--primary el-button--medium"]'

"""
返回列表后，检索刚刚完成的那个样本移库申请单
"""
# 列表页，搜索样本按钮
ybyk_list_search_button = '//*[@class="el-button baseClass-btn-searchSample el-button--primary el-button--medium"]'
# 弹框中输入taskid
ybyk_list_search_taskid = '//*[@class="moveSearch-form-taskId el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input'
# 点击确定搜索按钮
ybyk_list_search_confirm = '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
# 搜索完毕后，列表应该展示taskid信息
ybyk_list_search_result = '//*[@class="el-table__body-wrapper is-scrolling-none"]'
