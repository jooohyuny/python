# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

# Python + OracleDB : cx_Oracle.py
# Python + mongoDB : pymongo.py
#     cmd -> pip install pymongo
#####################################
try:
    con = MongoClient("195.168.9.85")
    db = con.xe     # con.db명
    print("성공")
    con.close()
except Exception as e:
    print(e)