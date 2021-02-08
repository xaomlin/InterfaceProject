# -*- coding: utf-8 -*-
# @Project : InterfaceProject
'''

请求相关
'''

import json
import requests
from bs4 import BeautifulSoup
from uti.LoggerHandler import logger
from uti.ExcelHandler import ExcelHandler

class RequestHandler(object):

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response,assert_value, = self.send_request()
        return response,assert_value

    def get_session(self):
        self.session = requests.Session()
        return self.session

    def send_request(self):
        """ 发请求 """
        method = self.case['case_method'].upper()
        data = self._check_params()
        # print(data)
        url = self.case['case_url']
        type = self.case['params_type'].upper()
        try:
            if method == 'GET':
                if data != '':
                    response = requests.request(method=method, url=url, params=data)
                else:
                    response = requests.request(method=method, url=url)
            elif method == 'POST':
                if type == 'FORM':  # 发送表单数据，使用data参数传递
                        response = requests.request(method=method, url=url, data=data)
                elif type == 'JSON':  # 如果接口支持application/json类型，则使用json参数传递
                        response = requests.request(method=method, url=url, json=data)
                else:  # 如果接口需要传递其他类型的数据比如 上传文件，调用下面的请求方法
                    response = requests.request(method=method, url=url)
                    # 如果请求方式非 get 和post 会报错，当然你也可以继续添加其他的请求方法
                # response_text = response.text
            else:
                raise ValueError('request method "{}" error ! please check'.format(method))
            content_type = response.headers['Content-Type']
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                assert_data = getattr(self, '_check_{}_response'.format(content_type))(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']
        response = response.json()
        return response,assert_data

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
            else:  # 执行成功
                logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
                return {key: self.case_expect[key]}, {key: response[key]}

    def _check_html_response(self, response):
        """ 校验html类型的数据"""
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        title = soup_obj.find('title').text
        return title, self.case_expect

    def _check_params(self):
        """ 整理参数 """
        param = self.case['case_params']
        # print(type(param))
        if param != '':
            if isinstance(param, str):
                data = json.loads(param)
                return data
            if isinstance(param,dict):
                return param
        else:
            return None

if __name__ == '__main__':
    data = {'case_id': 'case_5', 'case_name': '搜索APP', 'case_run': 'yes',
            'case_url': 'https://sj.qq.com/myapp/searchAjax.html', 'case_method': 'GET', 'case_depend_id': '',
            'case_depend_key': 'apkUrl', 'case_depend_param': '', 'case_params': {"kw": "美团"},
            'case_expect': '{"success":true}', 'other': ''}
    data1 = {'case_id': 'case_5', 'case_name': '搜索APP', 'case_run': 'yes',
            'case_url': 'https://sj.qq.com/myapp/searchAjax.html?kw=美团', 'case_method': 'GET', 'case_depend_id': '',
            'case_depend_key': 'apkUrl', 'case_depend_param': '', 'case_params': '',
            'case_expect': '{"success":true}', 'other': ''}
    data2 = {'case_id': 'case_5', 'case_name': '搜索APP', 'case_run': 'yes',
                'case_url': 'https://app.nicebooker.com/parental/app/v1/user/phoneLogin', 'case_method': 'post', 'case_depend_id': '',
                'case_depend_key': 'apkUrl', 'case_depend_param': '', 'case_params': '{"client":{"bundleId":"com.qlchat.hexiaoyu","caller":"app","ex":{"model":"VOG-AL00"},"os":"25","platform":"android","ver":"1.3.1"},"data":{"password":"01a3a90a410be072fbcffe9699816414","phoneNum":"15989160853"},"id":"1610968043407474","sign":"a7e4be19722660d16d55a330cdd97342","timestamp":1610968043407,"user":{}}',
                'case_expect': '{"state":{"code":0,"msg":"操作成功"}}','param_type':'json', 'other': ''}
    r = RequestHandler(data2)
    # r.send_request()
    r.get_response