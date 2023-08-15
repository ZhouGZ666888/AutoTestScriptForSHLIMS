from common.xls_excel import *


class ExcelMothed:
    def __init__(self, filepath, sheets):
        self.filepath = filepath
        self.sheet = sheets  # sheet=sheet页名称

    def open_excel(self):
        """打开excel"""
        workbook = openpyxl.load_workbook(self.filepath)
        return workbook

    def get_sheet(self):
        """获取Sheet表单"""
        workbook = self.open_excel()
        sheets = workbook[self.sheet]
        return sheets

    def get_case(self):
        """获取所有用例,按sheet页名称读取"""
        cell = self.get_sheet()
        rows = list(cell.rows)  # 获取行
        case = []
        title = []
        for row in rows[0]:
            title.append(row.value)  # 获取标题行
        for values in rows[1:]:  # 获取
            dic = {}
            for indx, value in enumerate(values):
                dic[title[indx]] = value.value
            case.append(dic)
        return case

    def excel_write(self, row, column, data):
        """excel根据单元格位置写入内容"""
        sheets = self.get_sheet()
        sheets.cell(row, column).value = data
        self.excel_save()
        self.excel_close()

    def excel_save(self):
        """保存excel"""
        self.open_excel().save(self.filepath)

    def excel_close(self):
        """关闭excel"""
        self.open_excel().close()


if __name__ == '__main__':
    pass
    # xls_path = file_path + '\\测试用例表.xlsx'
    # a = ExcelMothed(xls_path, 'Sheet1')
    # b = a.get_case()
    # print(b)
