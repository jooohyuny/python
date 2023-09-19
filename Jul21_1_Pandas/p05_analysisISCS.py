# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/yun/iscs.csv", names=["이름","업종","주소","항목","가격"])
print(df)
print("------")
# 0원인거 삭제하고
df = df[df["가격"]>0]
# 업종별 평균가 -> 업종으로 나누고 개별 평균가
print(df.groupby("업종")["가격"].mean())
print("------")

# 항목별 평균가
print(df.groupby("항목")["가격"].mean())
print("------")
df["주소"] = df["주소"].fillna("ㅋ 모름")
# df["구"] = df["주소"].apply(lambda a : a.split(" ")[1])

def getGu(a):
    a = a.split(" ")
    if a[0].endswith("구"):
        return a[0]
    return a[1]

df["구"] = df["주소"].apply(getGu)

# 구별 평균가
print(df.groupby("구")["가격"].mean())
print("------")
# 구별 -> 업종별 평균가
print(df.groupby(["구","업종"])["가격"].mean())
