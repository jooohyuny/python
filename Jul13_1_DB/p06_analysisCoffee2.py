# -*- coding:utf-8 -*-
from cx_Oracle import connect

# OracleDB서버에 100TB 데이터
# OracleDB서버의 강력한 cpu로 계산
# 4766.66을 가져옴
con = connect("yun/yun@195.168.9.85:1521/xe")
# 1) 평균가
sql = "select avg(c_price) from jul13_coffee"
cur = con.cursor()
cur.execute(sql)
for p in cur:
    print(p[0])
cur.close()
print("---------------")

# 2) 메뉴가 총 몇 종류
sql = "select count(*) from jul13_coffee"
cur = con.cursor()
cur.execute(sql)
for p in cur:
    print(p[0])
cur.close()
print("---------------")

# 3) 최고가 메뉴 뭐?
sql = "select *"
sql += " from jul13_coffee"
sql += " where c_price = ("
sql += "    select max(c_price)"
sql += "    from jul13_coffee"
sql += " )" 
cur = con.cursor()
cur.execute(sql)
for name,cate,price in cur:
    print(name, cate, price)
cur.close()
print("---------------")

# 4) 최저가 메뉴 뭐?
sql = "select *"
sql += " from jul13_coffee"
sql += " where c_price = ("
sql += "    select min(c_price)"
sql += "    from jul13_coffee"
sql += " )" 
cur = con.cursor()
cur.execute(sql)
for name,cate,price in cur:
    print(name, cate, price)
cur.close()
print("---------------")

# 5) 카테고리별 평균가
sql = "select c_cate, avg(c_price)"
sql += " from jul13_coffee"
sql += " group by c_cate"
cur = con.cursor()
cur.execute(sql)
for cate,price in cur:
    print(cate, price)
cur.close()
print("---------------")

con.close()













