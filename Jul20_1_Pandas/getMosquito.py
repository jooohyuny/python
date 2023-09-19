# -*- coding:utf-8 -*-
# 서울시 모기예보제 정보
# 2016.5.1 ~ 2016.10.31
# ...
# 어제까지
# csv로 
from http.client import HTTPConnection
from cx_Oracle import connect
from xml.etree.ElementTree import fromstring

f = open("C:/yun/mosquito.csv","a",encoding= "utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2016,2024):
    for m in range(5,11):
        for d in range(1,32):
            t = "%d-%02d-%02d" % (y,m,d)
            huc.request("GET","/575a4655496b636839386f58586542/xml/MosquitoStatus/1/1/" + t)
            resBody = huc.getresponse().read()
            
            for mq in fromstring(resBody).getiterator("row"):
                f.write("%s," % mq.find("MOSQUITO_DATE").text)
                f.write("%s," % mq.find("MOSQUITO_VALUE_WATER").text)
                f.write("%s," % mq.find("MOSQUITO_VALUE_HOUSE").text)
                f.write("%s\n" % mq.find("MOSQUITO_VALUE_PARK").text)
            print(t)
huc.close()
f.close()
