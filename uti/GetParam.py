# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 22:36
# @Project : InterfaceProject
from uti.MysqlHandler import MysqlHandler
from uti.ExcelHandler import ExcelHandler

import re


class GetParam(object):

    '''
    获取运行前的参数
    '''

    def getparam(self, case_depend_key, param) ->str:
        excelhandler = ExcelHandler()
        table = excelhandler.table_name()
        mysql = MysqlHandler()
        # 获取数据库的依赖值
        repl = mysql.select_table('value', table, case_depend_key)
        pattern = '<' + case_depend_key + '>'
        # repl替换掉string中被pattern匹配的字符， count表示最大替换次数，flags表示正则表达式的常量
        param = str(param)
        # print(pattern,repl,param)
        value = re.sub(pattern, repl, param, count=1, flags=re.IGNORECASE)
        # 将json字符串解析成为JSON对象
        param = eval(value)
        return param
