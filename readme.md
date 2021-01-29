# Api框架概述

##     环境要求：

Python版本：3+

第三方库：requests、PyMySql、pytest、openpyxl、xlrd、allure-pytest、bs4

本地需安装allure，并配置环境变量

## 测试用例设计思路：

![image-20210130002646871](C:\Users\83830\AppData\Roaming\Typora\typora-user-images\image-20210130002646871.png)

case_id：case编号，自行定义

case_name：可以定义为api的所属的模块名称，allure报告的功能名

case_run：判断是否执行case

case_url：api地址 

case_method：请求方式  **说明**：目前只处理GET/POST请求，其他请求方式待开发...

case_params：请求参数 **说明**：对于GET请求，参数可以在url传入，也可以在次列传入，需以字典形式传入

​						`如果有参数依赖，参数值为<依赖key>`

case_type：请求参数类型 **说明**：目前只支持FORM/JSON格式

case_response_key：是否被依赖，为空则没有被依赖，有值则被依赖

case_depend_key：是否依赖其它case，为空则没有依赖其它case，有值则依赖其它case

case_expect：预期值

other：其他