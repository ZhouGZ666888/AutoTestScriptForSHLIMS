# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 流转表元素定位
# -*-*************************************************************************************-*-

# ===================流转表的元素如下===========================

"""
流转表搜索页的元素---订单号搜索
"""
# 列表页，样本筛选按钮
workflow_samplesearch = (
    '//*[@class="el-button taskInitial-btn-searchVisible el-button--primary el-button--small"]')

# 搜索弹框中，点击订单输入框
workflow_samplesearch_order = (
    '//*[@class="search-form-orderCode el-input el-input--medium el-input-group el-input-group--prepend"]//input')

# 点击订单输入框后，右侧弹出的输入框
workflow_samplesearch_order_value = (
    '//*[@class="order-code-input el-textarea el-input--medium"]//textarea')

# 点击确定按钮
order_confirm = (
    '//*[@class="drawer-footer"]//button[@class="el-button el-button--primary el-button--medium"]')

# 点击最外层的确认按钮
search_order_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]')

"""
流转表搜索页的元素---样本号搜索
"""
# 点击【Lims样本号】输入框
workflow_samplesearch_sample = (
    '//*[@class="search-form-sampleIdLims el-input el-input--medium el-input-group el-input-group--prepend"]//input')

# 点击订单输入框后，右侧弹出的输入框
workflow_samplesearch_sample_value = (
    '//*[@class="sampleId-lims-input el-textarea el-input--medium"]//textarea')

# 点击确定按钮
sample_confirm = (
    '//*[@class="drawer-footer"]//button[@class="el-button el-button--primary el-button--medium"]')

# 点击最外层的确认按钮
search_sample_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]')

"""
流转表搜索页的元素---实验室号搜索
"""
# 点击【Lims样本号】输入框
workflow_labcoresearch_sample = (
    '//*[@class="search-form-sampleIdLab el-input el-input--medium el-input-group el-input-group--prepend"]//input')

# 点击订单输入框后，右侧弹出的输入框
workflow_labcoresearch_sample_value = (
    '//*[@class="sampleId-lab-textarea el-textarea el-input--medium"]//textarea')

# 点击确定按钮
labcore_confirm = (
    '//*[@class="drawer-footer"]//button[@class="el-button el-button--primary el-button--medium"]')

# 点击最外层的确认按钮
search_labcore_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]//span[text()="确认"]')

"""
流转表列表页的元素---设置病理任务
"""
# 勾选样本接收全选复选框
get_ybjs_allcheckbox = (
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="样本接收"]/preceding-sibling::span')

# 点击【设置病理任务】按钮
set_blrw_button = (
    '//*[@class="el-button taskInitial-btn-showPathologyConfig el-button--primary el-button--small"]')

# 点击设置弹框里的【添加】按钮
set_blrw_add = (
    '//*[@class="el-button add-btn dialogUsers-dialogUsersBtn-add el-button--primary el-button--mini"]')

# 点击【任务类型】按钮
set_blrw_type = (
    '//*[@class="el-table__row"]//descendant::span[@class="hidden-edit"]')

# 点击【任务类型】按钮的下拉框
set_blrw_select_type = (
    '//*[@class="el-table__row current-row"]//descendant::div[@class="el-input el-input--medium el-input--suffix"]//input')

# 下拉框中，选择选项比如【HE】
set_blrw_select_type_value = (
    '//span[text()="HE"]')

# 点击【保存修改】按钮
set_blrw_save = (
    '//*[@class="el-button taskInitial-btn-saveEdit el-button--primary el-button--medium"]')

"""
流转表列表页的元素---分管操作
"""
# 勾选样本处理全选复选框
get_ybcl_allcheckbox = (
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="样本处理"]/preceding-sibling::span')

# 点击【产物分管】按钮
sample_fg_button = (
    '//*[@class="el-button taskInitial-btn-showSampleSeparation el-button--primary el-button--small"]')

# 默认是下一步，即分1管
sample_fg_num = (
    '//*[@class="el-button taskInitial-form-currentStepName el-button--primary el-button--medium"]')

