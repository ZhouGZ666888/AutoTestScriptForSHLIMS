# -*- coding: utf-8 -*-
# @Time    : 2022/04/08
# @Author  : guanzhong.zhou
# @File    : 样本外送模块元素定位

"""
样本外送首页列表元素定位
"""
# 搜索按钮
search_btn = (
    '.app-container .filter-container .baseClass-btn-search')

# 搜索弹框申请单号录入文本
search_lims_task_id = (
    '.dialog-search .searchComponent-form-taskId input')

# 搜素弹框确认
search_confirm = (
    '.dialog-search .el-dialog__footer .baseClass-btn-confirm')

# 新增按钮
add_task = (
    '.app-container .filter-container .baseClass-btn-add')

##页面列表样本
sample_page_list = (
    '//*[@class="sample_receive_detail"]/descendant::tbody/tr')

# -*-*************************************************************************************-*-

"""
样本外送新建页面元素定位
"""
# 保存按钮元素定位
save_btn = (
    '.filter-container .sampleOutSendDetail-btn-save')

# 提交审核按钮元素定位
submit_btn = (
    '.filter-container .sampleOutSendDetail-btn-submit')

# 完成审核按钮元素定位
finishAudit_btn = (
    '.filter-container .sampleOutSendDetail-btn-finishAudit')

# 完成寄送按钮元素定位
sendfinish_btn = (
    '.filter-container .sampleOutSendDetail-btn-finish')

# 取样确认按钮元素定位
check_btn = (
    '.filter-container .sampleOutSendDetail-btn-check')

# ***********外送申请单详情***********

# 外送类型
outsend_type = (
    '.sample_receive_detail .sampleOutSendDetail-form-taskType input')

# 外送类型下拉值
outsend_type_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="{}"]]')

# 接收方
recipient = (
    '.sample_receive_detail .sampleOutSendDetail-form-recipient input')

# 接收方下拉值
recipient_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="患者家属"]]')

# 外送目的地地址
sendAddress = (
    '.sample_receive_detail .sampleOutSendDetail-form-sendAddress input')

# 寄送方式
sendMethod = (
    '.sample_receive_detail .sampleOutSendDetail-form-sendMethod input')

# 寄送方式下拉值选择
sendMethod_choice = (
    '//*[@class="el-select-dropdown el-popper"]/descendant::li[child::span[text()="快递"]]')

# 追踪信息*
trackingInfo = (
    '.sample_receive_detail .sampleOutSendDetail-form-trackingInfo input')

# 关联项目*
projectId = (
    '.sample_receive_detail .sampleOutSendDetail-form-projectId')

# 关联项目选择*
projectId_choice = (
    '//div[@class="el-scrollbar"]/descendant::li[child::span[text()="J022"]]')

# 审核人*
lastAuditedBy_btn = (
    '.sample_receive_detail .sampleOutSendDetail-form-lastAuditedBy')
# 审核人*
lastAuditedBy = (
    '.sample_receive_detail .sampleOutSendDetail-form-lastAuditedBy input')

#审核人选择
lastAuditedBy_choice=(
    '//div[@class="el-scrollbar"]/descendant::li[child::span[text()="周官钟"]]')

# ***********待选样本表***********

# 样本筛选
samplefilter = (
    '.sample_receive_detail .sampleList-btn-filter')

# 样本筛选弹框录入样本lims号
sampleIdLims_input = (
    '.dialog-sample-search .sampleSearchComponent-form-sampleIdLims input')

# Lims录入框
lims_input = (
    '.draw-sampleId-lims .sampleId-lims-input textarea')

# lims录入框确认按钮
lims_input_comfirm = (
    '.draw-sampleId-lims .drawer-footer .el-button--primary')

# 搜索弹框确认按钮
detail_search_comfirm = (
    '.dialog-sample-search .el-dialog__footer .baseClass-btn-confirm')

# 全选按钮
detail_all_choice = (
    '.out_content_table .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 添加至明细表
add_detail = (
    '.sample_receive_detail .sampleList-btn-addToDetail')

# 进入明细表
to_detail = (
    '.sample_receive_detail .sampleList-btn-goSchedule')

# 外送样本明细表全选按钮
outsend_detail_all_choice=(
    '.app-container div:nth-child(4)  .vxe-table--main-wrapper .vxe-table--header-wrapper table thead .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

#外送样本明细表是否全样外送按钮
is_allOutsend=(
    '.box-card .sample_receive_detail .baseClass-btn-isSendFull')

#外送样本明细表是否全样外送下拉选项
is_allOutsend_choice=(
    '//ul/li[@class="el-dropdown-menu__item" and text()="全部外送"]')

# 明细表申请单号
detail_task_id = (
    '.clearfix div span:nth-child(1)')

# 任务单状态
detail_task_status = (
    '.clearfix div span:nth-child(3)')

#*********************************************************


"""
待办任务，样本外送相关元素
"""
#样本外送审核tab页
outsendsample_tab=(
    '#tab-third')
#样本外送审核进入按钮
outsend_review_btn=(
    '.el-tabs__content #pane-third .el-table__body-wrapper tbody tr:nth-child(1) .baseClass-btn-enter')




# 退出登录按钮
logout_btn = '.navbar .right-menu div:nth-child(2) span'

# 退出登录
logout_choice = '//ul/li[child::span[text()="退出登录"]]'