# -*- coding: utf-8 -*-
# @Project : InterfaceProject
'''
关于Excel表的操作
'''
import xlrd
from settings import conf
from openpyxl import load_workbook
from uti.LoggerHandler import logger
import os


class ExcelHandler(object):

    def __init__(self):
        self.dir = conf.CASE_PATH  # case文件夹
        self.case_path = os.listdir(self.dir)  # 获取case文件夹下所有文件名，list输出
        self.file_name_list = conf.file_name.split(',')  # 输入的文件名，逗号分隔，list输出

    @classmethod
    def get_excel_data(cls, file) -> list:
        # 获取到book对象
        book = xlrd.open_workbook(file)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        rows, cols = sheet.nrows, sheet.ncols
        l = []
        title = sheet.row_values(0)
        # 获取其他行
        for i in range(1, rows):
            l.append(dict(zip(title, sheet.row_values(i))))
        return l

    @property
    def get_all_excel_data(self) ->list:
        '''获取所有excel数据'''
        allexceldata = []
        # 遍历所有输入文件名
        for file_name in self.file_name_list:
            file = file_name + '.xlsx'
            if file in self.case_path:
                file_path = os.path.join(self.dir, file)
                exceldata = self.get_excel_data(file_path)
                allexceldata.extend(exceldata)
            else:
                logger().error('没有找到{}，请检查case文件夹及输入文件名,'.format(file))
        return allexceldata

    def table_name(self):
        return self.file_name_list[0]


if __name__ == '__main__':
    e = ExcelHandler()
    print(e.get_all_excel_data)
    print(e.table_name())
    # print(e.get_request_data())
    # e.get_sheet_name()
