# -*- coding: utf-8 -*-
# @Time    : 2021/11/25
# @Author  : guoqi.dong
# @File    : 流转表元素定位
# -*-*************************************************************************************-*-

# ===================样本出库的元素如下===========================

"""
样本出库列表页的元素---LIMS号搜索
"""
# 点击搜索按钮
sample_ck_search = '//*[@class="el-button baseClass-btn-search el-button--primary el-button--medium"]'
# 点击LIMS样本号输入框
sample_ck_search_value = '//*[@class="outStorageSearch-form-sampleIdLims el-input el-input--medium el-input-group el-input-group--prepend el-input--suffix"]//input'
# 点击确定按钮
sample_ck_search_confirm = '//*[@class="el-dialog el-dialog--center dialog-out-storage-search"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

"""
样本出库列表页的元素---新建出库（接样节点）
"""
# 点击新建按钮
sampleReceive_ck_add_butoon = '//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]'
# 点击输入框，输入LIMS号
sampleReceive_ck_enter_value = '//*[@class="text-input el-textarea el-input--medium el-input--suffix"]//textarea'
# 输入完成，点击确定
sampleReceive_ck_enter_confirm = '//*[@class="el-dialog el-dialog--center"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
# 默认选择【样本接收】tab的全选样本按钮,css
sampleReceive_ck_allcheckbox = '#pane-reception .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'
# 点击【实验流程模板】按钮
sampleReceive_ck_piplane_button = '//*[@class="el-button el-button--primary el-button--mini"]//span[text()="实验流程模板"]'
# 选择提取-破碎模板
sampleReceive_ck_piplane_value = '//*[@class="el-dialog el-dialog--center multi-table-dialog"]//table[@class="vxe-table--body"]//span[text()="核酸提取-破碎"]'
# 点击确定按钮,css
sampleReceive_ck_piplane_confirm = '.dialog-next-step .multi-table-dialog .el-dialog__footer .dialog-footer .qcResult-btn-confirm '
# 点击【预设探针】按钮
sampleReceive_ck_probe_button = '//*[@class="el-button el-button--primary el-button--mini"]//span[text()="预设探针"]'
#搜索框录入搜索探针
search_input='.dialog-sample-probe input'
#搜索按钮
search_btn='.dialog-sample-probe .baseClass-btnBaseClass-search'
# 弹框中选择第一个探针
sampleReceive_ck_probe_value = '.dialog-sample-probe .dialog-table .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)'
# 点击确定按钮
sampleReceive_ck_probe_confirm = '.dialog-sample-probe .dialog-footer .qcResult-btn-confirm'
# 点击保留原项目信息按钮
sampleReceive_keep_project_button = '//*[@class="reception"]//following-sibling::div/button'
# 下拉框选择【保留】选项
sampleReceive_keep_project_value = '//*[@class="el-dropdown-menu__item reception-original-project1"]'
# 点击下一步按钮
sampleReceive_save_next_button = '//*[@class="el-button baseClass-btn-next el-button--primary el-button--medium"]'
# 出库理由弹框内编写信息
sample_ck_reason = '//*[@class="dialog-reason-textarea el-textarea el-input--medium"]//textarea'
# 点击确定按钮
sample_ck_reason_confirm = '//*[@class="el-dialog dialog-reason"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

