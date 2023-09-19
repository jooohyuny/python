# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv("C:/yun/mosquito.csv", names=["날짜", "물가", "집", "공원"])
print(df)
print("---------")
print(df["물가"].isnull())
print("---------")
print(df[df["물가"].isnull()])
print("---------")

# None이라는 글자가 있음
print(df[df["물가"] == "None"])
print("---------")

# 123, "None" -> object
print(df["물가"].dtype)
print("---------")

# "None" -> 없
df["물가"] = df["물가"].replace("None", np.nan)
df["집"] = df["집"].replace("None", np.nan)
df["공원"] = df["공원"].replace("None", np.nan)

# 필드 형변환 object -> int | float (숫자로)
df["물가"] = pd.to_numeric(df["물가"])
df["집"] = pd.to_numeric(df["집"])
df["공원"] = pd.to_numeric(df["공원"])
# print(df["물가"].dtype)

# 지금은 필요없지만
# 필드 형변환 object -> 글자로
# df["물가"] = df["물가"].astype(str)

# 없는거는 평균치로 채워서
df["물가"] = df["물가"].fillna(df["물가"].mean())
df["집"] = df["집"].fillna(df["집"].mean())
df["공원"] = df["공원"].fillna(df["공원"].mean())
print(df)
print("---------")

# 물가/집/공원 평균치
df["평균"] = (df["물가"] + df["집"] + df["공원"])/3
print(df["평균"])
print("---------")

# 모기각 가장 심했던 날 언제?
print(df[df["평균"]==df["평균"].max()])



