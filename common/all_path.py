import os
import time

dir_name_file = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件目录路径
# os.path.abspath(__file__)获取文件路径，脚本的完整路径
dir_name = os.path.dirname(dir_name_file)  # 当前工程路径

# 指定输出图片到目录
log_path = os.path.join(os.path.join(dir_name, "output"), 'logs')

# 指定输出图片到目录
img_path = os.path.join(os.path.join(dir_name, "output"), 'img')

# 指定输出截图文件到目录
fileshot = os.path.join(os.path.join(os.path.join(dir_name, "output"), "wordFile"), "回归测试记录{}.docx").format(
    time.strftime('%Y%m%d', time.localtime(time.time())))
# print(fileshot)

# 测试文件路径
file_path = os.path.join(dir_name, 'data')

# 测试报告文件路径
report_path = os.path.join(dir_name, "report")
# print(report_path)
# 指定用例路径
case_path = os.path.join(os.path.join(dir_name, "testcase"))
# print(case_path)
# 指定用例路径

case_xls_path = os.path.join(os.path.join(dir_name, 'data'), '测试用例表.xlsx')
# print(case_xls_path)
# 指定用例路径
conffile_path = os.path.join(os.path.join(dir_name, "data"))

# 系统中生成、下载等临时文件存储路径
excel_doc_file_path = os.path.join(os.path.join(dir_name, "data"), 'download_file')

# ===========================sql执行数据================================
report_views_refresh_sql = os.path.join(os.path.join(dir_name, "data"), 'report_view_refresh.txt')  # 配置文件路径
# 批量粘贴盒内位置导入文件
position_in_box_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                    'position_in_box_lims.xlsx')

# ===================以下是测试中用的临时yaml数据=============================
# 配置文件路径
testdata_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'logindata.yaml')

# 病理信息记录文件
medicalinfo_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'medicalInfo.yaml')

# 临时记录数据
sampledata_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'sampledata.yaml')

# 记录订单号文件
orderNub_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'MedicalOrderInfo.yaml')

# 记录接样的SR样本文件
SR_sample_for_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'SR_sample_for_import.yaml')

# 各实验流程存储明细表、结果表URL路径，以便浏览器直接调用直接访问
functionpageURL_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'), 'functionPage_url.yaml')

# 文库定量明细表，样本上机分组号临时数据
wkdl_sequencing_group_number = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'yaml_doc'),
                                            'wkdl_result_sequencing_group_number.yaml')

# ===================以下是测试流转数据用到的表格=============================

# 病历号记录表
medicalNumb_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                     'medicalNumb_id_lims.xlsx')

# 订单号记录表
order_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'order_id_lims.xlsx')

# 样本接收记录表
samplereceive_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                       'samplereceive_id_lims.xlsx')

# 病理检验待选表
pathologycheck_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                        'pathologycheck_id_lims.xlsx')

# 样本处理结果记录表
sampleprocessing_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                          'sampleprocessing_id_lims.xlsx')
# 核酸提取结果记录表
hstq_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'hstq_id_lims.xlsx')

# 超声破碎结果记录表
csps_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'csps_id_lims.xlsx')

# 文库构建结果记录表
wkgj_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'wkgj_id_lims.xlsx')

# 文库富集结果记录表
wkfj_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'wkfj_id_lims.xlsx')

# 文库定量结果记录表
wkdl_non_sr_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                     'wkdl_non_sr_id_lims.xlsx')

# 文库定量结果记录表
wkdl_sr_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'wkdl_sr_id_lims.xlsx')

# 文库定量华大sr样本结果记录表
wkdl_hdsr_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'wkdl_sr_huada_lims.xlsx')

# 上机结果记录表
sj_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'sj_id_lims.xlsx')

# 质谱仪记录表
zpy_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'zpy_id_lims.xlsx')

# 21基因记录表
esyjy_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'esyjy_id_lims.xlsx')

# MGMT结果记录表
mgmt_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'mgmt_id_lims.xlsx')

# APP-A样本记录表
app_a_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'appa_id_lims.xlsx')

# 环化环节样本记录表
cyclization_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                     'cyclization_lims_id.xlsx')

# 环节后混合环节样本记录表
postcyclmix_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                     'postcyclmix_lims_id.xlsx')

# DNB制备环节样本记录表
dnbpremix_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'dnbpremix_lims_id.xlsx')

# 样本入库类型样本lims号
ybrk_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'), 'ybrk_id_lims.xlsx')

# 报告模块基本信息处理，写入报告的上机和不上机样本记录表
report_basic_info_process_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'excel_doc'),
                                              'report_basic_info_process.xlsx')

# ===================以下是实验流转中，富集、定量、上机、报告、21基因等模块批量粘贴导入数据用到的表格和执行自动化上传文件的可执行文件=============================


# 文库富集明细表批量导入数据
wkfj_detail_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                       '文库富集-明细表批量粘贴导入E.xlsx')

# 文库富集结果表批量导入数据
wkfj_result_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                       '文库富集-结果表批量粘贴导入E.xlsx')

# 文库定量明细表SR数据批量导入数据
wkdl_detail_sr_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                          '定量-明细表SR数据批量粘贴导入E.xlsx')

# 文库定量明细表非SR数据批量导入数据
wkdl_detail_non_sr_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                              '定量-明细表非SR样本导入E.xlsx')

# 文库定量明细表单梯度SR数据批量导入数据
wkdl_detail_single_gradient_sr_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                                          '定量-单梯度SR样本导入模板E.xlsx')

# 文库定量明细表单梯度非SR数据批量导入数据
wkdl_detail_single_gradient_non_sr_import_path = os.path.join(
    os.path.join(os.path.join(dir_name, "data"), 'import_excel'), '定量-单梯度非SR样本导入模板E.xlsx')

# 文库定量结果表SR数据批量导入数据
wkdl_result_sr_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                          '定量-结果表SR样本导入模板E.xlsx')

# 文库定量结果表非SR数据批量导入数据
wkdl_result_non_sr_import_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                              '定量-结果表非SR样本导入模板E.xlsx')
# 文库定量结果表标准品表导入模板
wkdl_result_standard_sample_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                                '定量-结果表标准品表导入模板E.xlsx')

# 上机结果表FC质控结果表导入
sj_fc_quality_control_result = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                            '上机-结果表导入模板E.xlsx')
# 报告导入突变模板
mutation_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'), '突变上传模板.csv')

# 21基因分析结果表导入模板
twentyonegene_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                       '21基因批量粘贴导入模板.xlsx')

# 新建病历时用户身份证文件
identificationNo_file_path = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                          '自动化脚本用户身份证.xlsx')

# SR样本信息登记模块导入模板
sr_sample_imp_file = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'), 'SR样本信息导入模板.xlsx')

# SR样本信息登记模块子文库导入模板
sr_sample_sublibrary_imp_file = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                             'SR样本子文库导入模板.xlsx')

# 移库样本明细表导入模板
yk_sample_detail_imp_file = os.path.join(os.path.join(os.path.join(dir_name, "data"), 'import_excel'),
                                         '移库样本明细表.xlsx')
