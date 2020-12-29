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

    def send_depend_request(self,method,url,data = None):
        """ 发请求 """
        try:
            response = requests.request(
                method=method,
                url=url,
                data=data
            )
            content_type = response.headers['Content-Type']
            print(content_type)
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            print(content_type)
            # if hasattr(self, '_check_{}_response'.format(content_type)):
            #     response = getattr(self, '_check_{}_response'.format(content_type))(response)
            # else:
            #     raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(url)})
            return {'response': "请求发送失败，详细信息： url={}".format(url)}
        print(response.json())
        print(response.json()['total'])
        return response


if __name__ == '__main__':
    d = DependHandler()
    # method = 'GET'
    # url = 'https://sj.qq.com/myapp/searchAjax.htm?kw=微信'
    # # param = {'kw':'UC浏览器极速版'}
    # d.send_depend_request(method,url)
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
    test = d.send_depend_request('apkUrl',test_json)
