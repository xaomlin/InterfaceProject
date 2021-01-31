# Api框架概述

##     环境要求：

Python版本：3+

第三方库：requests、PyMySql、pytest、openpyxl、xlrd、allure-pytest、bs4、pyyaml

本地需安装allure，并配置环境变量

## 测试用例设计：

![image-20210131235756843](C:\Users\83830\AppData\Roaming\Typora\typora-user-images\image-20210131235756843.png)

case_id：case编号，自行定义

case_name：可以定义为api的所属的模块名称，allure报告的功能名

case_model：从yaml文件获取参数一级名称

case_run：判断是否执行case

case_url：api地址 

case_method：请求方式  **说明**：目前只处理GET/POST请求，其他请求方式待开发...

case_params：从yaml文件获取参数的key **说明**：对于GET请求，参数可以在url传入，也可以在次列传入，需以字典形式传入

​						`如果有参数依赖，参数值为<依赖key>`

case_type：请求参数类型 **说明**：目前只支持FORM/JSON格式

case_response_key：是否被依赖，为空则没有被依赖，有值则被依赖

case_depend_key：是否依赖其它case，为空则没有依赖其它case，有值则依赖其它case

case_expect：预期值

other：其他

## 用例执行方案

使用@pytest.mark.parametrize()装饰器获取用例

用例没有被依赖，也没有依赖字段：判断是否执行，是则直接执行，否不执行

用例被依赖：判断是否执行，如果不执行，则在setup先执行该用例，执行后把依赖字段保存到数据库，如果执行，则在test_case执行，执行后把依赖字段保存到数据库

测试用例有依赖别的用例：在test_case中执行前先数据库获取依赖字段，替换到参数，更换参数再执行该用例

## 后续看开发方向

1. 测试用例多表则行，建立数据库，从数据库中获取测试用例
2. 目前只支持但字段依赖及被依赖，后续看有无必要添加多字段
3. 后续看是否有必要测试表中添加headers

