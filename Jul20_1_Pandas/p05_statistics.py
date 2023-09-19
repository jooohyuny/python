# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/yun/lnpsData.csv", names=["어디","뭐","가격","종류","구"])
print(df)
print("---------")
print(df["가격"].max())
print(df["가격"].min())
print(df[df["가격"] == df["가격"].min()])
print("---------")
print(df["가격"].mean())
print(df["가격"].median())
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var())
print(df["가격"].std())
print("---------")
print(df["가격"].mode())
print(df["어디"].mode()[0])
print("---------")

