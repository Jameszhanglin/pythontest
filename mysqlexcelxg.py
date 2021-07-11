#!/usr/bin/env python
# coding=utf-8
import xlrd
import pymysql
import datetime

# 读取EXCEL中内容到数据库中
path = r"D:\\BaiduSyncdisk\\云门诊文件\\建德\\总府药品字典表 .xls"
wb = xlrd.open_workbook(path, encoding_override="uft-8")
sh = wb.sheet_by_index(0)
dfun = []
nrows = sh.nrows  # 行数
ncols = sh.ncols  # 列数
fo = []

fo.append(sh.row_values(0))
for i in range(1, nrows):
    row_values = sh.row_values(i)
    for j in range(ncols):
        cell = sh.cell(i, j)
        if cell.ctype == xlrd.XL_CELL_DATE:
            # 将日期数据转换为datetime对象
            dt_tuple = xlrd.xldate_as_tuple(cell.value, wb.datemode)
            dt = datetime.datetime(*dt_tuple)
            # 将datetime对象转换为字符串
            row_values[j] = dt.strftime('%Y-%m-%d')
    dfun.append(row_values)

conn = pymysql.connect(host='118.31.49.142', user='zhl', passwd='zhl123', db='test_db')
cursor = conn.cursor()
# 创建table
cursor.execute("create table zfyd1(" + fo[0][0] + " varchar(100));")
# 创建table属性
for i in range(1, ncols):
    cursor.execute("alter table zfyd1 add " + fo[0][i] + " varchar(100);")
val = ''
for i in range(0, ncols):
    val = val + '%s,'
print(dfun)

# 这里应该是建完表后导入数据才对
cursor.executemany("insert into zfyd1 values(" + val[:-1] + ");", dfun)
conn.commit()