# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

# 서울시 실시간 미세먼지 -> pd.DataFrame

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()
print(resBody.decode())

dustData = loads(resBody)   # JSON -> Python dict + list
dustDF = pd.DataFrame(dustData["RealtimeCityAir"]["row"])
print(dustDF)

huc.close()

