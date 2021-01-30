# -*- coding: utf-8 -*-
# @Project : InterfaceProject
import pytest
import allure
from uti.RequestHandler import RequestHandler
from uti.AllureHandler import AllureHandler
from uti.ExcelHandler import ExcelHandler
from uti.MysqlHandler import MysqlHandler
from uti.NotRunBeDpendCase import NotRunBeDependCase
from uti.SaveRunBeDependValue import SaveRunBeDependValue
from uti.GetParam import GetParam
'''
1. 获取测试数据
2. 发请求
3. 生成测试用例报告
4. 断言
'''

class Test_case(object):

    def setup_class(self):
        excelhandler = ExcelHandler()
        table = excelhandler.get_sheet_name()
        mysql = MysqlHandler()
        mysql.create_table(table)
        # print('11')
        run = NotRunBeDependCase()
        run.not_run_be_depend_case()

    @pytest.mark.parametrize('case', ExcelHandler().get_request_data)
    def test_case(self,case):
        """  执行断言 """
        if case['case_depend_key'] != '':
            param = GetParam().getparam(case['case_depend_key'],case['case_params'])
            case['case_params'] = param
        # print(case['case_params'])
        savevalue = SaveRunBeDependValue()
        response,assert_value = RequestHandler(case).get_response
        # print(assert_value)
        if case['case_response_key'] != '':
            # print(case['case_response_key'])
            savevalue.savedependvalue(case['case_response_key'],response)
        # 制作 allure 报告
        assert assert_value[0] == assert_value[0]
        allure.dynamic.title(case['case_name'])
        allure.dynamic.description('<font color="red">请求URL：</font>{}<br />'
                                   '<font color="red">期望值：</font>{}'.format(case['case_url'], case['case_expect']))
        allure.dynamic.feature(case['case_name'])
        allure.dynamic.story(case['case_method'])

    def teardown_class(self):
        """llure命令 """
        AllureHandler().execute_command()
        # 发邮件
    #     EmailHandler().send_email()