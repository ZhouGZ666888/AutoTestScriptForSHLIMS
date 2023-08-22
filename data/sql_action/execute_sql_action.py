# -*- coding: utf-8 -*-
# @File    : 系统中各模块执行SQL语句汇总


# 病历模块查询数据库是否存在相同身份证
bl_sql = "SELECT count(*) from crm_patient_t where identification_no ='{}';"

# 订单模块查询订单表是否存在新建订单号
order_isexists_sql = "select count(*) from order_info_t where order_code='{}'; "
# 接样写入备注
ybjs_sql = "UPDATE sample_receive_item_t set remarks='自动化测试数据' where order_code='{}';"

# 获取sr样本lims号
get_sr_sample_lims = "select sample_id_lims from sample_receive_item_t where order_code='{}' and  sample_type in ('C2016120700002','C2017042000002');"

# 修改获取sr样本的外部样本编号
set_sr_sample_id_external = "update sample_receive_item_t set sample_id_external='{}' where sample_id_lims='{}';"

# 样本处理明细表,更新盒内位置
ybcl_detail_sql = "UPDATE exp_preparation_item_t set position_in_box=1 where task_id='{}';"

# 样本处理结果表，获取样本lims号和实验室号
ybcl_detail_sql2 = "SELECT t1.sample_id_lims,t1.sample_main_lab_code from sample_id_lab_v t1 WHERE t1.sample_id_lims in (SELECT t2.sample_id_lims from exp_preparation_result_t t2 where t2.task_id ='{}');"

# 核酸提取明细表
hstq_detail_sql = "UPDATE exp_extraction_item_t set actual_sample_amt={},actual_sample_pkg_amt=1 where task_id='{}';"

# 查询提取明细表样本lims号
hstq_detail_sql2 = "SELECT sample_id_lims from exp_extraction_item_t where task_id='{}';"

# 核酸提取结果表,产物Qubit浓度、产物Nanodrop浓度、OD260/280、OD260/230
hstq_result_sql = "UPDATE exp_extraction_result_t set nanodrop_consistence_amt=5,od260_280=5,od260_230=5,consistence_amt=5 where task_id='{}';"

# 超声破碎明细表lims号
csps_detail_sql = "SELECT sample_id_lims from exp_ultrafrac_ITEM_t where task_id='{}';"

# 超声破碎结果表
csps_result_sql = "UPDATE exp_ultrafrac_result_t set position_in_tmp_box=1 where task_id='{}';"

# 文库构建明细表
# 是否选大小、使用体积、建库进入量、补水体积、余样体积、余样总量
wkgj_detail_sql1 = "UPDATE exp_libconstruction_item_t set selected_bigness=0 where task_id='{}';"

# 构建明细表查询样本lims号
wkgj_detail_sql2 = "SELECT sample_id_lims from exp_libconstruction_item_t where task_id='{}';"

# 修改构建明细表核酸浓度
wkgj_detail_sql3 = "UPDATE exp_libconstruction_item_t SET actual_consistence_amt = 5 WHERE task_id = '{}';"

# 修改文库构建---样本进入量值
wkgj_detail_sql4 = "UPDATE exp_libconstruction_item_t set used_total_amt =50 WHERE task_id = '{}';"

# 修改文库构建---核酸总量
wkgj_detail_sql5 = "UPDATE exp_libconstruction_item_t SET actual_total_amt = 450 WHERE task_id = '{}';"

# 修改文库构建---余样体积和余样总量
wkgj_detail_sql6 = "UPDATE exp_libconstruction_item_t SET remaining_volume_amt = 10,remaining_total_amt=10 WHERE task_id = '{}';"

# 文库构建结果表
# 大小片段分离后浓度、连接后纯化浓度、盒内位置
wkgj_result_sql1 = "UPDATE exp_libconstruction_result_t set consistence_amt=10,purification_consistence_amt=10,position_in_tmp_box=1 where task_id='{}';"

# 查当前结果表的result_id
wkgj_result_sql2 = "SELECT result_id from exp_libconstruction_result_t  WHERE task_id='{}';"

