# 各模块配置信息
# *************#
from common.all_path import pathologycheck_file_path, sampleprocessing_file_path, hstq_file_path, csps_file_path, \
    wkgj_file_path, wkfj_file_path, wkdl_sr_file_path, wkdl_non_sr_file_path, sj_file_path, esyjy_file_path, \
    mgmt_file_path, ybrk_file_path, report_basic_info_process_path, zpy_file_path, app_a_file_path, \
    cyclization_file_path, postcyclmix_file_path, dnbpremix_file_path, hd_sj_file_path, wkdl_hdsr_file_path
from common.xlsx_excel import write_excel_xlsx_by_openpyxl

# #样本接收模块生成样本数量
# specimen_list = {'FFPE白片': 8, 'EDTA抗凝血': 8, '骨冷冻组织': 8, 'DNA文库': 8, '外部血浆': 8,'cfDNA文库':2}
specimen_list = {'FFPE白片': 1, 'EDTA抗凝血': 1, '骨冷冻组织': 2, 'DNA文库': 1, '外部血浆': 1,'cfDNA文库':1}

"""
数据库配置
"""
# 表名

# 样本处理结果表
preparation_result = 'exp_preparation_result_t'

# 提取结果表
extraction_result = 'exp_extraction_result_t'

# 破碎结果表
ultrafrac_result = 'exp_ultrafrac_result_t'

# 构建结果表
libconstruction_result = 'exp_libconstruction_result_t'

# 富集结果表
pooling_result = 'exp_pooling_result_t'

# 定量结果表
libquant_result = 'exp_libquant_result_t'

# 质谱仪上机明细表
massspectro_item = 'exp_mass_spectro_item_t'

#APP-A结果表
appa_result='exp_appa_result_t'

#环化结果表
cyclization_result='exp_cyclization_result_t'

#环化后混合结果表
postcyclmix_result='exp_postcyclmix_result_t'

#DNB制备结果表
dnbpremix_result='exp_dnbpostmix_result_t'

def create_lab_excel():
    """
    新建各实验节点的Excel记录结果表样本下一步流程
    """
    all_laboratorys = ['病理检验', '样本处理', '核酸提取', '超声破碎', '文库构建', '文库富集', '文库定量', '上机', '21基因分析', 'MGMT', '样本入库',
                       '写入报告样本', '质谱仪上机','APP-A','环化','环化后混合','DNB制备']

    value = [["lims号", "实验室号", "当前节点", "任务单号"]]  # 其他
    HUADASJ = [["lims号", "文库名称", "当前节点", "任务单号"]]
    value1 = [["lims号", "上机分组号", "当前节点", "任务单号"]]  # 上机
    value2 = [["lims号", "文库名称", "当前节点", "任务单号"]]  # 定量sr
    value3 = [["lims号", "文库名称", "当前节点", "任务单号"]]  # 定量非sr
    value4 = [["lims号", "文库名称", "当前节点", "任务单号"]]  # 定量非sr
    write_excel_xlsx_by_openpyxl(pathologycheck_file_path, all_laboratorys[0], value)  # 病理检验数据流转Excel
    write_excel_xlsx_by_openpyxl(sampleprocessing_file_path, all_laboratorys[1], value)  # 样本处理数据流转Excel
    write_excel_xlsx_by_openpyxl(hstq_file_path, all_laboratorys[2], value)  # 核酸提取数据流转Excel
    write_excel_xlsx_by_openpyxl(csps_file_path, all_laboratorys[3], value)  # 超声破碎数据流转Excel
    write_excel_xlsx_by_openpyxl(wkgj_file_path, all_laboratorys[4], value)  # 文库构建数据流转Excel
    write_excel_xlsx_by_openpyxl(wkfj_file_path, all_laboratorys[5], value)  # 文库富集数据流转Excel
    write_excel_xlsx_by_openpyxl(wkdl_sr_file_path, all_laboratorys[6], value3)  # 文库定量sr样本数据数据流转Excel
    write_excel_xlsx_by_openpyxl(wkdl_hdsr_file_path, all_laboratorys[6], value4)  # 华大文库定量sr样本数据数据流转Excel
    write_excel_xlsx_by_openpyxl(wkdl_non_sr_file_path, all_laboratorys[6], value2)  # 文库定量非sr数据数据流转Excel
    write_excel_xlsx_by_openpyxl(sj_file_path, all_laboratorys[7], value1)  # 上机数据流转Excel
    write_excel_xlsx_by_openpyxl(hd_sj_file_path, all_laboratorys[7], HUADASJ)  # 华大上机数据流转Excel
    write_excel_xlsx_by_openpyxl(esyjy_file_path, all_laboratorys[8], value)  # 21基因分析数据流转Excel
    write_excel_xlsx_by_openpyxl(mgmt_file_path, all_laboratorys[9], value)  # MGMT数据流转Excel
    write_excel_xlsx_by_openpyxl(ybrk_file_path, all_laboratorys[10], value)  # 样本入库数据流转Excel
    write_excel_xlsx_by_openpyxl(report_basic_info_process_path, all_laboratorys[11], value)  # 写入报告样本数据流转Excel
    write_excel_xlsx_by_openpyxl(zpy_file_path, all_laboratorys[12], value)  # 质谱仪样本数据流转Excel
    write_excel_xlsx_by_openpyxl(app_a_file_path, all_laboratorys[13], value)  # APP-A样本数据流转Excel
    write_excel_xlsx_by_openpyxl(cyclization_file_path, all_laboratorys[14], value4)  # 环化样本数据流转Excel
    write_excel_xlsx_by_openpyxl(postcyclmix_file_path, all_laboratorys[15], value4)  # 环化后混合样本数据流转Excel
    write_excel_xlsx_by_openpyxl(dnbpremix_file_path, all_laboratorys[16], value4)  # DNB制备样本数据流转Excel


if __name__ == '__main__':
    create_lab_excel()
