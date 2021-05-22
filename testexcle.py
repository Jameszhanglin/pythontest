import xlrd
import pymysql
import  datetime

# 连接本地数据库
conn = pymysql.connect("127.0.0.1,1433","sa","123456","test")

cursor = conn.cursor()

# excle
fname = "123.xls"

#打开文件

bk = xlrd.open_workbook(fname)
#打开工作表
sh = bk.sheets()[0]
#获取行数
start_time = datetime.datetime.now()
sql3 = ''
#遍历所有行
 for i in range(1,sh.nrows):
     a = []
     sql = '('
     #遍历所有列
     for j in range(sh.ncols):
         #将excle每一旬都用，隔开
         sql += "'" + str(sh.cell(i,j).valer) + "'" + ','
         sql2 = sql.strip(",")
         sql3 += sql2.strip()+'),'
     #1000行执行一次
     if  1%1000==0:
         sql3 = sql3.rstrip("")
         sql1 = "insert into flow(id,saledate,danwei) values %s"%sql3
         #执行sql
         cursor.execute(sql1)
         sql=""
         sql3=""
     sql3 = sql3.rstrip(",")
     sql1 = "insert into flow(id,saledate,danwei) values %s" % sql3
     cursor.execute(sql1)

     end_date = datetime.datetime.now()
     speed = end_date-start_time

     print(speed)