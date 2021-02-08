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
from uti.ReadYaml import ReadYaml
from uti.GetData import GetData
'''
1. 获取测试数据
2. 发请求
3. 生成测试用例报告
4. 断言
'''

class Test_case(object):

    def setup_class(self):
        '''执行用例前执行一次'''
        excelhandler = ExcelHandler()
        table = excelhandler.table_name()
        mysql = MysqlHandler()
        mysql.create_table(table) #创建依赖数据表
        run = NotRunBeDependCase()
        run.not_run_be_depend_case() # 执行有被依赖但是不执行的用例

    @pytest.mark.parametrize('case',GetData().get_request_data)
    def test_case(self,case):
        case_model = case['case_model']
        case_params = case['case_params']
        if case_params != '':
            params = ReadYaml().get_yaml_param(case_model,case_params)# 读取yaml文件，获取请求参数
            if case['case_depend_key'] != '':#判断参数是否有依赖数据
                param = GetParam().getparam(case['case_depend_key'],params) #读取数据依赖数据库，更换请求数据
                case['case_params'] = param #请求参数赋值
            else: #没有依赖数据
                case['case_params'] = params
        response,assert_value = RequestHandler(case).get_response #获取到响应数据和断言数据
        if case['case_response_key'] != '': #判断响应数据是否有被依赖
            savevalue = SaveRunBeDependValue()
            savevalue.savedependvalue(case['case_response_key'],response)#把依赖的数据实时保存到数据库
        # 制作 allure 报告
        """  执行断言 """
        assert assert_value[0] == assert_value[1]
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