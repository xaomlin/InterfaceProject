# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 18:59
# @Project : InterfaceProject

from uti.ExcelHandler import ExcelHandler
from uti.DependHander import DependHandler
from uti.GetValue import GetValue
class GetData(object):
    def __init__(self):
        self.excelhandler = ExcelHandler()
        self.dependhandler = DependHandler()
        self.getvalue = GetValue()
    def get_data(self):
        request_data = self.excelhandler.get_request_data()
        for i in range(len(request_data)):
            is_depend = request_data['case_depend_id']
            if is_depend != '':
                depend_key = request_data[i]['case_depend_key']
                case_id = is_depend

                url = request_data[case_id].get('case_url')
                methon = request_data[case_id].get('case_method')
                params = request_data[case_id].get('case_params')
                depend_response = self.dependhandler.send_depend_request(url,methon,params).json()
                self.getvalue.get_json_value_by_key(depend_response,depend_key)