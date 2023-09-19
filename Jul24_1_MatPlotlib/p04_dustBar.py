# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

# 서울 실시간 미세먼지
# 구별로 미세 + 초미세 막대그래프

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()
# print(resBody.decode())

huc.close()
dustData = loads(resBody)
dustDF = pd.DataFrame(dustData["RealtimeCityAir"]["row"])
# print(dustDF)
name = dustDF["MSRSTE_NM"]
pm10 = dustDF["PM10"]
pm25 = dustDF["PM25"]
print(pm10)
print(pm25)
plt.bar(name,pm10, color="red")
plt.bar(name,pm25, color="blue",bottom=pm10)
plt.title("미세먼지")
plt.show()




