# -*- coding: utf-8 -*-
# @Project : InterfaceProject
import os
import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 脚本路径
file_path = '接口测试示例.xlsx'
TEST_CASE_PATH = os.path.join(BASE_PATH, 'data', file_path)

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