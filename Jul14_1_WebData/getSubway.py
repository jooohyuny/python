# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
# HTTP통신 -> 파싱   -> 파일
#                -> 하루데이터 먼저 다 

# 3) 파일 바로 저장
f = open("C:/yun/subway.csv","a",encoding= "utf-8")

# 1) HTTP통신여부
huc = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2015, 2023):
    for m in range(1,13):
        for d in range(1,32):
            when = "%d%02d%02d" % (y,m,d)
            huc.request("GET","/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/610/" + when)
            resBody = huc.getresponse().read()
            # print(resBody.decode())
            
            # 2) 파싱
            for sub in fromstring(resBody).getiterator("row"):
                # print(sub.find("USE_DT").text)
                useDt = sub.find("USE_DT").text
                f.write("%s,%s,%s," % (useDt[0:4],useDt[4:6],useDt[6:8]))
                f.write("%s," % sub.find("LINE_NUM").text)
                f.write("%s," % sub.find("SUB_STA_NM").text)
                f.write("%s," % sub.find("RIDE_PASGR_NUM").text)
                f.write("%s\n" % sub.find("ALIGHT_PASGR_NUM").text)
            print(when)

huc.close()

f.close()