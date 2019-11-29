# -*- coding: utf-8 -*
"""
    公共函数方法
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from utils.operation_excel import OperationExcel

class Common:

    # 输出文件地址
    def get_file_path(self, file_name):
        return rootPath + '/doc/' + file_name + '.xls'

    # 文件写入
    def write_file_excel(self,file_name, row, col, value):
        excel = OperationExcel(self.get_file_path(file_name))
        excel.write_value(row, col, value)
        return True
    
    # 获取表格列数
    def get_mac_col(self, file_name):
        excel = OperationExcel(self.get_file_path(file_name))
        col = excel.get_mac_col()
        return col

    # 获取表格行数
    def get_max_row(self,file_name):
        excel = OperationExcel(self.get_file_path(file_name))
        row = excel.get_max_row()
        return row

    # 获取文件名称
    def get_file_name(self):
        file_name = os.path.basename(__file__).split(".")[0]
        return file_name
    