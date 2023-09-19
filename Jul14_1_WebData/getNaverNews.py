# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import ElementTree, fromstring
from pymongo.mongo_client import MongoClient
#######################################
# 웹사이트에서 clean에 작성한거처럼 쓸모없는 부분은 replace를 이용해서 바꿔주고
# 비정형 데이터를 MongoDB에 저장하는 방법은 
# {} : JS의 객체/Python dict 와 같다
#######################################
def clean(s):
    s = s.replace("&apos;","").replace("&amp;","")
    s = s.replace("<b>","").replace("</b>","")
    s = s.replace("&quot;","")
    return s
#######################################
q = quote("경제") # ㅋ -> %2A

# 요청헤더
h = {"X-Naver-Client-Id" : "P3qqr6A33BZP7naZRPUV",
     "X-Naver-Client-Secret" : "xg_TyVqLlS"}


huc = HTTPSConnection("openapi.naver.com")
huc.request("GET","/v1/search/news.xml?query=" + q, headers=h)
resbody = huc.getresponse().read()
# print(resbody.decode())

con = MongoClient("195.168.9.85")
db = con.xe
for n in fromstring(resbody).getiterator("item"):
    data = {"title" : clean(n.find("title").text),
            "desc" : clean(n.find("description").text),
            "date" : clean(n.find("pubDate").text)}
    db.naverNewsEconomy.insert_one(data)

con.close()
huc.close()