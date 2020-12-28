# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 22:16
# @Project : InterfaceProject

import json
import requests
from bs4 import BeautifulSoup
from uti.LoggerHandler import logger
class DependHandler(object):

    # def __init__(self, case):
    #     self.case = case
    #     try:
    #         self.case_expect = json.loads(self.case['case_expect'])
    #     except:
    #         self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response = self.send_request()
        return response

    def send_request(self,method,url,data = None):
        """ 发请求 """
        try:
            response = requests.request(
                method=method,
                url=url,
                data=data
            )
            content_type = response.headers['Content-Type']
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                response = getattr(self, '_check_{}_response'.format(content_type))(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(url)})
            return {'response': "请求发送失败，详细信息： url={}".format(url)}
        print(response.json())
        return response

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
        else:  # 执行成功
            logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
            return {key: self.case_expect[key]}, {key: response[key]}

    # def _check_html_response(self, response):
    #     """ 校验html类型的数据"""
    #     soup_obj = BeautifulSoup(response.text, 'html.parser')
    #     title = soup_obj.find('title').text
    #     return title, self.case_expect
    #
    # def _check_params(self):
    #     """ 整理参数 """
    #     if self.case['case_params']:
    #         """
    #         做扩展
    #         """
    #         pass
    #     else:
    #         return {}

if __name__ == '__main__':
    d = DependHandler()
    method = 'GET'
    url = 'https://sj.qq.com/myapp/searchAjax.htm?kw=微信'
    # param = {'kw':'UC浏览器极速版'}
    d.send_request(method,url)