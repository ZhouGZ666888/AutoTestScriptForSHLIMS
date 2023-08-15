# -*- coding: utf-8 -*-
# @Time    : 2022/02/22
# @Author  : guanzhong.zhou
# @File    : 样本通知消息列表元素定位
# -*-*************************************************************************************-*-

# ===================消息列表元素===========================

"""
消息列表元素
"""
# 列表页，新建发送按钮
add_send = (
    '.sample-list-header .baseClass-btn-add')

# 检索条件---样本号，文本框定位
check_by_sample_lims = (
    '.sample-list-header .right-list .sampleNotice-form-sampleIdLims input')

# 搜索按钮
search_btn = (
    '.sample-list-header .right-list .baseClass-btn-fetch')

# 选择关联样本，文本输入框
samplesearch_textarea = (
    '.choose-sample-dialog .dialog-choose-sample textarea')

# 选择关联样本弹框，下一步
samplesearch_textarea_next = (
    '.choose-sample-dialog .dialog-choose-sample .el-dialog__footer .baseClass-btn-next')

# 通知内容填入&发送文本表单定位
notice_info = (
    '.dialog-batch-notice .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .batchNotice-tableCol-noticeInfo')

# 通知内容填入&发送文本录入定位
notice_info_input = (
    '.dialog-batch-notice .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) .batchNotice-tableCol-noticeInfo input')

# 通知内容填入，确认发送按钮
comfirm_send_btn = (
    '.dialog-batch-notice .el-dialog__footer .baseClass-btn-confirm')

#消息列表
sample_list=(
    '.sample-notice-list .box-card .el-card__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1)')


# 消息列表，【状态】字段表达定位
sample_status = (
    '.sample-notice-list .box-card .el-card__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(8)')

# 消息列表，【是否已读】字段表达定位
sample_isRead = (
    '.sample-notice-list .box-card .el-card__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(9)')

"""
明细表样本通知弹框
"""
# 样本通知信息弹框
samplemsgnotice = (
    '.dialog-notice')

# 样本通知弹框，通知内容表单定位
samplemsgnotice_notice_msg = (
    '.dialog-notice .el-dialog__body .vxe-table--main-wrapper .vxe-table--body-wrapper tbody td:nth-child(3)')

# 样本通知弹框，已处理勾选框
process_checkbox = (
    '.dialog-notice .el-dialog__body #pane-0 .vxe-table--main-wrapper .vxe-table--body-wrapper tbody td:nth-child(7) span span')

# 样本通知弹框，提交按钮
samplemsgnotice_sumbit = (
    '.dialog-notice .el-dialog__footer .baseClass-btn-submit')
