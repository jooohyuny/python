# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/samResult.txt", sep="\t", names=["누구","몇번"])
df = df.sort_values(by="몇번",ascending=False)
print(df)

name = df["누구"]
count = df["몇번"]

# 비율
c = ["red","green","blue"]
e = [0,0,0.2]
w = {"edgecolor": "black", "linewidth" : 3, "width":0.7}
plt.pie(count, labels=name, autopct="%.1f%%",
        colors=c, explode=e, startangle=45, wedfeprops=w)
plt.title("삼국지")
plt.show()

# 절대적인 크기 비교
# plt.bar(name,count)
# plt.show()










