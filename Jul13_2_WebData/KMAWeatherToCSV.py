# -*- coding:utf-8 -*-

# DB에 저장된 기상청 날씨예보 데이터
# csv로 저장하는 프로그램
#
# 년,월,일,시,기온,날씨
# 2023,07,13,21,20.0,비
from cx_Oracle import connect
from datetime import datetime
con = connect("yun/yun@195.168.9.85:1521/xe")
cur = con.cursor()

sql = "select * from kma_weather order by kw_date, kw_hour"
cur.execute(sql)

f = open("C:/yun/kmaWeather.csv","a",encoding= "utf-8")

for d, h, t, w in cur:
    # print(datetime.strftime(d,"%Y,%m,%d"))
    f.write(datetime.strftime(d,"%Y,%m,%d,"))
    f.write("%d,%.1f,%s\n" % (h, t, w))

f.close()
cur.close()
con.close()

