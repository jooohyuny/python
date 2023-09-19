# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/kwon/titanic.csv")
print(df) ; print("----")
print(df.columns) ; print("----")

#좌석 크래스별 요금 평균
print(df.groupby("Pclass")["Fare"].mean())

#좌석 클래스별 죽은사람수/산 사람수
print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())
print("----")

#성별 별로 죽은 사람 수/산 사람 수
print(df.groupby(["Sex", "Survived"])["PassengerId"].count())
print("----")

# 객실명이 뭐뭐있나(중복제거)
print(df["Cabin"].unique())
print("----")

# 객실이 몇 개 있었나
print(df["Cabin"].nunique())
print("----")

# 객실별로 몇명씩
print(df["Cabin"].value_counts())
print("----")

# con=connect("newkwon/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
# sql = "select * from kma_weather"
# df2=pd.read_sql(sql,con)
# con.close()
# 
# #어떤 날씨들이 있었나
# print(df2["kw_wfkor"].unique())
# print(df2["kw_wfkor"].nunique())
# print("----")
# 
# #각 날씨별 횟수 몇번
# print(df2["kw_wfkor"].value_counts())