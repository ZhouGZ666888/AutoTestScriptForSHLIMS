# -*- coding: utf-8 -*-
# @Time    : 2021/11/12
# @Author  : guanzhong.zhou
# @File    : 样本接收列表模块元素定位


"""
样本接收首页元素
"""
# 查询按钮，元素定位
search_btn = (
    '.filter-container .baseClass-btn-search')
# 查询框，输入订单号文本框，元素定位
order_numb = (
    '.sampleReceiveList-dialogSearch-orderCode input')

# 搜索按钮，元素定位
search_confirm = (
    '.dialog-search .baseClass-btn-search')

# 选中查询结果，默认选中第一条
chioce_result = (
    '//div[@class="el-dialog el-dialog--center dialog-search"]/descendant::tbody/tr[1]')

# 订单查询弹框，选中查询结果点击编辑接样单按钮，元素定位
edit_sample_order = (
    '.dialog-search .dialog-footer .sampleReceiveList-dialogSearch-handleEdit')

'''
样本接收-订单信息
'''
# 检测产品选择弹框
test_item = (
    '//*[@class="inp sampleReceiveDetail-form-orderProductTList"]')

# 检测产品弹框，搜索文本录入
product_input = (
    '//*[@class="tableTree_info_search"]/descendant::input')
# 检测产品弹框，搜索按钮
product_search_btn = (
    '//*[@class="tableTree_info_search"]/descendant::button')
# 检测产品展开
open_product = (
    '//*[@class="tableTree_select"]/descendant::tbody/tr[1]/descendant::i')

# 检测产品展开后选择
choice_product = (
    '//*[@class="tableTree_select"]/descendant::td[descendant::span[text()="世和一号(Geneseeq Prime)"]]')

# 选择产品提示信息
tipInfo='.el-message-box__wrapper .el-message-box__btns button:nth-child(1)'

# 选择检测产品，关闭弹框，元素定位
close_button = (
    '//*[@class="el-dialog el-dialog--center dialog-test-product"]/descendant::button[child::span[text()="返 回"]]')

# 项目选择弹框
project_name_chioce = (
    '//*[@class="inp sampleReceiveDetail-form-orderProjectTList"]')

# 项目名称文本框，元素定位
project_name_input = (
    '//*[@class="sampleReceiveDetail-tableColDialogProject-id el-input el-input--small el-input-group el-input-group--prepend el-input--suffix"]/input')

# 项目查询搜索按钮
project_search_button = (
    '//*[@class="el-button baseClass-btnBaseClass-search el-button--primary el-button--small"]')

# 选择查询结果，默认选择第一条
chioce_project_result = (
    '//*[@class="dialog-table"]/div/div[2]/div[2]/table/tbody/tr[1]')
# 项目查询框，返回按钮
back_button = (
    '//*[@aria-label="所属项目"]/descendant::button[child::span[text()="返 回"]]')

'''
样本接收-样本明细(未审核)
'''
# 保存按钮
save_btn = (
    '.sample-receiving-module-card2 .baseClass-btn-handleSavaBefore')

# 编辑页面，全选样本标签，元素定位
all_chioce = (
    '.sample-receiving-module-card2 .vxe-table--fixed-left-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')
# 审核页面，全选样本标签，元素定位
review_all_chioce = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--fixed-left-wrapper"]/descendant::span[@title="全选/取消"]/span[2]')
# 添加样本按钮，元素定位
add_sample = (
    '//*[@class="el-button border_size sampleReceiveDetail-btn-addSample el-button--primary el-button--mini"]')
# 获取添加的样本（全部）
all_samples = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--main-wrapper"]/descendant::tbody/tr')
# 从全部样本中依次获取样本（单个）
one_by_one_samples = (
    '.sampleDetail_content .vxe-table--fixed-left-wrapper tbody tr:nth-child({}) td:nth-child(3)')

# 获取单个样本的样本类型值
one_sample_type = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--main-wrapper"]/descendant::tbody/tr[{}]/td[8]')

# 获取单个lims号值
one_lims_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--main-wrapper"]/descendant::tbody/tr[{}]/td[4]')

# 获取单个实验室号值
one_laboratory_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--fixed-left-wrapper"]/descendant::tbody/tr[{}]/td[3]')

# 获取实验室号列所有值
laboratory_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--fixed-left-wrapper"]/descendant::tbody/tr/td[3]')
# 获取lims号列所有值
lims_num = (
    '//*[@class="el-card box-card sample-receiving-module-card2 is-always-shadow"]/descendant::div[@class="vxe-table--main-wrapper"]/descendant::tbody/tr/td[4]')

# 复制样本，元素定位
copy_sample = (
    '//*[@class="el-button border_size sampleReceiveDetail-btn-copySample el-button--primary el-button--mini"]')

# 生成实验流程弹框按钮，元素定位
generateLibProcessVisible = (
    '//*[@class="el-button border_size generateLibProcessVisible-generateLibProcessVisible-btn3 el-button--primary el-button--mini"]')

# 实验流程弹框中选中全部样本
template_sample_all = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::tbody/tr')

# 获取实验流程弹框样本类型
template_sample_type = (
    '//div[@aria-label="实验流程配置/预设探针"]/descendant::tbody/tr[{}]/td[5]')

# 实验流程弹框中按个数选中样本
one_by_one_chioce_sample = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::tbody/tr[{}]')

# 实验流程模板按钮
laboratory_process_temp_btn = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::button[child::span[text()="实验流程模板"]]')

