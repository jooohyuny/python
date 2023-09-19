# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/kwon/LNPS.csv",names=["어디","뭐","가격","종류","위치"])
print(df) ; print("----")

#평균가
print(df["가격"].mean())
print("----")

#종류별 평균가
print(df.groupby("종류")["가격"].mean())
print("-----")

#구 별 최고가 ->종류별 최고가
print(df.groupby(["위치","종류"])["가격"].max())
print("----")

#OracleDB에 있는 기상청데이터
#날씨별 평균기온

# con=connect("newkwon/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
# sql = "select * from kma_weather"
# df2=pd.read_sql(sql,con)
# 
# #pandas로
# print(df2.groupby("KW_WFKOR")["KW_TEMP"].mean())
# 
# #SQL로
# sql="select kw_wfkor, avg(kw_temp) from kma_weather"
# sql+=" group by kw_wfkor"
# df2=pd.read_sql(sql,con)
# print(df2)
# 
# con.close()