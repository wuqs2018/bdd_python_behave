# -*- coding: utf-8 -*

import os
import xlrd
import xlwt
import time
from xlutils.copy import copy

"""
内容写入 excel 表格中
"""

class OperationExcel:

    def __init__(self, file_path=None):

        # 判断文件目录是否存在，存在使用传入的路径，否系统默认路径
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = 'E:/test_dir/data/data.xls'
        
        # 判断文件是否存在，不存在创建文件
        is_file = os.path.exists(self.file_path)
        if is_file == False:
            filename = xlwt.Workbook()
            sheet = filename.add_sheet('Sheet1')
            sheet.write(0, 0, '')
            filename.save(self.file_path)
        
        # table 文件
        excel = xlrd.open_workbook(self.file_path)
        self.table = excel.sheets()[0]

    
    # 获取excel表格总行数
    def get_max_row(self):
        return self.table.nrows
    
    # 获取excel表格总列数
    def get_mac_col(self):
        return self.table.ncols

    '''
        内容写入Excel表中  

        @author qisheng.wu@newtype.io 2019-09-10
        @param  row Number    行数    必填
        @param  col Number    列数    必填
        @param  value String  内容    必填
        @return 
    ''' 
    def write_value(self, row, col, value):

        # excel 文件参数不能为空
        if row == '' or col == '' or value == '':
            return False

        # 复制上一次修改excel内容
        read_data = xlrd.open_workbook(self.file_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)

        # 内容写入指定行、列表格中
        sheet_data.write(row, col, value)
        write_data.save(self.file_path)