# 点击全选样本的复选框
sample_fg_allcheckbox = (
    '//*[@class="vxe-cell--title"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 点击最后步骤按钮
sample_fg_laststep = (
    '//*[@class="el-button btn_chlid taskInitial-btnDiver-showlastStepVisible el-button--primary el-button--mini"]')

# 弹框中选择样本处理
sample_fg_laststep_value = (
    '//*[@class="el-table__body-wrapper is-scrolling-none"]//div[text()="样本处理"]')

# 点击确定
sample_fg_laststep_confirm = (
    '.dialog-last-step .el-dialog__footer .baseClass-btn-confirm')

# 点击【修改后项目信息】
sample_fg_modify_project = (
    '//*[@class="el-button border_size btn-change-project el-button--primary el-button--mini"]')

# 弹框里勾选项目号复选框
sample_fg_modify_project_value = (
    '//*[@class="el-dialog el-dialog--center"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 选完项目，点击确定按钮
sample_fg_modify_project_confrim = (
    '.dialog-select-project .el-dialog__footer .baseClass-btn-confirm')

# 点击最外层的确定按钮
sample_fg_confirm = (
    '.dialog-sample-seDetail .el-dialog__footer .baseClass-btn-confirm')

"""
流转表列表页的元素---出库操作
"""
# 点击【样本出库】按钮
sample_ck_button = (
    '//*[@class="el-button taskInitial-btn-showSampleOutbound el-button--primary el-button--small"]')

# 弹框中，全选复选框
sample_ck_allcheckbox = (
    '//*[@class="vxe-cell--title"]//span[@class="vxe-checkbox--icon vxe-checkbox--unchecked-icon"]')

# 点击【实验流程模板】

# 点击【预设探针】


"""
流转表列表页的元素---修改建库信息操作
"""
# 全选建库节点按钮
get_wkgj_allcheckbox = (
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="文库构建"]/preceding-sibling::span')

# 点击【修改建库信息】按钮
update_wkgj_data_button = (
    '//*[@class="el-button taskInitial-btn-showEditLibconstructionType el-button--primary el-button--small"]')

# 全选样本复选框
update_wkgj_data_allcheckbox = (
    '.vxe-table--main-wrapper .vxe-table--body .vxe-checkbox--unchecked-icon')

# 点击【批量建库类型】按钮
update_wkgj_data_libtype = (
    '.dialog-libconstruction-type .taskInitial-btn-handleStorage_type')

# 下拉框选择建库类型
update_wkgj_data_libtype_value = (
    '//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]//li[@class="el-dropdown-menu__item" and text()="{}"]')
# update_wkgj_data_libtype_value=('//*[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]//li[@class="el-dropdown-menu__item" and text()="血液建库"]')
# 点击【修改建库备注】
update_wkgj_data_remarks = (
    '//*[@class="el-button border_size taskInitial-btn-showEditRemarks el-button--primary el-button--mini"]')

# 点击输入框内
update_wkgj_data_remarks_value = (
    '//*[@class="el-textarea el-input--medium"]//textarea')

# 点击确定按钮
update_wkgj_data_remarks_confirm = (
    '//*[@class="el-button qcResult-btn-confirm el-button--primary el-button--medium"]')

# 点击最外层弹框的确定按钮
update_wkgj_data_confirm = (
    '//*[@class="el-button btn-save-all el-button--primary el-button--medium"]')

"""
流转表列表页的元素---修改富集信息操作
"""
# 取消刚刚选择的建库节点
cancel_all_check = (
    '//*[@class="el-button taskInitial-btn-deleteSelect el-button--primary el-button--small"]')

# 全选富集节点的复选框
get_wkfj_allcheckbox = (
    '//*[@class="el-checkbox__input"]//following-sibling::input[@value="文库富集"]/preceding-sibling::span')

# 点击【修改富集信息】按钮
update_wkfj_data_button = (
    '//*[@class="el-button taskInitial-btn-showEditProbe el-button--primary el-button--small"]')

# 全选样本复选框
update_wkfj_data_allcheckbox = (
    '.vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon')

# 点击【批量修改通量】
update_wkfj_thought = (
    '//*[@class="el-button btn_chlid taskInitial-btn-throughput el-button--primary el-button--mini"]')

# 输入数据
update_wkfj_thought_value = (
    '//*[@class="sample-flux-input el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

# 点击确定按钮
update_wkfj_thought_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--small"]')

# 点击【批量修改预设探针】按钮
update_wkfj_prob = (
    '//*[@class="el-button btn_chlid taskInitial-btn-rcvItemPro el-button--primary el-button--mini"]')

# 选择第一个探针
update_wkfj_prob_value = (
    '//*[@class="el-table el-table--fit el-table--border el-table--fluid-height el-table--scrollable-y el-table--enable-row-hover el-table--medium"]//div[text()="AA(PRIME_v5.0.0)/201902-425"]')

# 点击确定按钮
update_wkfj_prob_confirm = (
    '//*[@class="el-button baseClass-btn-confirm el-button--primary el-button--mini"]')

# 点击保存全部按钮
update_wkfj_confirm = (
    '//*[@class="el-button taskInitial-msg-closedVisible el-button--primary el-button--mini"]')

"""
富集混合样本列表页的元素
"""
# 点击样本筛选按钮
wkfj_workflow_search = (
    '//*[@class="el-button btn-sample-select el-button--primary el-button--mini"]')

# 点击LIMS号搜索框
wkfj_workflow_search_lims = (
    '//*[@class="sampleId-lims-input el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input')

# 右侧展开弹框后，点击输入框
wkfj_workflow_search_lims_value = (
    '//*[@class="sampleId-lims-input el-textarea el-input--medium"]//textarea')

# 点击确定按钮
wkfj_workflow_search_lims_confirm = (
    '//*[@class="el-drawer__body"]//button[@class="el-button el-button--primary el-button--medium"]')

# 点击最外层的确定按钮
wkfj_workflow_search_confirm = (
    '//*[@class="el-dialog el-dialog--center dialog-sample-search"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]')
