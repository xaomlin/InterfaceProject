# -*- coding: utf-8 -*-
# @Project : InterfaceProject
'''

关于Excel表的操作
'''
import xlrd
from settings import conf

class ExcelHandler(object):
    def get_excel_data(self):
        # 获取到book对象
        # print(conf.TEST_CASE_PATH)
        book = xlrd.open_workbook(conf.TEST_CASE_PATH)
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            l.append(dict(zip(title, sheet.row_values(i))))
        return l

    def get_request_data(self):
        '''
        EXCEL表中判断是否执行
        :return: 执行的数据集，以列表的形式
        '''
        request_data = []
        excel_data = self.get_excel_data()
        for i in range(len(excel_data)):
            is_run = excel_data[i].get('case_run')
            if is_run == 'yes':
                request_data.append(excel_data[i])
        # print(request_data)
        return request_data

    # def dict_data(self, excelPath):
    #     data = xlrd.open_workbook(excelPath)
    #     table = data.sheet_by_index(0)
    #     # 获取第一行作为key值
    #     keys = table.row_values(0)
    #     # 获取总行数
    #     rowNum = table.nrows
    #     # 获取总列数
    #     colNum = table.ncols
    #     if rowNum <= 1:
    #         print("总行数小于1")
    #     else:
    #         r = []
    #         j = 1
    #         for i in list(range(rowNum - 1)):
    #             s = {}
    #             # 从第二行取对应values值
    #             s['rowNum'] = i + 2
    #             values = table.row_values(j)
    #             # print(values)
    #             for x in list(range(colNum)):
    #                 s[keys[x]] = values[x]
    #             r.append(s)
    #             j += 1
    #         return r
    #
    # def get_request_data(self):
    #     '''
    #     EXCEL表中判断是否执行
    #     :return: 执行的数据集，以列表的形式
    #     '''
    #     request_data = []
    #     excel_data = self.dict_data(r'D:\InterfaceProject\data\接口测试示例.xlsx')
    #     for i in range(len(excel_data)):
    #         is_run = excel_data[i].get('case_run')
    #         if is_run == 'yes':
    #             # print(excel_data[i])
    #             request_data.append(excel_data[i])
    #     print(request_data)
    #     return request_data


if __name__ == '__main__':
    e = ExcelHandler()
    e.get_request_data()