# 根据result_id修改文库构建‘cfdna结果扩展表’---‘fragment_consistence_amt’字段【片段分离后浓度（ng/μL）】值，即页面文库浓度ng/μL*值
wkgj_result_sql3 = "UPDATE exp_libconstruction_cl_result_t set fragment_consistence_amt =10 WHERE result_id in (SELECT result_id from exp_libconstruction_result_t  WHERE task_id='{}');"
# 录入结果表96孔板编号
wkgj_result_sql4 = "UPDATE exp_libconstruction_cl_result_t set well_plates_code ='zx1' WHERE result_id = '{}';"

# 查询一条最新的样本盒，作为96孔板编号写入数据库
wkgj_result_sql5 = "UPDATE exp_libconstruction_result_t set well_plates_code=(SELECT  box_name from  sample_box_info_t ORDER BY creation_date DESC LIMIT 1) WHERE task_id='{}';"
# 构建设置Adapter(index_id )
wkgj_result_sql6 = "UPDATE  exp_libconstruction_result_t set index_id ='1' WHERE task_id='{}';"

# 文库富集明细表,获取lims号
wkfj_detail_sql1 = "SELECT sample_id_lims from exp_pooling_item_t WHERE task_id = '{}';"

# APP-A获取明细表样本lims号
app_get_lims = "SELECT sample_id_lims FROM exp_appa_item_t WHERE task_id = '{}' ;"

# APP-A更新分管样本文库包装量
updata_detail_sample_pkg_amt = "UPDATE exp_appa_item_t set actual_sample_pkg_amt=1 where actual_sample_pkg_amt IS NULL " \
                               "AND " \
                               "task_id ='{}';"
# APP-A更新结果表产物包装量
updata_result_sample_pkg_amt = "UPDATE exp_appa_result_t set sample_pkg_amt=1 where  task_id ='{}';"

# 环化更新自动计算数据
cyclization_update = "UPDATE exp_cyclization_item_t SET fragment_len =150 WHERE task_id ='{}';UPDATE " \
                     "exp_cyclization_result_t SET " \
                     "fragment_len =150,sample_type_id='C2023042500008',used_volume_amt=5, sup_volume_amt=5 ," \
                     "consistence_amt =5,volume_amt=5 ,cyclization_data_amt=1.51,next_step='01' WHERE task_id ='{}';"

# 环化获取明细表lims号
cyclization_get_lims="SELECT sample_id_lims from exp_cyclization_item_t WHERE task_id='{}';"

# 环化下一步
cyclization_next_step="SELECT sample_id_lims, cyclization_name, CASE WHEN next_step = '01' THEN '环化后混合'WHEN next_step = '02' THEN " \
 "'DNB制备'ELSE next_step END AS next_step FROM {}  WHERE task_id = '{}';"




# 文库定量明细表
# 获取样本总数
wkdl_detail_sql1 = "SELECT count(*) from exp_libquant_item_t WHERE task_id = '{}';"

# 设置明细表余样本包装量
wkdl_detail_sql2 = "UPDATE exp_libquant_item_t set remaining_sample_pkg_amt=1 WHERE task_id = '{}';"

# 数据库获取定量明细表lims号
wkdl_detail_sql3 = "SELECT sample_id_lims from exp_libquant_item_t WHERE task_id = '{}';"

# 文库定量结果表
# 获取样本总数
wkdl_result_sql1 = "SELECT count(*) from exp_libquant_result_t WHERE task_id ='{}';"

# 上机
# 浓度调整前样本明细
# 更新浓度调整前样本明细【取样】值
sj_detail_before_concentration_sql1 = "UPDATE exp_sequencing_item_t SET used_volume_amt =1,preinstall_lane_num=3 WHERE task_id='{}';"

# 获取lims样本号
sj_detail_before_concentration_sql2 = "SELECT sample_id_lims from exp_sequencing_item_t WHERE task_id='{}';"

