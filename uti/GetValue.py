# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 22:58
# @Project : InterfaceProject

class GetValue(object):
    def get_json_value_by_key(self, in_json, target_key,results = []):
        """
        根据key值读取对应的value值
        :param in_json:传入的json
        :param target_key: 目标key值
        :param results:
        :return:数据依赖的value列表
        """
        if isinstance(in_json, dict):  # 如果输入数据的格式为dict
            for key in in_json.keys():  # 循环获取key
                data = in_json[key]
                self.get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value
                if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                    results.append(data)
        elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
            for data in in_json:  # 循环当前列表
                self.get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素
        return results

if __name__ == '__main__':
    test = GetValue()
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
    print(type(test_json))
    a = test.get_json_value_by_key(test_json,'apkUrl')
    print(a)