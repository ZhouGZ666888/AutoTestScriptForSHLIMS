# -*- coding: utf-8 -*-
# @Time    : 2023/03/02
# @Author  : guanzhong.zhou
# @File    : 质谱仪上机元素定位
# -*-*************************************************************************************-*-

"""
质谱仪首页列表元素定位
"""
# 搜索按钮

search = '.filter-container .baseClass-btn-search'

# 搜索弹框lims号录入文本
search_lims_sample_num = '.commonTaskList-commonTaskListDialog-sampleIdLims input'

# 搜索弹框确认
search_confirm = '.dialog-search .dialog-footer .baseClass-btn-confirm'

# 新增按钮
add_sample_process_task = '.filter-container .baseClass-btn-add'

##页面列表样本
sample_page_list = '//*[@class="sample_receive_detail"]/descendant::tbody/tr'

"""
待选表元素定位
"""
# 任务类型选择框
task_type = '.createTask_content_choose .el-form--label-left > div:nth-child(1)  input'

# 任务类型下拉值选择(多肽上机)
task_type_choice = '.task-type-unique .el-select-dropdown__list li:nth-child(1)'

# 选择sop下拉框
select_sop = (
    '.createTask_content_choose .el-form--label-left > div:nth-child(2)  input')

# 选择sop下拉值,m默认选择第一条
select_sop_choice = (
    '.sopId-unique .el-select-dropdown__list .el-select-group li:nth-child(1)')

# 核对lims样本号按钮
check_lims_sample_num = (
    '.createTask_content_choose .commonTaskDetail-btn-judgeLims')

# 核对样本号文本录入框
check_lims_sample_number_textarea = (
    '.dialog-expMgmt-detail textarea')

# 核对lims样本号确认按钮，元素定位
check_lims_sample_number_confirm = (
    '.dialog-expMgmt-detail .dialog-footer .qcResult-btn-confirm')