# 浓度调整后样本明细
# 设置调整后摩尔浓度,余样包装量
sj_detail_after_concentration_sql1 = "UPDATE exp_sequencing_item_adjusted_t SET molar_concentration=1 WHERE task_id='{}';"
# 设置余样包装量
sj_detail_after_concentration_sql3 = "UPDATE exp_sequencing_item_adjusted_t SET remaining_sample_pkg_amt=1 WHERE task_id='{}';"

# 获取样本lims号
sj_detail_after_concentration_sql2 = "SELECT sample_id_lims from exp_sequencing_item_adjusted_t WHERE task_id='{}';"

# 21基因
# 明细表设置样本浓度、体积、总量
twentyonegene_sql1 = "UPDATE exp_twentyonegene_item_t set actual_consistence_amt=5,actual_volume_amt=10,actual_total_amt=50 WHERE task_id='{}';"

# 结果表设置进入体积、进入总量
twentyonegene_sql2 = "UPDATE exp_twentyonegene_result_t set volume_amt=5,total_amt=25 WHERE task_id='{}';"

# MGMT
# MGMT明细表获取样本lims号
mgmt_sql1 = "SELECT sample_id_lims from exp_mgmt_item_t WHERE task_id='{}';"
# MGMT明细表设置包装余量
mgmt_sql3 = "UPDATE exp_mgmt_item_t set remaining_sample_pkg_amt=1 where task_id='{}';"

# MGMT结果表录入转化后浓度、进入总量、总油滴数、FAM信号油滴数、HEX信号油滴数
mgmt_sql2 = "UPDATE exp_mgmt_result_t set consistence_amt=5,ddpcr_used_total_amt=10,total_oil_drop=5,fam_sig_oil_drop=5,hex_sig_oil_drop=5 where task_id='{}';"

# 到数据库中查询需要条件的原始样本号：按照FFPE白片，接样直接到提取的流转表来搜索数据库满足条件的原始样本号，即满足提取待选表的sql。
# 如果需要检索具体的样本，在本sql最后面加上该条件即可：---AND t.previous_sample_id_lims = 'GS2110200044'
lzb_get_sql1 = """SELECT  t.previous_sample_id_lims AS sampleIdLims, t3.sample_id_lab AS sampleIdLab FROM 
sample_info_t t 
INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') 
INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON 
(t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id) 
WHERE t.is_valid = '1' AND t.current_step = '{}' AND t.workflow_status = '04' AND t.sample_status IS NULL """

# 通过系统检索出，F，T大类的样本，在流转表设置病理任务，否则无法设置,('C2012120800006','C2012120800003')分别代表F,T大类,且当前还没有设置过病理任务的
lzb_get_sql2 = """SELECT DISTINCT t.previous_sample_id_lims AS sampleIdLims, t3.sample_id_lab AS sampleIdLab FROM 
sample_info_t t 
INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') 
INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON 
(t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id)
WHERE t.is_valid = '1' AND t.current_step = '{}' AND t.workflow_status = '04' AND t.sample_status IS NULL AND 
tp.sample_type IN ('C2012120800006','C2012120800003') AND t.previous_sample_id_lims NOT IN (SELECT tpa.sample_id_lims 
FROM pathology_sample_task tpa WHERE tpa.is_valid='1')
"""

# 通过系统检索出，接样节点样本是库内的，用于接样出库(样本类型是FF白片的)
lzb_get_sql3 = """SELECT sample_id_lims,order_code FROM sample_info_t  WHERE previous_sample_id_lims IS NULL 
AND sample_status='01' AND workflow_status= '01' AND current_step ='reception' AND sample_type='C2012120800006'"""

# 通过系统检索出，可以在流转表修改建库信息的样本，修改建库信息就可以修改富集信息。
lzb_get_sql4 = """SELECT t.original_sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE '%D00%' AND 
t.sample_status IS NULL AND workflow_status ='02'"""

# 通过系统检索出，在库内的富集/定量实体样本
lzb_get_sql5 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'FJ%' AND t.sample_status ='01' AND workflow_status ='01'"""
lzb_get_sql6 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'ZC%' AND t.sample_status ='01' AND workflow_status ='01'"""

