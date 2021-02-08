# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 18:59
# @Project : InterfaceProject

from uti.ExcelHandler import ExcelHandler
from uti.DependHander import DependHandler
from uti.GetValue import GetValue
from uti.MysqlHandler import MysqlHandler
import re
import json
class GetData(object):
    def __init__(self):
        self.excelhandler = ExcelHandler()

    @property
    def get_request_data(self):
        '''
        EXCEL表中判断是否执行
        :return: 执行的数据集，以列表的形式
        '''
        request_data = []
        excel_data = self.excelhandler.get_all_excel_data()
        for i in range(len(excel_data)):
            is_run = excel_data[i].get('case_run').upper()
            if is_run == 'YES':
                request_data.append(excel_data[i])
        return request_data
