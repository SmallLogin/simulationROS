#coding=utf-8
'''
Created on 2016年1月22日
@author: cf
'''
import xlrd 
from xlutils.copy import copy
xls=xlrd.open_workbook(r'grade.xls',formatting_info=True)
xlsc=copy(xls)
shtc=xlsc.get_sheet(0)

shtc.write(1,1,'#####')
shtc.write(1,2,'++++++')
xlsc.save(r'new.xls')