# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads
from cx_Oracle import connect

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()
huc.close()

dustData = loads(resBody)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
print(df)

# sns.barplot(data=df)    # pd.DataFrame넣으면 알아서 그리기는 함
# 통계가 필요하면 알아서(권역별 PM10평균)
# 검은선 : 신뢰구간 95%
# sns.barplot(x="MSRRGN_NM", y="PM10", data=df, palette="Pastel1")

# 검은선 : 표준편차   
# sns.barplot(ci="sd", x="MSRRGN_NM", y="PM10", data=df, palette="summer")   

# 갯수(권역별 데이터 몇개씩)
# sns.countplot(x="MSRRGN_NM", data=df, palette="autumn")   

# 권역별 대이터 몇개씩, 상태별로 색깔다르게
# sns.countplot(x="MSRRGN_NM", hue="IDEX_NM", data=df, palette="autumn")   
# plt.show()
print("---------------")

# OracleDB에 있는 기상청 날씨
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from kma_weather order by kw_date, kw_hour"
df2 = pd.read_sql(sql,con)
con.close()
print(df2)

sns.barplot(x="KW_HOUR", y="KW_TEMP", hue="KW_WFKOR", data= df2, palette="rocket")
# sns.barplot(x="KW_WFKOR", y="KW_TEMP", data= df2, palette="rocket")
print(df2)

# 시간대별 데이터  몇개씩
# sns.countplot(x="KW_HOUR",hue="KW_WFKOR",data=df2, palette="Accent")
plt.show()