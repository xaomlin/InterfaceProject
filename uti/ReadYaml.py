# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 18:54
# @Project : InterfaceProject

import yaml
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
yaml_ = os.path.join(path,'data','Param.yaml')
class ReadYaml(object):
    def __init__(self,yaml_path = None):
        # 由于官方提示load方法存在安全漏洞，所以读取文件时会报错。加上warning忽略，就不会显示警告
        yaml.warnings({'YAMLLoadWarning': False})
        if yaml_path != None:
            self.yaml_path = yaml_path
        else:
            self.yaml_path = yaml_
        with open(self.yaml_path, 'r', encoding='utf-8') as yaml_file:
            yaml_file = yaml_file.read()
            self.datas = yaml.load(yaml_file)

    def get_yaml_param(self,object,key):
        # print(self.datas[object][key])
        return self.datas[object][key]


if __name__ == '__main__':
    r = ReadYaml()
    r.get_yaml_param('HEXIAOYU','phoneLogin')