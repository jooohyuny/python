# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/bus2015Result.txt", sep="\t", names=["요일","합계"])
print(df)

df1 = df[df["요일"].str.contains("데이터수")]
df1["요일"] = df1["요일"].apply(lambda y : y.replace("_데이터수",""))

df2 = df[df["요일"].str.contains("합")]
df2["요일"] = df2["요일"].apply(lambda y : y.replace("_합",""))

yoil = df1["요일"]
cnts = df1["합계"]
sums = list(df2["합계"])
# avgs = sums/cnts
print(yoil)
avgs = []
for i,v in enumerate(cnts):
    avgs.append(sums[i]/v)
print(avgs)

plt.bar(yoil,avgs)
plt.show()
# print(sums)
# print(cnts)
# print(df1)
# print(df2)



