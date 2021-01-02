# -*- coding: utf-8 -*-
# @Project : InterfaceProject
'''

关于Excel表的操作
'''
import xlrd
from settings import conf

class ExcelHandler(object):

    @property
    def get_excel_data(self):
        # 获取到book对象
        print(conf.TEST_CASE_PATH)
        book = xlrd.open_workbook(conf.TEST_CASE_PATH)
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        # sheet = book.sheet_by_name('接口自动化用例')
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            l.append(dict(zip(title, sheet.row_values(i))))
        print(l)
        return l

    def get_request_data(self):
        '''
        EXCEL表中判断是否执行
        :return: 执行的数据集，以列表的形式
        '''
        request_data = []
        excel_data = self.get_excel_data
        for i in range(len(excel_data)):
            is_run = excel_data[i].get('case_run')
            if is_run == 'yes':
                print(excel_data[i])
                request_data.append(excel_data[i])
        print(request_data)
        return request_data



if __name__ == '__main__':
    e = ExcelHandler()
    e.get_request_data()