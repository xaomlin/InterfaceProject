# -*- coding: utf-8 -*-
# @Project : InterfaceProject
import os
import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 脚本路径
# file_path = 'Test.xlsx'
# TEST_CASE_PATH = os.path.join(BASE_PATH, 'data', file_path)
file_name = 'Test,aa' #第一个为依赖数据库表
CASE_PATH = os.path.join(BASE_PATH, 'data')

# 参数路径
yaml_name = 'Test.yaml'
PARAM_PATH = os.path.join(BASE_PATH, 'Param',yaml_name)

# ------------ allure 相关配置 -----------

result_path = os.path.join(BASE_PATH,'report', 'result')
allure_html_path = os.path.join(BASE_PATH,'report', 'allure-report')
ALLURE_COMMAND = 'allure generate {} -o {} --clean'.format(result_path, allure_html_path)

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'  # 文件输出流

# 日志文件命名

LOG_FILE_NAME = os.path.join(BASE_PATH, 'logs', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log')

if __name__ == '__main__':
    print(os.path.abspath(__file__))
    print(BASE_PATH)