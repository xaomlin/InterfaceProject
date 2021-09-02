# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 22:16
# @Project : InterfaceProject

import json
import requests
from bs4 import BeautifulSoup
from uti.LoggerHandler import logger


class DependHandler(object):

    # @property
    # def get_response(self):
    #     """ 获取请求结果 """
    #     response = self.send_depend_request()
    #     return response

    def send_depend_request(self, url, method, type, headers=None, data=None) -> str:
        """ 发请求 """
        method = method.upper()
        type = type.upper()
        try:
            if data != '':
                if isinstance(data, str):
                    data = json.loads(data)
            if method == 'GET':
                if data != None:
                    response = requests.request(method=method, url=url, headers=headers, params=data)
                else:
                    response = requests.request(method=method, url=url, headers=headers)
                response_data = response.json()
                return response_data
            elif method == 'POST':
                if type == 'FORM':  # 发送表单数据，使用data参数传递
                    response = requests.request(method=method, url=url, headers=headers, data=data)
                elif type == 'JSON':  # 如果接口支持application/json类型，则使用json参数传递
                    response = requests.request(method=method, url=url, headers=headers,json=data)
                else:  # 如果接口需要传递其他类型的数据比如 上传文件，调用下面的请求方法
                    response = requests.request(method=method, headers=headers, url=url)
                    # 如果请求方式非 get 和post 会报错，当然你也可以继续添加其他的请求方法
                response_data = response.json()
                return response_data
        except:
            logger().error({'依赖接口执行失败': " url={}".format(url)})


if __name__ == '__main__':
    d = DependHandler()
    method = 'GET'
    url = 'https://sj.qq.com/myapp/searchAjax.htm'
    param = {'kw': 'UC浏览器极速版'}
    print(d.send_depend_request(url, method, 'json', param))
    test_json = {
        "obj": {
            "appDetails": [
                {
                    "apkMd5": "228573CE7F198D9053F03F47B470A2CA",
                    "apkPublishTime": 1609141840,
                    "apkUrl": "https://imtt.dd.qq.com/16891/apk/228573CE7F198D9053F03F47B470A2CA.apk?fsname=com.tencent.mm_7.0.22_1820.apk&csr=1bbd",
                    "appDownCount": 8531688189,
                    "appId": 10910,
                    "appName": "微信",
                    "appRatingInfo": {
                        "averageRating": 3.5332585935663525,
                        "ratingCount": 553030,
                        "ratingDistribution": {
                            "1": 122849,
                            "2": 37170,
                            "3": 62805,
                            "4": 82636,
                            "5": 247570
                        }
                    },
                    "versionName": "7.0.22"
                },
                {
                    "apkMd5": "A650E524361B909386224AB3AA18DD30",
                    "apkPublishTime": 1608615869,
                    "apkUrl": "https://imtt.dd.qq.com/16891/apk/A650E524361B909386224AB3AA18DD30.apk?fsname=com.boly.wxmultopen_3.0.9_309.apk&csr=1bbd",
                    "appDownCount": 22041880,
                    "appId": 12204155,
                    "appName": "多开助手",
                    "appRatingInfo": {
                        "averageRating": 4.861168603725521,
                        "ratingCount": 6281,
                        "ratingDistribution": {
                            "1": 196,
                            "2": 12,
                            "3": 12,
                            "4": 28,
                            "5": 6033
                        }
                    },
                    "versionName": "3.0.9"
                }
            ]
        }
    }
    # test = d.send_depend_request('apkUrl',test_json)
