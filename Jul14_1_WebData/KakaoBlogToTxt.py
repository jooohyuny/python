# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("195.168.9.85")
db = con.xe

f = open("C:/yun/kakaoBlog.txt","a",encoding= "utf-8")
for k in db.kakaoBlog.find():
#     f.write("%s\t" % k["title"])
#     f.write("%s\t" % k["contents"])
#     f.write("%s\n" % k["blogname"])
#########################################
    f.write(k["title"] + "\t")
    f.write(k["contents"] + "\t")
    f.write(k["blogname"] + "\n")

#     print(k["title"])
#     print(k["contents"])
#     print(k["blogname"])
f.close()
con.close()



