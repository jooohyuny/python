# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

# 지하철
df = pd.read_csv("C:/yun/subway.csv", names=["년","월","일","노선","역","타고","내리고"])
df["이용객수"] = df["타고"] + df["내리고"]

def getYoil(d):
    date = "%d%02d%02d" % (d["년"],d["월"],d["일"])
    date = datetime.strptime(date, "%Y%m%d")
    return datetime.strftime(date, "%a")

df["요일"] = df.apply(getYoil,axis=1)
print(df)

# 노선별 이용객수 분포
# sns.violinplot(data=df, x="노선", y="이용객수", palette="Spectral")
# 요일별 이용객수 분포
sns.violinplot(data=df, x="요일", y="이용객수", palette="Spectral")
plt.show()