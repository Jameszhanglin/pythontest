import xlrd
wb = xlrd.open_workbook(r'E:\学习\标价签1.xls' )#读取工作薄
ws = xlrd.open_workbook(r'E:\学习\标价签1.xls' ).sheet_by_name('copy') #读取工作薄
wsobj = wb.sheets() # 读取工作薄下面的所有工作表对旬
wsname = wb.sheet_names() #读取工作薄下的所有工作表名称
ws1 = wb.sheet_by_name('copy')
ws2 = wb.sheet_by_index(1)
ws3 = wb.sheets()[1]

crow = ws.nrows
ccol = ws.ncols
row_data = ws.row_values(1) #指定行数据
col_data = ws.col_values(1) #指定列数据
cell_data_1 = ws.cell_value(1,1) #获取指定单元格数据
cell_data_2 = ws.cell(1,1).value  #获取指定单元格数据
cell_data = ws.cell(1,1)

import  xlwt
nwb = xlwt.Workbook(encoding='utf-8') #新建工作薄
nws = nwb.add_sheet('test')  #添加新工作表
nws.write(1,2,'阿川') #写入单元格
nwb.save(r'E:\学习\test.xls') #保存工作薄



print(cell_data)

print(cell_data_2)


from xlutils.copy import copy  #导入 xlutils  中的复制模块



