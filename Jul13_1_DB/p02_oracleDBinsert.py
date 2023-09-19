# -*- coding:utf-8 -*-
from cx_Oracle import connect

# J : JDBC -> ConnectionPool -> MyBatis

# 연결
con = connect("yun/yun@195.168.9.85:1521/xe")

# 데이터 확보
n = input("이름  : ")
c = input("종류  : ")
p = int(input("가격  : "))

# SQL(완성, ; 빼고)
sql = "insert into jul13_coffee values('%s', '%s', %d)" % (n, c, p)

# DB관련 작업 총괄메니저(preparedStatement)겸 결과(ResultSet)
cur = con.cursor()

# SQL을 서버로 전송, 실행 -> 결과가 cur에 저장
cur.execute(sql)

if cur.rowcount == 1:
    print("성공")
    con.commit()

cur.close()
con.close()







