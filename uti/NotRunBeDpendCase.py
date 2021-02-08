# -*- coding: utf-8 -*-
# @Time    : 2021/1/26 22:28
# @Project : InterfaceProject
from uti.ExcelHandler import ExcelHandler
from uti.DependHander import DependHandler
from uti.GetValue import GetValue
from uti.MysqlHandler import MysqlHandler
class NotRunBeDependCase(object):
    '''
    1、执行被依赖但不执行的case
    2、获取依赖的值
    3、以key，value的形式保存到数据库
    '''
    def __init__(self):
        self.excelhandler = ExcelHandler()
        self.dependhandler = DependHandler()
        self.getvalue = GetValue()

    def not_run_be_depend_case(self):
        #获取所有的case
        excel_data = self.excelhandler.get_all_excel_data()
        #获取插入表
        table = self.excelhandler.table_name()
        mysql = MysqlHandler()
        mysql.create_table(table)
        # 循环遍历每一条case
        for case in excel_data:
            is_run =case['case_run'].upper()
            if case['case_response_key'] != '' and is_run != 'YES':
                url =case['case_url']
                method = case['case_method']
                type = case['params_type']
                data = case['case_params']
                #执行被依赖用例
                response = self.dependhandler.send_depend_request(url, method, type, data)
                depend_key = case['case_response_key']
                depend_value = self.getvalue.get_json_value_by_key(response,depend_key)
                for value in depend_value:
                    sql = MysqlHandler()
                    # 把每一个依赖key，value保存到数据库
                    sql.insert_data(table,depend_key,value)