# 待选列表全选按钮
all_choice = (
    '.vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-header--row .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 加入选中&保存按钮，元素定位
addSelect_or_save_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-submit')

# 进入明细表按钮，元素定位
enter_detail_list_btn = (
    '.commonTaskDetail-commonTaskDetailBtn-goSchedule')

# 页面成功提示信息
page_success_info = (
    '//*[@class="el-message el-message--success"]/descendant::p')

# 页面失败提示信息
page_failed_info = (
    '//*[@class="el-message el-message--success"]')

"""
质谱仪上机明细表元素定位
"""

# 列表全选按钮
detail_all_choice = (
    '.createTask_content_table .vxe-table--fixed-left-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 明细表批量入库类型下拉框
detail_batch_storage_type = (
    '.sampleDetail_header .massSpectroSchedule-btn-batchStorageType')

# 明细表批量入库类型下拉值
detail_batch_storage_type_choice = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="余样入库" and preceding-sibling::li[text()="不入库（样本用尽）"]]')



# 批量导入
import_btn = '.sampleDetail_header .button-list .massSpectroSchedule-btn-import'

#导入按钮
upload_sampleInfo_btn=(
    '.dialog-csv-import .el-dialog__body input')

#批量导入确认按钮
import_confirm_btn='.dialog-csv-import .el-dialog__footer .baseClass-btn-confirm'

# 批量数据
batchData = '.sampleDetail_header .button-list .baseClass-btn-batchData'

# 批量数据---液相柱
liquidColumn = '.massSpectroSchedule-formBatchData-liquidColumn input'

# 液相柱选择
liquidColumn_choice = '//span[contains(text(),"HILIC柱")]'

# 批量数据---包装余量
SamplePkgAmt = '.massSpectroSchedule-formBatchData-remainingSamplePkgAmt input'

# 批量数据---液质联用仪器号
lcmsModel = '.massSpectroSchedule-formBatchData-lcmsModel input'

# 液质联用仪器号选择
lcmsModel_choice = '//span[contains(text(),"Vanquish Flex-OE480")]'

#检测项目
detectionItem='.massSpectroSchedule-formBatchData-detectionItem input'

#计量余量
remainingVolumeAmt='.massSpectroSchedule-formBatchData-remainingVolumeAmt input'

#检测项目选择
detectionItem_choice='//span[text()="Lable-Free DDA"]'

# 批量数据---扫描模式
scanMethod = '.massSpectroSchedule-formBatchData-scanMethod input'

# 扫描模式选择
scanMethod_choice = '//span[contains(text(),"负离子模式")]'

# 批量数据确认按钮
confirm_btn = '.dialog-batch-data .el-dialog__footer .baseClass-btn-confirm'

# 确认上机
confirmSequencing = '.sampleDetail_header .massSpectroSchedule-btn-confirm'

#确认上机弹框确认
confirmSequencing_confirm='//p[contains(text(),"是否确认上机")]/parent::div/following-sibling::div/div/button'



# 生成samplesheet
sampleSheet = '.sampleDetail_header .massSpectroSchedule-btn-sampleSheet '

# 入库按钮
deposit_into_storage = (
    '.sampleDetail_header .massSpectroSchedule-btn-storage')

# 入库弹框全选按钮
storage_all_choice = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--header-wrapper .vxe-checkbox--icon.vxe-checkbox--unchecked-icon')

# 入库弹框选择入库类型下拉框
target_storage_type = (
    '.dialog-check-storage .checkStorageDialog-btn-targetLocation')

# 入库弹框选择入库类型下拉值（临时库）
target_storage_type_value = (
    '//ul[@class="el-dropdown-menu el-popper el-dropdown-menu--medium"]/descendant::li[text()="临时库"]')

# 入库弹框选择样本盒按钮
batch_paste_sample_box = (
    '.dialog-check-storage .checkStorageDialog-btn-selectBox')

# 入库弹框选择样本盒弹框target storage 搜索文本录入框
target_storage = (
    '.boxSearch-boxSearchDialogForm-boxName input')

# 入库弹框选择样本盒弹框t搜索按钮
select_sample_box_search = (
    '.dialog-box-search .baseClass-btn-search')

# 入库弹框选选择样本盒值，默认选择列表第一条数据
select_sample_box_choice = (
    '.dialog-box-search .el-dialog__body .el-table__body-wrapper tbody tr:nth-child(1)')

# 入库弹框选选择样本盒弹框，确认按钮
select_sample_box_comfirm = (
    '.dialog-box-search .dialog-footer .baseClass-btn-confirm')

# 入库弹框样本总数
all_select_sample_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr td:nth-child(7)')

# 入库弹框盒内位置
detail_position_in_box = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7)')

# 入库弹框盒内位置文本框
detail_position_in_box_input = (
    '.dialog-check-storage .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child({}) td:nth-child(7) input')

# 批量粘贴盒内位置
batch_copy_BoxPosition = (
    '.dialog-check-storage .checkStorageDialog-btn-batchCopyBoxPosition')

# 批量粘贴盒内位置确认按钮
batch_copy_BoxPosition_comfirm = (
    '.dialog-position-box .dialog-footer .baseClass-btn-confirm')

# 批量粘贴盒内位置文本录入
batch_copy_BoxPosition_input = (
    '.dialog-position-box textarea')

# 入库弹框下一步按钮
storage_next = (
    '.dialog-check-storage .dialog-footer .baseClass-btn-next')

# 提交
submit = '.sampleDetail_header .massSpectroSchedule-btn-submit'

# 提交弹框确认按钮
submit_comfirm = (
    '.dialog-commit .dialog-footer .baseClass-btn-confirm')

# 提交状态文本定位
detail_sumbit_status = (
    '.createTask_content .vxe-table--main-wrapper .vxe-table--body-wrapper tbody tr:nth-child(1) td:nth-child(15)')

#导出样本列表
export_btn='.sampleDetail_header .massSpectroSchedule-btn-export'

#保存结果
save_result='.row-bg .baseClass-btn-save'


# 任务单号
task_id = (
    '.createTask .clearfix div span:nth-child(1)')

# 任务单状态
task_status = (
    '.createTask .clearfix div span:nth-child(3)')