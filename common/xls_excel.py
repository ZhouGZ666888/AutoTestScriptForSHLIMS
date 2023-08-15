# coding=UTF-8
import openpyxl
import xlrd
import xlwt
from xlrd import sheet
from xlutils.copy import copy
from common.all_path import *
import pandas as pd

def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            # 追加写入数据，注意是从i+rows_old行开始写入
            new_worksheet.write(i + rows_old, j, value[i][j])
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path):
    """
    指定读取第一个sheet的每行数据
    :param path:
    :return:
    """
    row_list, col_list,ret = [], [],[]
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    # print(worksheet)
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            # row_list.append(worksheet.cell_value[i])
            # col_list.append(worksheet.cell_value[j])
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据


def read_excel_xls_todict(path, row):
    """
    遍历excel所有sheet，并以字典返回
    :param row:指定行
    :return:
    """
    with xlrd.open_workbook(path, 'rb') as book:
        sheets = book.sheet_names()  # 找到所有sheets
    data_dict = {}
    for sheet in sheets:
        table = book.sheet_by_name(sheet)  # 找到要操作的sheet

        # 获取sheet所有列数
        col_num = table.ncols
        # print(table.nrows)
        #  读取第一行的值，作为每个sheet返回字典的key
        keys = table.row_values(0)

        # 读取除指定行，作为每个sheet返回字典的value
        values = table.row_values(row)

        # 遍历所有列，并以字典接收,其中第一行作为字典的key，其他行作为字典的value
        sheet_dict = {}
        ret=[]
        for col in range(col_num):
            # ret.append(values[col])#将指定列加入到列表
            # print(col_num,values[col])
            sheet_dict[keys[col]] = values[col]#将结果按照字典表返回

            # 遍历所有sheet，并以字典接收返回，其中sheet名称作为字典的key，每个sheet的数据作为字典的value
        data_dict[sheet] = sheet_dict

    return data_dict


def read_excel_xls_list(path,index):
    """
    获取指定sheet页数据，返回list
    :param path:文件路径
    :param index:sheet页序号
    :return:
    """
    ret=[]
    data = xlrd.open_workbook(path)  #获取文本对象
    table = data.sheets()[index]  #根据index获取某个sheet
    rows = table.nrows  #获取当前sheet页面的总行数,把每一行数据作为list放到 list
    for i in range(rows):
        col = table.row_values(i)  ##获取每一列数据
        # print(col)
        ret.append(col)
    # print(ret)
    return ret


def read_excel_xls_list_col(path,index,colname):
    """
    获取指定sheet页&指定列的数据，返回list
    :param path:文件路径
    :param index:sheet页名称
    :param colname:指定列名
    :return:
    """
    row_list,col_list,ret=[],[],[]
    data = xlrd.open_workbook(path)  #获取文本对象
    table = data.sheets()[index]  #根据index获取某个sheet
    rows = table.nrows  #获取当前sheet页面的总行数,把每一行数据作为list放到 list
    df=pd.read_excel(path)#使用pd读取excel
    col_name=list(df)#获取列名

    # print(colname,col_name)

    while colname in col_name:
        col = col_name.index(str(colname))
        print("表格中，" + str(colname) + "，处于第" + str(col_name.index(str(colname)) + 1) + "列")

        #获取指定列的每行信息（除去列名那行不算）
        for i in range(1,rows):
            # print(table.cell_value(i, col))
            ret.append([table.cell_value(i, col)])

        break
    # print(ret)
    return ret



if __name__ == '__main__':
    book_name_xls = '审计提供订单表格.xls'  # 表名
    sheet_name_xls = '穿行'  # sheet頁名

    # value_title = [["name", "sex", "age", "city", "work"], ]  # 列名
    # value_title = [["订单号"]]  # 列名

    # value1 = [["Tom1", "man", "19", "HZ", "E1"],
    #           ["Jones1", "man", "22", "BJ", "D1"],
    #           ["Cat1", "woman", "33", "NJ", "T1"], ]  # 每行的數據
    # value=[['00031702'], ['00038597'], ['00035911']]

    # write_excel_xls(book_name_xls, sheet_name_xls, value_title)
    # write_excel_xls_append(book_name_xls, value1)

    # write_excel_xls_append(book_name_xls, value)
    # read_excel_xls(book_name_xls)

    # path = 'ceshi.xls'
    # path = 'xls格式测试工作簿.xls'
    # path = file_path + '\\' + 'lims_sample_order2.xls'
    path=originorder_file_path
    # read_excel_xls(path)
    test1 = read_excel_xls_list_col(path, 0,'订单号')
    print(test1)
