# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# MongoDB : NoSQL -> JavaScript로
#    JavaScript나  Python나 문법이....
#    테이블 -> JS배열 : [] : Python list
#    데이터 -> JS객체 : {} : Python dict
con = MongoClient("195.168.9.85")
db = con.xe

n = input("이름 : ")
c = input("종류 : ")
p = int(input("가격 : "))

# Python dict(JS객체랑 생긴게 같음)
d = {"name" : n, "cate" : c, "price" : p}

# MongoDB문법 거의 그대로
result = db.jul13_coffee.insert_one(d)

if result.acknowledged:
    print("성공")

con.close()







