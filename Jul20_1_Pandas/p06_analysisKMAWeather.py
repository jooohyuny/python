# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

# OracleDB에 있는 기상청 날씨정보를 df로
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from kma_weather"
df = pd.read_sql(sql, con)
print(df)
print('---------')
# 최고기온
print(df["KW_TEMP"].max())
print('---------')
# 평균기온
print(df["KW_TEMP"].mean())
print('---------')
# 최고기온 언제, 몇시
print(df[df["KW_TEMP"] == df["KW_TEMP"].max()][["KW_DATE","KW_HOUR"]])
print('---------')
# 평균기온보다 낮은거 언제, 몇시, 날씨
print(df[df["KW_TEMP"] < df["KW_TEMP"].mean()][["KW_DATE","KW_HOUR","KW_WFKOR"]])
print('---------')
print("===========")

# 최고기온
sql = "select max(kw_temp) from kma_weather"
df = pd.read_sql(sql,con)
print(df)
print('---------')
# 평균기온
sql = "select avg(kw_temp) from kma_weather"
df = pd.read_sql(sql,con)
print(df)
print('---------')
# 최고기온 언제, 몇시
sql = "select kw_date, kw_hour "
sql += "from kma_weather "
sql += "where kw_temp = ("
sql += "    select max(kw_temp) from kma_weather"
sql += ")"
df = pd.read_sql(sql,con)
print(df)
print('---------')
# 평균기온보다 낮은거 언제, 몇시, 날씨
sql = "select kw_date, kw_hour, kw_wfkor "
sql += "from kma_weather "
sql += "where kw_temp < ("
sql += "    select avg(kw_temp) from kma_weather"
sql += ")"
df = pd.read_sql(sql,con)
print(df)
print('---------')




con.close()
