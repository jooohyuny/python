# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)


# oracledb에 있는 owm날씨 불러다가
# 기온, 습도 꺾은선 그래프
# 날짜를 "23일 10시" 형태로 
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from owm_weather"
df = pd.read_sql(sql,con)
con.close()

df = df.sort_values(by="OW_DATE")
df["OW_DATE"] = df["OW_DATE"].apply(lambda d : "%d일 %d시" % (d.day,d.hour))
print(df)

# Pandas DF -> Numpy Array
date = df["OW_DATE"]
temp = df["OW_TEMP"]
humi = df["OW_HUMI"]
print(temp)

_, cf1 = plt.subplots()
p1 = cf1.plot(date,temp,"r-")
cf1.set_xlabel("날짜")
cf1.set_ylabel("기온")

cf2 = cf1.twinx()
p2 = cf2.plot(date,humi,"b-")
cf1.set_ylabel("습도")
cf1.legend(p1 + p2, ["기온", "습도"])
plt.title("날씨")
plt.show()