# 通过系统检索出，库内的样本
ybck_get_sql5 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' AND workflow_status ='01'"""

# 数据库获取实验流程结果表下一步流向
next_step_sql = "SELECT  DISTINCT previous_sample_id_lims,sample_id_lab_core,current_step FROM sample_info_t WHERE (previous_sample_id_lims IN ( SELECT sample_id_lims FROM {} WHERE task_id = '{}') AND is_valid = '1')"

# 数据库获取富集结果表下一步流向
fj_next_step = "SELECT sample_id_lims, pooling_name, next_step_name FROM {}  WHERE task_id = '{}';"

# 数据库获取定量结果表下一步流向
dl_next_step = "SELECT sample_id_lims,sqc_group_num,next_step_name FROM {}  WHERE task_id='{}';"

# 样本项目信息修改筛选符合条件项目信息
project_id = "SELECT project_id FROM bas_project_info_t WHERE  ( project_id like 'P%' OR project_id like 'M%' or project_id like 'Y%')and is_valid='1';"

# 样本项目信息修改后，数据库获取修改后的样本项目信息
sampleProId = "SELECT project_id,is_valid from exp_result_sample_project_t  WHERE sample_id_lims ='{}';"

# 样本消息通知，获取待选表样本，此处以核酸提取待选表为例
sampleMsgNotice = "SELECT DISTINCT t.previous_sample_id_lims,t.estimated_generated_time FROM sample_info_t t INNER JOIN sample_receive_item_t t2 ON (t.original_sample_id_lims = t2.sample_id_lims AND t.is_valid = '1') INNER JOIN sample_info_t tp ON (t.previous_sample_id_lims = tp.sample_id_lims) LEFT JOIN sample_id_lab_v t3 ON (t.previous_sample_id_lims = t3.sample_id_lims) LEFT JOIN bas_sample_type_t t4 ON (tp.sample_type = t4.sample_type_id) WHERE t.is_valid = '1' AND t.current_step = 'extraction' AND t.workflow_status = '04' AND t.sample_status IS NULL  ORDER BY t.estimated_generated_time DESC limit 1;"

# 在出库列表中，搜索库内样本
ybck_get_sql1 = """SELECT t.sample_id_lims FROM sample_info_t t WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' ORDER BY t.creation_date DESC"""

# 接样样本出库的sql
ybck_get_sql2 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND t2.project_id IS NOT NULL
AND workflow_status ='01' AND t.original_sample_id_lims=t.sample_id_lims AND sample_type='C2012120800006'"""

# 查询提取节点可出库的样本
ybck_get_sql3 = """SELECT t.sample_id_lims FROM sample_info_t t
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='extraction' 
AND t2.project_id IS NOT NULL"""

# 查询富集节点可出库的样本
ybck_get_sql4 = """SELECT t.libquant_lims_id FROM sample_info_t t 
LEFT JOIN exp_result_sample_project_t t2 ON (t.sample_id_lims=t2.sample_id_lims)
WHERE t.sample_id_lims LIKE 'GS%' AND t.sample_status ='01' 
AND workflow_status ='01' AND t.current_step='libquant' 
AND t2.project_id IS NOT NULL"""

# 样本/盒移位模块，对样本进行移库操作，查询数据库中已有样本，取10条样本进行查询，查询结果大于等于查询条件（10）
yk_sample_info = """
SELECT T.sample_id_lims AS sampleIdLims,T.position_in_box AS positionInBox,t2.sample_type_name AS sampleTypeName,
t5.box_name AS boxName,t7.position_code AS positionCode,t7.storage_name AS storageName,tv.sample_id_lab AS sampleIdLab,t8.dt_name_cn AS storageTypeName,t5.position_in_drawer AS positionInDrawer,T.pooling_lims_id AS poolingLimsId FROM
	sample_info_t
	T LEFT JOIN sample_id_lab_v tv ON ( T.sample_id_lims = tv.sample_id_lims )
	LEFT JOIN bas_sample_type_t t2 ON ( T.sample_type = t2.sample_type_id )
	LEFT JOIN bas_dictionary_t t3 ON ( t3.dt_code = T.sample_amt_unit AND t3.dt_type = 'meterage_unit' )
	LEFT JOIN bas_dictionary_t t4 ON ( t4.dt_code = T.sample_pkg_amt_unit AND t4.dt_type = 'packing_unit' )
	LEFT JOIN sample_box_info_t t5 ON ( T.box_id = t5.box_id )
	LEFT JOIN sample_storage_info_t t6 ON ( t6.storage_id = t5.storage_id )
	LEFT JOIN sample_storage_info_t t7 ON ( t6.parent_id = t7.storage_id )
	LEFT JOIN bas_dictionary_t t8 ON ( t7.storage_type = t8.dt_code AND t8.dt_type = 'storage_type' ) 
