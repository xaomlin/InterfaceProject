# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 18:47
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

    # @property
    # def get_response(self):
    #     """ 获取请求结果 """
    #     response = self.send_request(self.case)
    #     return response

    def send_request(self, method, url, params=None):
        """ 发请求 """
        try:
            response = requests.request(
                method=method,
                url=url,
                params=params
            )
            print(response)
            content_type = response.headers['Content-Type']
            print(content_type)
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
                content_type.split("/")[-1]
            print(content_type)
            if hasattr(self, '_check_{}_response'.format(content_type)):
                responses = getattr(self, '_check_{}_response'.format(content_type))(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(url)})
            return {'response': "请求发送失败，详细信息： url={}".format(url)}

        return responses

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
        else:  # 执行成功
            logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
            return {key: self.case_expect[key]}, {key: response[key]}
    #
    # def _check_html_response(self, response):
    #     """ 校验html类型的数据"""
    #     soup_obj = BeautifulSoup(response.text, 'html.parser')
    #     title = soup_obj.find('title').text
    #     return title
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
    r = RequestHandler()
    url = 'https://sj.qq.com/myapp/searchAjax.htm?kw=微信'
    method = 'GET'
    r.send_request(method, url)
