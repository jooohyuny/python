# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

f = open("C:/yun/iscs.csv","a",encoding= "utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for i in range(1,7457,1000):
    huc.request("GET","/575a4655496b636839386f58586542/json/IndividualServiceChargeService/%d/%d/" % (i,i+999))
    rb = huc.getresponse().read()
    for i in loads(rb)["IndividualServiceChargeService"]["row"]:
        f.write("%s," % i["BSSH_NM"].replace(",",""))
        f.write("%s," % i["INDUTY_DESC"].replace(",",""))
        f.write("%s," % i["ADRES_CN2"].replace(",",""))
        f.write("%s," % i["PRDLST_DESC"].replace(",",""))
        f.write("%.1f\n" % i["PC"])
print("끝")
huc.close()
f.close()    