WHERE
	T.is_valid = '1' AND T.sample_status = '01' AND T.sample_pkg_amt >= 0 AND (( t7.storage_type = '01' ) OR (t7.storage_type = '00' AND EXISTS ( SELECT 1 FROM sample_storage_user_t ssu WHERE ssu.is_valid = '1' AND ssu.storage_id = t7.storage_id AND ssu.user_id ='zhouguanzhong' ) ) ) AND t7.storage_type = '00' AND t5.box_name = '自动化测试用(勿删)'  ORDER BY T.mod_date DESC LIMIT 10 OFFSET 0;
"""

# 移库样本查询结果
yk_sample_search = """
SELECT T.sample_id_lims AS sampleIdLims,T.position_in_box AS positionInBox,t2.sample_type_name AS sampleTypeName,
t5.box_name AS boxName,t7.position_code AS positionCode,t7.storage_name AS storageName,tv.sample_id_lab AS sampleIdLab,t8.dt_name_cn AS storageTypeName,t5.position_in_drawer AS positionInDrawer,T.pooling_lims_id AS poolingLimsId FROM
	sample_info_t
	T LEFT JOIN sample_id_lab_v tv ON ( T.sample_id_lims = tv.sample_id_lims )
	LEFT JOIN bas_sample_type_t t2 ON ( T.sample_type = t2.sample_type_id )
	LEFT JOIN bas_dictionary_t t3 ON ( t3.dt_code = T.sample_amt_unit AND t3.dt_type = 'meterage_unit' )
	LEFT JOIN bas_dictionary_t t4 ON ( t4.dt_code = T.sample_pkg_amt_unit AND t4.dt_type = 'packing_unit' )
	LEFT JOIN sample_box_info_t t5 ON ( T.box_id = t5.box_id )
	LEFT JOIN sample_storage_info_t t6 ON ( t6.storage_id = t5.storage_id )
	LEFT JOIN sample_storage_info_t t7 ON ( t6.parent_id = t7.storage_id )
	LEFT JOIN bas_dictionary_t t8 ON ( t7.storage_type = t8.dt_code AND t8.dt_type = 'storage_type' ) 
WHERE
	T.is_valid = '1' 
		AND  (strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1 OR strpos(t.sample_id_lims, '{}') >= 1) 
	AND T.sample_status = '01' AND T.sample_pkg_amt >= 0 AND (( t7.storage_type = '01' ) OR (t7.storage_type = '00' AND EXISTS ( SELECT 1 FROM sample_storage_user_t ssu WHERE ssu.is_valid = '1' AND ssu.storage_id = t7.storage_id AND ssu.user_id ='zhouguanzhong' ) ) ) AND t7.storage_type = '00' AND t5.box_name = '自动化测试用(勿删)'  ORDER BY T.mod_date DESC LIMIT 10 OFFSET 0;
"""
# 质谱仪修改样本“检测项目”“复溶液”值
Massspectr = "update exp_mass_spectro_item_t set re_solution='01',detection_item='01' ," \
             "polypeptide_concentration_amt=5,polypeptide_total_amt=110 ,remaining_volume_amt=5 where task_id='{}';"
# 构建明细表查询样本lims号
Massspectr_sample_no = "SELECT sample_id_lims from exp_mass_spectro_item_t where task_id='{}';"
