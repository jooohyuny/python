# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df1 = pd.read_csv("C:/yun/shResult.txt", sep="\t", names=["노선","승차인원"])
df2 = pd.read_csv("C:/yun/sh2Result.txt", sep="\t", names=["노선","하차인원"])
df = pd.merge(df1,df2)
print(df)
no = df["노선"]
ride = df["승차인원"]
alight = df["하차인원"]

plt.bar(no,ride, color="red")
plt.bar(no,alight, color="blue", bottom=ride)
plt.show()



