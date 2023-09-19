# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# 비정형데이터
# 데이터자체에 , 그러므로 csv는 안된다
con = MongoClient("195.168.9.85")
db = con.xe

f = open("C:/yun/naverNews.txt","a",encoding= "utf-8")
for n in db.naverNews.find():
    f.write("%s\t" % n["title"])
    f.write("%s\n" % n["desc"])

f.close()
con.close()