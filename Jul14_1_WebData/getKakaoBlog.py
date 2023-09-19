# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from pymongo.mongo_client import MongoClient
from xml.etree.ElementTree import fromstring
from json import loads

############################################################
def clean(s):
    s = s.replace("<b>","").replace("</b>","")
    return s

############################################################
# REST API 키  :  b21348a9e3263c7abefcf6b76a30ee50
# JavaScript 키  :  e38096f306538fd5954fab266598a5af

q = quote("맛집") # URL인코딩

# 요청헤더
# h = {"헤더명" : "값","헤더명" : "값",...}
h = {"Authorization" : "KakaoAK b21348a9e3263c7abefcf6b76a30ee50"}

huc = HTTPSConnection("dapi.kakao.com")
huc.request("GET", "/v2/search/blog?query=" + q, headers = h)
resbody = huc.getresponse().read()
############################################################
# 정형 : OracleDB
# 비정형 : MongoDB
# 분석하는날 DB서버 죽으면??
# 빅데이터가 DB서버 한대에 저장??
# 데이터중에 특정부분 손상?

# 서버 여러대로 ElasticSearch네트워크 구성
# 나눠서, 복사본 몇개씩
############################################################
con = MongoClient("195.168.9.85") # MongoDB서버 연결
db = con.xe # xe라는 이름의 db

# 비정형 -> MongoDB -> JS객체형태로

blogData = loads(resbody)
for b in blogData["documents"]:
    # JS객체형태로(Python dict형태로)
    data = {"title" : clean(b["title"]),
            "contents" : clean(b["contents"]),
            "blogname" : clean(b["blogname"])}
    db.kakaoBlog.insert_one(data)
con.close()
huc.close()












