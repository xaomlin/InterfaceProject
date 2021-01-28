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
        self.dependhandler = DependHandler()
        # self.getvalue = GetValue()

    def get_data(self):
        '''
        1、获取所有is_run为yes的所有用例集
        2、判断是否有数据依赖
        3、获取数据依赖值
        '''
        # 获取所有用例，包括不进行运行的用例
        excel_data = self.excelhandler.get_excel_data()
        # 获取插入表
        table = self.excelhandler.get_sheet_name()
        run_data = []
        # 循环列表
        for i in range(len(excel_data)):
            # 判断是否需要依赖数据
            is_depend = excel_data[i]['case_depend_key']
            is_run = excel_data[i]['case_run'].upper()
            if is_depend != '' and is_run != 'YES':
                mysql = MysqlHandler()
                # 获取依赖的key
                depend_key = excel_data[i]['case_depend_key']
                #获取数据库的依赖值
                repl = mysql.select_table('value',table,depend_key)
                pattern = '<'+depend_key+'>'
                #repl替换掉string中被pattern匹配的字符， count表示最大替换次数，flags表示正则表达式的常量
                request_case = str(excel_data[i])
                # print(pattern,repl,request_case)
                request_case = re.sub(pattern, repl, request_case, count=1, flags=re.IGNORECASE)
                excel_data[i] = eval(request_case)
                # print(request_data[i])
                # print(type(request_data[i]))
                # # 赋值依赖的case_id
                # case_id = int(is_depend[5:]) - 1
                # # 获取依赖的case的url
                # url = excel_data[case_id].get('case_url')
                # # print(url)
                # # 获取依赖的case的method
                # method = excel_data[case_id].get('case_method')
                # print(method)
                # # 获取依赖的case的param
                # params = excel_data[case_id].get('case_params')
                # if params == '':
                # # 执行依赖case
                #     depend_response = self.dependhandler.send_depend_request(url, method)
                # else:
                #     depend_response = self.dependhandler.send_depend_request(url, method, params)
                # # 获取依赖数据对应的值
                # depend_data = self.getvalue.get_json_value_by_key(depend_response, depend_key)
                # # print(depend_data)
                # dicts = {}
                # dicts['depend'] = depend_data[0]
                # request_data.append(dicts)
        #     run_data.append(request_data[i])
        #     # print(run_data)
        # return run_data
