# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

# csv파일(첫줄에 제목 있는)로
a =pd.read_csv("C:/yun/titanic.csv")
print(a)
print('---------------------------------------------------------')

# csv파일(첫줄에 제목 없는)
b = pd.read_csv("C:/yun/subway.csv", names=["년","월","일","노선","역이름","승차인원","하차인원"])
print(b)
print('---------------------------------------------------------')

# 어쨌든 파일
# .csv, .txt : 확장자 - MS Windows에만 있는 허상
c = pd.read_csv("C:/yun/kakaoBlog.txt", sep="\t", names = ["제목","내용","블로그"])
print(c)
print('---------------------------------------------------------')

# OracleDB에 있는거 
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from owm_weather"
d = pd.read_sql(sql, con)
print(d)
print('---------------------------------------------------------')

sql = "select sd_MSRRGN_NM, avg(sd_PM10) from seoul_dust group by sd_MSRRGN_NM"
e = pd.read_sql(sql, con)
print(e)

con.close()

# 정형데이터
#    oracleDB에 : DB에서 SQL로 처리
#    csv파일 : Hadoop으로 처리
# 비정형데이터
#    데이터프레임은 좀 아니고
# -> pandas??






