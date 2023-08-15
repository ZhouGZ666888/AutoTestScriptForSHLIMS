# import datetime
# import time
#
# import pyperclip
# import xlrd
# import yaml
#
# from common import read_yaml
# from common.all_path import *
# from openpyxl import load_workbook
#
# # from common.all_path import wkfj_import_path
# from common.sql import Get_Sql_Helper
# from common.xlsx_excel import read_excel_xlsx_list_col, write_excel_xlsx_by_openpyxl
# from conf.execute_sql_action import *
#
# s = ['病理检验', '样本处理', '核酸提取', '文库构建', '文库富集', '文库定量', '上机', '21基因分析', 'MGMT']
#
# # from selenium import webdriver
# # driver = webdriver.Chrome()
# # driver.get(r'C:\Users\admin\Desktop\2.html')
# #
# # strrs = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]').text
# # for i in s:
# #     if i in strrs:
# #         print(i)
# import openpyxl
#
#
# # sds = 'dsfdsfdsfsdf文库构建sfsf'
# # for i in s:
# #     if i in sds and i == '文库构建':
# #         print('yes')
#
#
# def write_excel_xlsx(path, sheet_name, value):
#     index = len(value)
#     workbook = openpyxl.Workbook()  # 新建工作簿（默认有一个sheet？）
#     sheet = workbook.active  # 获得当前活跃的工作页，默认为第一个工作页
#     sheet.title = sheet_name + '明细表数据'  # 给sheet页的title赋值
#     for i in range(0, index):
#         for j in range(0, len(value[i])):
#             sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))  # 行，列，值 这里是从1开始计数的
#     workbook.save(path)  # 一定要保存
#     print("xlsx格式表格写入数据成功！")
#
#
# book_name_xlsx = '测试工作簿.xlsx'
#
# sheet_name_xlsx = 'xlsx格式测试表'
#
# value3 = [["lims", "实验室号", "当前节点"]]
#
#
# # write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value3)
# def add_write_excel_xlsx(path, values):
#     data = openpyxl.load_workbook(path)
#
#     # 取第一张表
#     table = data.sheetnames[0]
#
#     table = data.active
#     print(table.title)  # 输出表名
#     nrows = table.max_row  # 获得行数
#     ncolumns = table.max_column  # 获得列数
#
#     # 注意行业列下标是从1开始的
#     for i in range(1, len(values) + 1):
#         for j in range(1, len(values[i - 1]) + 1):
#             table.cell(nrows + i, j).value = values[i - 1][j - 1]
#
#     data.save(path)
#
#
# value = [["lims号", "实验室号", "当前节点"]]
# values = [['Es', 'Xs', 'Cs'],
#           [7, 8, ],
#           ['e', 'f']]
# # add_write_excel_xlsx(book_name_xlsx,values)
#
#
# # order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
# # # print(lims_id[0][0])
# # print(order_nub[0][0])
#
# # lims_nub1 = read_excel_xlsx_list_col(all_path.hstq_file_path, 0, '当前节点')
# # print(lims_nub1)
# # lims_nub = read_excel_xlsx_list_col(all_path.""", 0, 'lims号')
# # print(lims_nub[0][0])
#
#
# # ssaa='Task number：WKFJ2021112600001'
# # print(ssaa[12:].strip())
#
# from conf.data.PageElemens.libraryEnrichment_ele import *
# from conf.data.import_excel import *
#
# # file_home = "./xls/modify/name.xlsx"
# # wb = load_workbook(filename=wkfj_import_path)  # 打开excel文件
# # sheets = wb.worksheets
# # ws = wb.active#print(sheet_ranges['A1'].value)  # 打印A1单元格的值
# # # 修改小明的出生日期
# # ws.cell(2,1,'niubi')
# # ws['A3'] = 'hello world2'
# # wb.save(wkfj_import_path)
#
# #
# # def get_rows_value(row):
# #     '''
# #     获取某一行的内容
# #     '''
# #     row_list = []
# #     sheet_name = openpyxl.load_workbook(wkfj_import_path)
# #     ws = sheet_name.active
# #     s = ws.rows[3]
# #     for i in ws[row]:
# #         row_list.append(i.value)
# #     return s
#
#
# #
# # if __name__ == '__main__':
# #     handle = get_rows_value(2)
# #     print(handle)
#
# # data = xlrd.open_workbook(wkfj_import_path)
# # tables = data.sheets()[0]
# # allrows = tables.nrows
# # vals = tables.row_values(1)
# # sa = chr(9)
# # import pandas as pd
# #
# # str = sa.join(map(str, vals))
# # pyperclip.copy(str)
# # print(str)
# # filename = r'that.txt'
# # raw_score = r'C:\Users\lenovo\Desktop\data1.xlsx'
# # # 读取excel保存成txt格式
# # excel_file = pd.read_excel(wkfj_import_path)
# # excel_file.to_csv(filename, sep=' ', index=False)
# # data = xlrd.open_workbook(wkfj_import_path)
# # num_list = []
# # for b in range(3):
# #     j = b + 1
# #     tables = data.sheets()[0]
# #     allrows = tables.nrows
# #     vals = tables.row_values(j)
# #     imp_data = '\t'.join(map(str, vals))
# #     num_list.append(imp_data)
# # pyperclip.copy("\n".join(map(str, num_list)))
# # print("\n".join(map(str, num_list)))
# # now_time = datetime.datetime.now()
# # str_time = now_time.strftime('%Y%m%d')  # 获取当前时间
# #
# # print(str_time)
# # print(st lims_nub2 = read_excel_xlsx_list_col(all_path.""", 0, '实验室号')r_time)
#
# #
# # lims_nub2 = read_excel_xlsx_list_col(""", 0, 'lims号')
# # lisa=[]
# # for i in lims_nub2:
# #     lisa.append(i[0])
# #
# # lims_id_str = ",".join(map(str,lisa))
# # print(lims_id_str)
# all_laboratorys = ['样本入库', '核酸提取', '超声破碎', '文库构建', '文库富集', '文库定量', 'Library quantification', '上机', '21基因分析',
#                    'MGMT']
# #
# # for i in range(len(all_laboratorys) - 1, -1, -1):
# #     print(all_laboratorys[i])
# # enrichment_nub = read_excel_xlsx_list_col(""", 0, 'lims号')
# # print(enrichment_nub)
# #
# # non_sr_lims = get_non_sr_sample_from_excel('lims号')
# # lims_id_str = "\n".join(non_sr_lims)  # 取出Excel表中样本，拼接成字符串录入到检索文本中
# #
# # sr_lims = self.get_sr_sample_from_excel()
# # sr_lims_id_str = "\n".join(sr_lims)  # 把所有值（富集lims号）转换为带换行的字符串
# # now_time = datetime.datetime.now()
# # str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
# # print(str_time)
# # f = open(wkdl_sequencing_group_number, 'r+', encoding='utf-8')
# #
# # list1=['sfsfsdf','fsfsf']
# #
# # list2=[12,3,4,5,6]
# #
# # yaml.dump_all([list1],f)
# #
# # f.close()
#
# # s=None
# # with open(wkdl_sequencing_group_number, 'r+', encoding='utf-8') as f:
# #     cfg = f.read()
# #     ds = yaml.load_all(cfg,Loader=yaml.FullLoader)
# #     # ds是所有读取数据的迭代器
# # for i in ds:
# #    s=i
# # print(len(ds))
# # data = xlrd.open_workbook(wkdl_result_standard_sample_path)
# # tables = data.sheets()[0]
# # allrows = tables.nrows
# # print(allrows)
# # num_list = []
# # for nss in range(0, allrows-1):
# #     h = nss + 1
# #     # tables = data.sheets()[0]
# #     # allrows = tables.nrows
# #     vals = tables.row_values(h)
# #     imp_data = '\t'.join(map(str, vals))
# #     print("第{}行".format(h),imp_data)
# #     num_list.append(imp_data)
# # print("\n".join(map(str, num_list)))
# # # pyperclip.copy("\n".join(map(str, num_list)))
# #
# # lims_id = read_excel_xlsx_list_col(wkdl_file_path, 0, '实验室号')
# # # print(lims_id)
# # ss='Task list status：完成'
# # # print(ss[17:].strip())
# # specimen_list = {'FFPE白片': 8, 'EDTA抗凝血': 8, '骨冷冻组织': 16, 'DNA文库': 8}
# # # total = specimen_list.values()
# # # n=0
# # # for d in total:
# # #     n+=d
# # # print(n)
# # nums = 0
# # for s_type in specimen_list.keys():
# #
# #     print(s_type)
# # with open (report_views_refresh_sql,'r',encoding='utf-8',errors='ignore') as f:
# #     sa=f.read()
# #     print(sa)
# # sql_first_step = Get_Sql_Helper()
# # sql_first_step.test_update(sa)
# # lims_nub = read_excel_xlsx_list_col(esyjy_file_path, 0, 'lims号')
# # print(lims_nub[2][0])
# # laboratory_list=[]
# # for i in lims_nub:
# #     laboratory_list.append(i[0])
# # print(laboratory_list)
# #
# # sss = 'PB21B30002-J022'
# # print(sss[:2])
# listss = ['病理检验', '样本处理', '核酸提取', '超声破碎', '文库构建', '文库富集', '文库定量', '上机', '21基因分析', 'MGMT', '样本入库',
#           '写入报告样本']
#
# valuedd = [["lims号", "实验室号", "当前节点", "任务单号"]]  # 其他
#
# #
# # order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
#
# # print(order_nub)
#
# #
# # testdata = read_yaml.read_yaml(testdata_path)
# #
# # name = testdata["medicalnuminfo"][0]['name']
# # order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
#
#
# # name = testdata["medicalnuminfo"][0]['name']
# # order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
#
# # wb = openpyxl.Workbook()
# # ws = wb.active
# # ws.title = 'test_sheet1'
# # ws.cell(row=1, column=2).value = 1
# # file_name = "报告上传文件" + str(name) + "_" + str(order_nub[0][0])
# # # wb.save(excel_doc_file_path+'/'+'{}.xlsx'.format(file_name))
# #
# # file_path = os.path.abspath(excel_doc_file_path + '/' + '{}.xlsx'.format(file_name))
# #
# # print(file_path)
#
# # with open(excel_doc_file_path + '/' + '自动化测试解读文件上传.doc','w', encoding='utf-8') as a:
# #     a.write('自动化测试解读文件上传')
#
#
# # wb = openpyxl.Workbook()
# # ws = wb.active
# # ws.title = 'test_sheet1'
# # ws.cell(row=1, column=2).value = 1
# # file_name = "报告上传文件" + str(name) + "_" + str(order_nub[0][0])  # 新建Excel文件，以读取的患者姓名和订单号为文件名
# # wb.save(excel_doc_file_path + '/' + '{}.csv'.format('报告上传文件'))  # 保存文件
# # file_path = os.path.abspath(excel_doc_file_path + '/' + '{}.csv'.format('报告上传文件'))
# # items = {}
# # items["bioinformatic_negative_lab_num"] = 123456789
# # with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式获取的URL地址到yaml文件中
# #     yaml.safe_dump(items, fs, allow_unicode=True)
# # print("写入后的URL地址", items)
#
#
# # # sampledata_path
# # testdata = read_yaml.read_yaml(testdata_path)
# # a = [i for i in testdata.values()]
# # print(a[0])
# # testdata1 = read_yaml.read_yaml(mutation_file_path)
# # print(testdata1)
# # import pandas as pd
# #
# # df = pd.read_csv(mutation_file_path, encoding='utf-8', )
# # print(df.columns)
# # df.loc[:,'id']=a[0]
# # df.to_csv(mutation_file_path, index=False, encoding='utf-8')
# # datas = read_yaml.read_yaml(testdata_path)
# # testdata = datas["medicalnuminfo"][0]
# # testdata1 = datas["medicalnuminfo"]
# # print(testdata["identificationNo"])
# # print(testdata1)
# #
# # order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
# # print(order_nub)
# from common.sql import Get_Sql_Helper
#
# # lims_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
# # print(lims_nub[0][0])
# # lims_nub = read_excel_xlsx_list_col(all_path.pathologycheck_file_path, 0, 'lims号')
# # lism_id = []
# # for i in lims_nub:
# #     lism_id.append(i[0])
# # lims_id_str = "\n".join(lism_id)
# #
# # print(lism_id)
# # c='任务单状态：完成'
# # print(c[6:].strip())
#
# all_sql = Get_Sql_Helper()
# # sqls = "UPDATE exp_extraction_item_t set actual_sample_amt={},actual_sample_pkg_amt=1 where task_id='{}';".format(20,taskstatus[5:].strip())
# #
# # sss.test_update(sqls)
# # sqla="SELECT * from exp_libconstruction_cl_result_t WHERE result_id in (327289,327288,327287,327286)"
# # sqla="SELECT result_id from exp_libconstruction_result_t  WHERE task_id='WKGJ2022011200002';"
# # sde=sss.test_select_limsdb(sqla)
# # res=tuple([item[key] for item in sde for key in item])
# # print(res)
#
# # sql1 = wkgj_result_sql1.format(taskstatus[5:].strip())
# # all_sql.test_update(sql1)
# #
# # sql2 = wkgj_result_sql2.format(taskstatus[5:].strip())
# #
# # result_id = all_sql.test_select_limsdb(sql2)
# #
# # res = tuple([item[key] for item in result_id for key in item])
# #
# # sql3 = wkgj_result_sql3.format(res)
# # all_sql.test_update(sql3)
#
# # hstq_detail_sql2="SELECT sample_id_lims from exp_extraction_item_t where task_id='{}';"
# #
# # taskstatus='任务单号：HSTQ2022011400001'
# # result_id1 = all_sql.test_select_limsdb(hstq_detail_sql2.format(taskstatus[5:].strip()))
# # res=[item[key] for item in result_id1 for key in item]
# # print(res)
# #
# # import pandas as pd
# #
# # nub_list=[i for i in range(1,len(res)+1)]
# # ress=[list(i) for i in zip(res,nub_list)]
# # print(ress)
# # def deal(company_name_list,path):
# #     # 列表
# #     # company_name_list = ['腾讯', '阿里巴巴', '字节跳动', '腾讯']
# #
# #     # list转dataframe
# #     df = pd.DataFrame(company_name_list)
# #
# #     # 保存到本地excel
# #     df.to_excel(path, header=None,index=False)
#
#
# # data = xlrd.open_workbook(position_in_box_path)
# # num_list = []
# # for b in range(0, 7):
# #     tables = data.sheets()[0]
# #     allrows = tables.nrows
# #     vals = tables.row_values(b)
# #     imp_data = '\t'.join(map(str, vals))
# #     num_list.append(imp_data)
# # print("\n".join(map(str, num_list)))
# taskstatus = '任务单号：WKDL2022011100004'
# # print(taskstatus[5:].strip())
# lims_idu = all_sql.test_select_limsdb(wkdl_detail_sql1.format(taskstatus[5:].strip()))
# # ss=[item[i] for item in lims_id for i in item]
# # print(ss)
# #
# # for item in lims_id :
# #     for i in item:
# #         print(i)
# #
# # dict={'cs':'csshisssss'}
# # for i in dict:
# #     print(dict[i])
#
# # cdea=[[1],[2],[3]]
# # lisc=[c for i in cdea for c in i]
# #
# # print(lisc)
# #
# # enrichment_nub = read_excel_xlsx_list_col(wkdl_sr_file_path, 0, 'lims号')
# #
# # print(enrichment_nub)
# # def fdsdfsf():
# #     sql=wkdl_detail_sql2.format(taskstatus[5:].strip())
# #     all_sql.test_update(sql)
# # # fdsdfsf()
# # with open(wkdl_sequencing_group_number, 'r+', encoding='utf-8') as f:
# #     cfg = f.read()
# #     non_srgroup_nums = yaml.load_all(cfg, Loader=yaml.FullLoader)
# # print(non_srgroup_nums)
# # non_srgroup_num_list=[key for i in non_srgroup_nums for key in i]
# # print(non_srgroup_num_list)
#
# from datetime import datetime
#
#
# # str_time=time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
# # print(str_time)
# # lims_nub = read_excel_xlsx_list_col(sj_file_path, 0, '富集lims号')
# # for lism in [b for i in lims_nub for b in i]:
# #     print(lism)
# # now_time = datetime.now()
# # str_time = now_time.strftime('%Y.%m.%d')  # 获取当前时间
# # print(str_time)
# # testdata = read_yaml.read_yaml(testdata_path)
# # print(str(testdata["medicalnuminfo"][0]['identificationNo']).strip())
#
# # ssss='任务单状态：新建'
# # print(ssss[6:].strip())
# # ab = []
# # cd = []
# # sql = "SELECT previous_sample_id_lims,current_step FROM sample_info_t WHERE ( previous_sample_id_lims IN ( SELECT t.sample_id_lims FROM exp_extraction_result_t t WHERE task_id = 'HSTQ2022012200001' ) AND is_valid = '1' )"
# #
# # dada = all_sql.test_select_limsdb(sql)
# # sb = 'sndjf4522'
# # result = [list(dct.values())+[sb] for dct in dada]
# #
# # for i in result:
# #     if i[1]=='mgmt':
# #         i[1]='MGGTFF'
# # print(result)
#
#
# #
# # ab=[]
# # for item in dada:
# #     nub=item['previous_sample_id_lims']
# #     current_step=item['current_step']
# #     ab.append([nub,current_step])
# # print(ab)
#
#
# def add_excel_xlxs(self, sql, table_name, task_id):
#     """
#     根据核酸提取、超声破碎、文库构建流程结果表任务单号，在数据库中查询出样本对应下一步流程，以二维列表形式存入相对应的Excel中。最终存入lims号，下一步流向，和任务单号
#     :param sql: 数据库sql
#     :param table_name: 实验流程节点对应的结果表表名
#     :param task_id: 实验流程对应的结果表任务号页面元素定位
#     """
#     # 获取任务单号
#     taskidstr = self.get_text('css', task_id)
#     taskid = taskidstr[5:].strip()
#
#     # 执行SQL，获取二维列表，lims号和下一步流向
#     dada = all_sql.test_select_limsdb(sql.format(table_name, taskid))
#
#     # 把任务单号添加进二维列表
#     result = [list(dct.values()) + [taskid] for dct in dada]  # ID，next，task_id
#
#     # 根据不同下一步，循环写入Excel
#     for item in range(len(result)):
#
#         # 取出二维列表子元素的第二个值（下一步），进行判断
#         next_step = result[item][1]
#
#         if next_step == 'extraction':  # 核酸提取
#             result[item][1] = '核酸提取'
#             add_write_excel_xlsx(hstq_file_path, result[item])
#
#         elif next_step == 'ultrafrac':  # 超声破碎
#             result[item][1] = '超声破碎'
#             add_write_excel_xlsx(csps_file_path, result[item])
#
#         elif next_step == 'libconstruction':  # 文库构建
#             result[item][1] = '文库构建'
#             add_write_excel_xlsx(wkgj_file_path, result[item])
#
#         elif next_step == 'pooling':  # 文库富集
#             result[item][1] = '文库富集'
#             add_write_excel_xlsx(wkfj_file_path, result[item])
#
#         elif next_step == '文库定量':  # 文库定量
#             add_write_excel_xlsx(wkdl_non_sr_file_path, result[item])
#
#         elif next_step == '上机':  # 上机
#             add_write_excel_xlsx(sj_file_path, result[item])
#
#         elif next_step == 'twentyonegene':  # 21基因
#             result[item][1] = '21基因'
#             add_write_excel_xlsx(esyjy_file_path, result[item])
#
#         elif next_step == 'mgmt':  # MGMT
#             result[item][1] = 'MGMT'
#             add_write_excel_xlsx(mgmt_file_path, result[item])
#         else:
#             pass
#
#
# #
# # ybcl_detail_sql2="SELECT t1.sample_id_lims,t1.sample_main_lab_code from sample_id_lab_v t1 WHERE t1.sample_id_lims in (SELECT t2.sample_id_lims from exp_preparation_result_t t2 where t2.task_id ='{}');"
# # dada2 = all_sql.dada = all_sql.test_select_limsdb(ybcl_detail_sql2.format('YBCL2022012600007'))
# #
# # results=[list(i.values())for i in dada2]
# # print(results)
#
# # coding: utf-8
#
# # author: liuqin
#
# # import xlrd
# #
# #
# # def get_data(excelname):
# #
# #     wb = xlrd.open_workbook(excelname)
# #     data = wb.sheet_by_index(0)
# #
# #     '''获取第一行数据，即表头'''
# #     keys = data.row_values(0,0,1)
# #
# #     '''获取总行数'''
# #     rowsNum = data.nrows
# #
# #     '''获取总列数'''
# #     colsNum = data.ncols
# #
# #     if rowsNum > 1:
# #         pass
# #     else:
# #         print("没有数据")
# #         r = []
# #         j = 1
#
#
# # print(rowsNum)
# # print(keys)
# # print(colsNum)
# import pandas as pd
#
#
# def get_identificationNo():
#     """
#     身份证Excel中读取身份证信息
#     :return: 返回身份证号
#     """
#
#     df = pd.read_excel(identificationNo_file_path)
#     '''获取总行数'''
#     rowsNum = df.shape[0]
#
#     if rowsNum > 1:
#         '''获取第一行身份证号码'''
#         identificationNo = df.iloc[0].values
#         # print(identificationNo)
#
#         reslt = all_sql.test_select_limsdb(bl_sql.format(identificationNo[0]))
#         used_identificationNo = [i[item] for i in reslt for item in i]
#
#         if used_identificationNo[0] == 0:
#             '''取出后删除该行'''
#             df.drop(index=[0], axis=0, inplace=True)
#             # print(df.shape[0])
#             df.to_excel(identificationNo_file_path, index=None)
#             return identificationNo
#         else:
#             df.drop(index=[0], axis=0, inplace=True)
#             # print(df.shape[0])
#             df.to_excel(identificationNo_file_path, index=None)
#
#             return get_identificationNo()
#
#
# # used_identificationNo = all_sql.test_select_limsdb(bl_sql.format('320684199109177674'))
# # used_identificationNo=[i[item] for i in used_identificationNo for item in i]
# # print(used_identificationNo[0])
#
# # datas=all_sql.test_select_limsdb(project_id)
# # result=[list(i.values()) for i in datas]
# # print(result)
# # add_write_excel_xlsx(report_basic_info_process_path,result)
# # projectIdList = self.get_sql_data(project_id)
# # projectid = [i[item] for i in datas for item in i]
# # print(projectid)
# lims_nub = read_excel_xlsx_list_col(sampleprocessing_file_path, 0, 'lims号')
# projectIdafter = all_sql.test_select_limsdb(sampleProId.format(lims_nub[2][0]))
# projectids = [list(dct.values()) for dct in projectIdafter]
# print(projectids)
#
# import os
# # from selenium import webdriver
# #
# # options = webdriver.ChromeOptions()
# # # 0禁止弹出下载窗口
# # # download.default_directory设置下载路径
# # prefs = {
# #     "profile.default_content_settings.popups": 0,
# #     "download.default_directory": download_path}
# # options.add_experimental_option("prefs",prefs)
# # options.add_argument('headless')
# # driver = webdriver.Chrome(chrome_options=options)
# # driver.get("https://shouji.360.cn/v6/index.html")
# #
# # driver.find_element_by_partial_link_text("极速版").click()
#
# import os
#
# # dpdp=r'C:\Users\admin\Downloads\样本项目信息修改 (87).xlsx'
# # url=excel_doc_file_path
# # lists=os.listdir(url)
# # print(lists)
# # lists.sort(key=lambda fn: os.path.getmtime(url+'\\'+fn))
# # filepath=os.path.join(url,lists[-1])
# # print(filepath)
# # data= pd.read_excel(dpdp, engine='xlrd')
# # data.iloc[1,8]='cc'
# # data.to_excel(dpdp, header=True, index=False)
#
#
# # lims_nub = read_excel_xlsx_list_col(sampleprocessing_file_path, 0, '实验室号')
# # print(lims_nub[1][0])
# # # print(lims_nub)
# # # def abc(x):
# # #     return lambda  y:x+y
# # # sx=abc(5)
# # # print(sx(2))
# # sssppll="SELECT project_id,is_valid from exp_result_sample_project_t  WHERE sample_id_lims ='GS2201300049';"
# execute_sql = Get_Sql_Helper()
#
#
# # sql_data = execute_sql.test_select_limsdb(sssppll)
# # # projectid=[i[b] for i in sql_data for b in i ]
# # projectid=[list(dct.values())  for dct in sql_data]
# # # print(projectid)
# # sdws=[b for i in projectid for b in i]
# # print(sdws)
#
#
# # testdata = read_yaml.read_yaml(sampledata_path)
# # a = [i for i in testdata.values()]  # 读取基本信息处理模块存储的实验室号
# # print(a[1])
# # cddc='任务单号：YBCL2022021400005'
# # task_id = cddc[5:].strip()
# # print(task_id)
# #
# # testdata = read_yaml.read_yaml(sampledata_path)
# # sql_data = execute_sql.test_select_limsdb(ybcl_detail_sql2.format(testdata['samplepaocessing_taskid']))
# # result = [(i['sample_main_lab_code']) for i in sql_data]
# # print(result)
# #
# # laboratory_nub = read_excel_xlsx_list_col(report_basic_info_process_path, 0, '实验室号')  #
# # # 获取样本处理结果表的样本信息，此处为样本处理节点写入
# # laboratory_list = [item.strip() for i in laboratory_nub for item in i]
# # print(laboratory_list)
# def get_sql_data(sqls):
#     """
#     调用sql方法,执行数据库操作，获取返回值
#     :return:数据库返回值
#     """
#     execute_sql = Get_Sql_Helper()
#     sql_data = execute_sql.test_select_limsdb(sqls)
#     return sql_data
#
#
# def check_order_isExists(order):
#     sql = "select count(*) from order_info_t where order_code='{}'; "
#     result = get_sql_data(sampleMsgNotice)
#     result1 = [dct[item] for dct in result for item in dct]
#     if result1[0] == 0:
#         return order
#     elif result1[0] != 0:
#         order = str(int(order) + 1)
#         return check_order_isExists(order)
#
#
# # # nub=check_order_isExists('99991214')
# # result = get_sql_data(sampleMsgNotice)
# # lims_nub=[i['previous_sample_id_lims'] for i in result ]
# # print(lims_nub)
# #
# # dicss={'ddd':'dd','sssa':'dsd2'}
# # print(dicss['ddd'])
#
# def funA(fn):
#     # 定义一个嵌套函数
#
#     def say(arc):
#         print("Python教程:", arc)
#
#     return say
#
#
# @funA
# def funB(arc):
#     print("funB():", arc)
#
#
# funB("http://c.biancheng.net/python")
#
#
# def 炼丹炉(func):
#     def 变身(*args, **kwargs):
#         print('有火眼金睛了')
#         return func(*args, **kwargs)
#
#     return 变身
#
#
# def 龙宫走一趟(func):
#     def 你好(*args, **kwargs):
#         print('有金箍棒了')
#         return func(*args, **kwargs)
#
#     return 你好
#
#
# def 拜师学艺(func):
#     def 师傅(*args, **kwargs):
#         print('学会飞、72变了')
#         return func(*args, **kwargs)
#
#     return 师傅
#
#
# @拜师学艺
# @龙宫走一趟
# @炼丹炉
# def 孙悟空():
#     print('吃桃子')
#
#
# # 孙悟空()
#
#
# def test02(fun):
#     def test03(s):
#
#         if type(s) is not str:
#             print("fff")
#         else:
#             return fun(s)
#
#     return test03
#
#
# @test02
# def test01(s):
#     print(s)
#
#
# # test01('ddd')
# import functools
# import time
#
#
# def timer(func):
#     """Print the runtime of the decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()  # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()  # 2
#         run_time = end_time - start_time  # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         # return func(*args, **kwargs)
#
#     return wrapper_timer
#
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i ** 2 for i in range(10)])
#
#
# # waste_some_time(1)
#
# def timers(func):
#     def wrapper(timess):
#         if timess >50000:
#             start_time = time.time()
#             sxd=func(timess)
#             end_time = time.time()
#             all_time = end_time - start_time
#             print('共计用时，', all_time)
#         else:
#             print('整不了')
#         return func(timess)
#
#     return wrapper
#
#
# @timers
# def go_time(timess):
#     for i in range(1):
#         sum([i for i in range(timess)])
#
#
# # go_time(10)
# # print( sum([i for i in range(1000)]))
#
# from docx import Document
# from docx.enum.text import WD_BREAK
# import os
# from docx.oxml.ns import qn
#
#
# # ef getContent():
# #     """
# #     获取图片方法（以png存储）
# #     """
# #     return get_screenshot_as_png()
#
#
# #
# # def append2doc(file_path):
# #     if not os.path.exists(file_path):
# #         document=Document()            #声明word
# #
# #         content = getContent() # 读取文件内容
# #         document.add_paragraph(content) # 写入word
# #         document.save(file_path)         # 保存word
# #     else:
# #         document = Document(file_path)
# #
# #         paragraphs = document.paragraphs
# #         paragraphs[-1].runs[-1].add_break(WD_BREAK.LINE)  #在最后位置 追加内容
# #         content = getContent()
# #         paragraphs[-1].add_run(content)
# #         document.save(file_path)
#
#
#
#
# order_nub = read_excel_xlsx_list_col(order_file_path, 0, 'order_number')
#
# #
# # sql_data = execute_sql.test_select_limsdb("select sample_id_lims from sample_receive_item_t where order_code='{}' and sample_type='C2016120700002' limit 1;".format(order_nub[0][0]))
# # ss=[list(i.values())for i in sql_data]
# print(order_nub)
#
#
# def eeeesd():
#     now_time = datetime.now()
#     str_time = now_time.strftime('%Y%m%d')  # 获取当前时间
#     sr_sample_id_external = str_time + '_TEST_SR'  # 按时间规则生成外部样本编号
#     wb = load_workbook(filename=sr_sample_imp_file)  # 打开excel文件
#     ws = wb.active
#     ws.cell(2, 2, sr_sample_id_external)  # 修改第k行，第index列值
#     wb.save(sr_sample_imp_file)
#     wb = load_workbook(filename=sr_sample_sublibrary_imp_file)  # 打开excel文件
#     ws = wb.active
#     ws.cell(2, 1, sr_sample_id_external)  # 修改第k行，第index列值
#     wb.save(sr_sample_sublibrary_imp_file)
#     # 数据库先获取一条sr样本的lims号，再根据lims号在数据库设置外部样本编号
#     sr_sample_nubs = execute_sql.test_select_limsdb(get_sr_sample_lims.format(order_nub[0][0]))
#     sr_sample_nub = [list(i.values()) for i in sr_sample_nubs]
#     print(sr_sample_nub[0][0])
#     execute_sql.test_update(set_sr_sample_id_external.format(sr_sample_id_external, sr_sample_nub[0][0]))
#     # 将获取的一条sr样本的lims号，存到临时文件，在SR样本信息登记模块使用
#     datas = read_yaml.read_yaml(sampledata_path)
#     datas["rec_sr_sample_for_sr_import"] = sr_sample_nub[0][0]
#     with open(sampledata_path, 'w', encoding='utf-8') as fs:  # 写入模式
#         yaml.safe_dump(datas, fs, allow_unicode=True)
#
#
# # eeeesd()
#
#
# sr_sample_nubs = execute_sql.test_select_limsdb(get_sr_sample_lims.format(order_nub[0][0]))
# sr_sample_nub = [list(i.values()) for i in sr_sample_nubs]
# # print(sr_sample_nub[0][0])
# # datas = read_yaml.read_yaml(testdata_path)
# # testdata = datas["medicalnuminfo"][0]
# # print(testdata)
#
# # lims_id = []
# # lims_nub = read_excel_xlsx_list_col(csps_file_path, 0, 'lims号')
# # for i in lims_nub:
# #     lims_id.append(i[0])
# # lims_id_str = "\n".join(lims_id[:2])  # 取出Excel表中样本，拼接成字符串录入到检索文本中
# # print(lims_id_str)
# #
# # for i in range(5):
# #     sbb=input('sssss')
# #     if sbb != 'aa':
# #         print('haha')
# #     else:
# #         print('right')
#
#
# lims_nub = read_excel_xlsx_list_col(sj_file_path, 0, '富集lims号')
# print(lims_nub)
# if lims_nub:
#     for lims in [b for i in lims_nub for b in i]:
#         print(lims)
#
#
# def get_sql_data(sqls):
#     """
#     调用sql方法,执行数据库操作，获取返回值
#     :return:数据库返回值
#     """
#     execute_sql = Get_Sql_Helper()
#     sql_data = execute_sql.test_select_limsdb(sqls)
#     return sql_data
#
#
# def sql_actions():
#     df = pd.read_excel(identificationNo_file_path)
#     rowsNum = df.shape[0]
#
#     if rowsNum > 1:
#
#         '''获取第一行身份证号码'''
#         identificationNos = df.iloc[0].values
#         print("读取的身份证号", identificationNos)
#
#         '''从Excel中取第一行的身份证，去数据库查询是否已存在'''
#         reslt = get_sql_data(bl_sql.format(identificationNos[0]))
#         print('sss',reslt)
#         return reslt
#
# sssasdd=sql_actions()
# print(sssasdd)
#
#
from common import all_path
from common.editYaml import read_yaml
from common.xlsx_excel import read_excel_col

lims_id = read_excel_col(all_path.sampleprocessing_file_path,  'lims号')
# print(lims_id[0][0])
lims_nub = read_excel_col(all_path.sampleprocessing_file_path, 'lims号')

lism_id = []
for i in lims_nub:
    lism_id.append(i[0])
lims_id_str = "\n".join(lism_id)
print(lims_id_str)