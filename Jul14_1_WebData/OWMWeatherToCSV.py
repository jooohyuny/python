# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime

con = connect("yun/yun@195.168.9.85:1521/xe")

sql = "select * from owm_weather order by ow_date"
cur = con.cursor()
cur.execute(sql)

# for문의 문법이 원래
# for 변수 in 컬렉션:
# for w in cur:        # tuple 하나 통으로 받는 버전
#    print(type(w)) 

# append모드로, utf-8인코딩방식(Excel은 원래 utf-8을 감당못한다)
f = open("C:/yun/owmWeather.csv","a",encoding= "utf-8")

# type은 확인하고 tuple의 특징을 나눠서 쓸 수 있다
# tuple 나눠서 받는 버전
for d, desc, temp, humi in cur:
    # Python은 접근제어자가 없어서 캡슐화가 없고
    # 멤버변수에 직접 접근하니깐 아래와 같이 쓴다
    f.write("%d," % d.year)
    f.write("%d," % d.month)
    f.write("%d," % d.day)
    f.write("%d," % d.hour)
    f.write("%s," % desc)
    f.write("%.2f," % temp)
    f.write("%d\n" % humi)
    # Python에서 Java처럼 쓰는 방식은 아래와 같다
    # print(datetime.strftime(d,"%Y,%m,%d,%H:"))
f.close()
cur.close()
con.close()