# 实验流程探针选择按钮
laboratory_process_planned_btn = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::button[child::span[text()="预设探针"]]')

# 探针选择弹框,默认选择第一条探针
laboratory_process_planned_chioce = (
    '//*[@class="el-dialog__wrapper dialog-sample-probe"]/descendant::tbody/tr[1]')

# 探针选择后点击确认按钮
laboratory_process_planned_comfirm = (
    '//*[@class="el-dialog__wrapper dialog-sample-probe"]/descendant::button[child::span[text()="确认"]]')

# 获取所有实验流程对象，安照名称进行选定
LibProcessVisible = (
    '//*[@class="el-dialog__wrapper dialog-next-step"]/descendant::tr/td/div/span[text()="{}"]')

# 选中实验流程后确认按钮
LibProcessVisible_btn = (
    '//*[@class="el-dialog__wrapper dialog-next-step"]/descendant::button[child::span[text()="确认"]]')

# 实验流程弹框全部流程生成后确认
generatelaboratoryprocess_btn = (
    '//*[@aria-label="实验流程配置/预设探针"]/descendant::button[child::span[text()="生成实验流程"]]')

# 选择样本项目，元素定位
project_name = (
    '//*[@class="el-button border_size sampleReceiveDetail-form-orderProjectTList el-button--primary el-button--mini"]')

# 样本类型选择按钮，元素定位
sample_TypeName = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-sampleTypeName el-button--primary el-button--mini"]')

# 样本类型选项弹框，查询录入文本框
original_specimen_type = (
    '//*[@class="el-dialog__wrapper dialog-sample-type"]/descendant::input')

# 样本类型选项弹框，查询按钮(isdisplayed判断)
search_type_button = (
    '//*[@class="el-dialog__wrapper dialog-sample-type"]/descendant::button[child::span[text()="搜索"]]')

# 样本类型选项弹框，选择查询结果,精确查找，选择第一条
chioce_search_result = (
    '//*[@class="el-dialog__wrapper dialog-sample-type"]/descendant::tbody/tr[1]')

# 样本类型选项弹框，选择确认
specimen_type_comfirm = (
    '//*[@class="el-dialog__wrapper dialog-sample-type"]/descendant::button[child::span[text()="确认"]]')

# 样本包装量，元素定位
sample_PkgAmt = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-samplePkgAmt el-button--primary el-button--mini"]')

# 样本包装量文本录入
sample_PkgAmt_input = (
    '//*[@aria-label="样本包装量"]/descendant::input')

# 样本包装量确认按钮
sample_PkgAmt_input_comfirm_btn = (
    '//*[@aria-label="样本包装量"]/descendant::button[child::span[text()="确 定"]]')

# 样本计量，元素定位
sample_amt = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-sampleAmt el-button--primary el-button--mini"]')

# 样本计量文本录入框
sample_amt_input = (
    '//*[@aria-label="样本计量"]/descendant::input')

# 样本计量文本录入确认
sample_amt_input_comfirm_btn = (
    '//*[@aria-label="样本计量"]/descendant::button[child::span[text()="确 定"]]')

# 运输条件，元素定位
transport_condition = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-transportConditionName el-button--primary el-button--mini"]')

# 运输条件选择，默认选第一条
transport_condition_chioce = ('/html/body/div[9]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]')

# 运输条件选择，确认按钮
transport_condition_comfirm_btn = ('/html/body/div[9]/div/div[3]/span/button[2]')

# 质检结果
qc_result = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-qcResult el-button--primary el-button--mini"]')

# 选择质检结果，默认第一条“合格”
qc_result_chioce = ('/html/body/div[10]/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]')

# 异常类型
exception_type = (
    '//*[@class="el-button border_size sampleReceiveDetail-tableCol-sampleRcvItemAbnormalityTList el-button--primary el-button--mini"]')

# 添加病理任务
add_pathology_worksheet = (
    '.button-list .btn-add-pathology-task')

# 选择HE病理任务HE
pathology_worksheet_HE = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="HE"]')

# 选择HE病理任务PD
pathology_worksheet_PD = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="PD-L1(28-8)"]')

# 批量提交审核
batch_submit_for_review = (
    '.sample-receiving-module-card2 .sampleReceiveDetail-formSampleReceive-mulitSubmit')

# 批量完成审核
batch_checked_for_review = (
    '//*[@class="el-button border_size sampleReceiveDetail-formSampleReceive-mulitChecked el-button--primary el-button--mini"]')

# 保存样本信息后，页面提示信息
save_info = (
    '.el-message.el-message--success')

#退出登录按钮
logout_btn='.navbar .right-menu div:nth-child(2) span'

#退出登录
logout_choice='//ul/li[child::span[text()="退出登录"]]'


# 切换待审核按钮
review_pending = (
    '//*[@class="el-radio sampleReceive-waitForChecked"]/span[1]')

# 批量审核，输入审核人账号密码，密码录入文本框，元素定位
password_inpt = (
    '//*[@class="signature-password el-input el-input--medium el-input-group el-input-group--prepend"]/descendant::input')

# 批量审核，输入账号密码弹框，下一步按钮，元素定位
next_step = (
    '//*[@aria-label="电子签名"]/descendant::button[child::span[text()="下一步"]]')

# 批量审核，审核理由文本输入框，元素定位
review_remarks = (
    '//*[@aria-label="审核备注"]/descendant::textarea')

# 批量审核，审核理由录入后确认按钮，元素定位
review_confirm = (
    '//*[@aria-label="审核备注"]/descendant::button[child::span[text()="确定"]]')
