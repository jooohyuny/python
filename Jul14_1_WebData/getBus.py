# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

y = input("년  : ")
f = open("C:/yun/bus%s.csv" % y,"a",encoding= "utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")

for m in range(1,13):
    for d in range(1,32):
        for i in range(1,40002,1000):
            t = "/%d/%d/%s%02d%02d" % (i, i+999, y, m, d)
            huc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew" + t)
            resBody = huc.getresponse().read()
    
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData: 
                cbssn = busData["CardBusStatisticsServiceNew"]
                r = cbssn["row"]
                for bus in r:
                    useDt = bus["USE_DT"]
                    f.write("%s,%s,%s," % (useDt[0:4],useDt[4:6],useDt[6:8]))
                    f.write("%s," % bus["BUS_ROUTE_NM"])
                    f.write("%s," % bus["BUS_STA_NM"])
                    f.write("%s," % str(bus["RIDE_PASGR_NUM"]).replace(".0",""))
                    f.write("%s\n" % str(bus["ALIGHT_PASGR_NUM"]).replace(".0",""))
        print(y,m,d)
huc.close()
f.close()






