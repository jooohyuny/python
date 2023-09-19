# -*- coding:utf-8 -*-

# DB에 저장된 서울시 실시간 미세먼지 데이터를
# csv로 저장하는 green
#
from cx_Oracle import connect
from datetime import datetime
con = connect("yun/yun@195.168.9.85:1521/xe")
cur = con.cursor()

sql = "select * from seoul_dust order by sd_date, sd_MSRRGN_NM, sd_MSRSTE_NM"
cur.execute(sql)

f = open("C:/yun/seoul_dust.csv","a",encoding= "utf-8")

for date, rgn, ste, pm10, pm25, grade in cur:
    # print(datetime.strftime(d,"%Y,%m,%d,%H,"))
    f.write(datetime.strftime(date,"%Y,%m,%d,%H,"))
    f.write("%s," % rgn)
    f.write("%s," % ste)
    f.write("%d,%d," % (pm10, pm25))
    f.write("%s\n" % grade)
f.close()
cur.close()
con.close()

