# -*- coding:utf-8 -*-
from cx_Oracle import connect
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from jul13_coffee"
cur = con.cursor()
cur.execute(sql)

f = open("C:/yun/coffee.csv","a",encoding= "utf-8")
for name, cate, price in cur:
    f.write("%s,%s,%d\n" % (name, cate ,price))

f.close()
cur.close()
con.close()

