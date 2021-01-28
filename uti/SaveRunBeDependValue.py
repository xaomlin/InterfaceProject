# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 22:10
# @Project : InterfaceProject
from uti.MysqlHandler import MysqlHandler
from uti.GetValue import GetValue
from uti.ExcelHandler import ExcelHandler
class SaveRunBeDependValue(object):
    """保存执行而且有被依赖的value"""
    def savedependvalue(self,depend_data_key,response):
        excelhandler = ExcelHandler()
        table = excelhandler.get_sheet_name()
        getvalue = GetValue()
        depend_value = getvalue.get_json_value_by_key(response, depend_data_key)
        for value in depend_value:
            sql = MysqlHandler()
            # 把每一个依赖key，value保存到数据库
            # print(table, depend_data_key, value)
            sql.insert_data(table, depend_data_key, value)