"""
样本出库列表页的元素---新建出库（非接样，非混合节点）
"""
# 点击新建按钮
unsampleReceive_ck_add_butoon = '//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]'
# 点击输入框，输入LIMS号
unsampleReceive_ck_enter_value = '//*[@class="text-input el-textarea el-input--medium el-input--suffix"]//textarea'
# 输入完成，点击确定
unsampleReceive_ck_enter_confirm = '//*[@class="el-dialog el-dialog--center"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
# 点击【核酸提取】节点tab
hstq_tab_button = '//*[@id="tab-extraction"]'
# 勾选提取节点的全选样本按钮
hstq_ck_allcheckbox = '#pane-extraction .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'
# 点击是否需要破碎按钮
hstq_ck_isultrafrac_button = '//*[@id="pane-extraction"]//span[text()="是否需要破碎"]'
# 弹框中选择是破碎
hstq_ck_isultrafrac_value = '//*[@aria-label="是否需要破碎"]//div[text()="是"]'
# 点击确定按钮
hstq_ck_isultrafrac_confirm = '//*[@aria-label="是否需要破碎"]//button[@class="el-button el-button--primary el-button--mini"]'
# 点击最后步骤按钮
hstq_ck_laststep_button = '//*[@id="pane-extraction"]//button[@class="el-button el-button--primary el-button--mini" and span[text()="最后步骤"]]'
# 弹框中选择最后步骤为：上机
hstq_ck_laststep_value = '//*[@aria-label="最后步骤"]//td//div[text()="上机测序"]'
# 点击确定按钮
hstq_ck_laststep_confirm = '//*[@aria-label="最后步骤"]//button[@class="el-button el-button--primary el-button--mini"]'
# 点击上机目的按钮
hstq_ck_sequence_goal = '//*[@id="pane-extraction"]//button//span[text()="上机目的"]'
# 选择一般测序
hstq_ck_sequence_goal_value = '//*[@aria-label="上机目的"]//td//div[text()="一般测序"]'
# 点击确定按钮
hstq_ck_sequence_goal_confirm = '//*[@aria-label="上机目的"]//button//span[text()="确 定"]'
# 点击【是否保留原项目信息】按钮
hstq_ck_keep_project_button = '//*[@id="pane-extraction"]//following-sibling::div/button'
# 下拉框选择【保留】选项
hstq_ck_keep_project_value = '//*[@class="el-dropdown-menu__item extraction-original-project1"]'
# 点击下一步按钮
hstq_ck_save_next_button = '//*[@class="el-button baseClass-btn-next el-button--primary el-button--medium"]'
# 出库理由弹框内编写信息
hstq_ck_reason = '//*[@class="dialog-reason-textarea el-textarea el-input--medium"]//textarea'
# 点击确定按钮
hstq_ck_reason_confirm = '//*[@class="el-dialog dialog-reason"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'

# 出库审核人录入框
ckAuditor_box='.dialog-reason .el-dialog__body >div:nth-child(2)'
ckAuditor = '.dialog-reason .dialog-select-nextProcessorId input'
# 出库审核人下拉选择
ckAuditorChoice = '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="董国奇"]]'
"""
样本出库列表页的元素---新建出库（定量混合节点）
"""
# 点击新建按钮
libquantmixed_ck_add_butoon = '//*[@class="el-button baseClass-btn-add el-button--primary el-button--medium"]'
# 点击输入框，输入LIMS号
libquantmixed_ck_enter_value = '//*[@class="text-input el-textarea el-input--medium el-input--suffix"]//textarea'
# 输入完成，点击确定
libquantmixed_ck_enter_confirm = '//*[@class="el-dialog el-dialog--center"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
# 点击【文库富集】节点tab
libquantmixed_tab_button = '//*[@id="tab-libquant"]'
# 勾选定量节点的全选样本按钮
wkdl_ck_allcheckbox = '#pane-libquant .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--unchecked-icon'
# 点击【上机目的】按钮
wkdl_ck_sequence_goal_button = '//*[@id="pane-libquant"]//div[@class="poolingOut"]//div[@class="el-dropdown"]//button'
# 选择【一般测序】
wkdl_ck_sequence_goal_value = '//*[@x-placement="bottom-end"]//li[text()="一般测序"]'
# 点击【是否保留原项目信息】按钮
wkdl_ck_keep_project_button = '//*[@id="pane-libquant"]//following-sibling::div/button'
# 下拉框选择【保留】选项
wkdl_ck_keep_project_value = '//*[@class="el-dropdown-menu__item libquant-original-project1"]'
# 点击下一步按钮
wkdl_ck_save_next_button = '//*[@class="el-button baseClass-btn-next el-button--primary el-button--medium"]'
# 出库理由弹框内编写信息
wkdl_ck_reason = '//*[@class="dialog-reason-textarea el-textarea el-input--medium"]//textarea'
# 点击确定按钮
wkdl_ck_reason_confirm = '//*[@class="el-dialog dialog-reason"]//button[@class="el-button baseClass-btn-confirm el-button--primary el-button--medium"]'
