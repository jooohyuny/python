# -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

#지하철 csv불러서
df = pd.read_csv("C:/yun/subway.csv", names=["년","월","일","노선","역","탄","내린"])
df["이용객수"] = df["탄"] + df["내린"]

def getYoil(s):
    date = "%d%02d%02d" % (s["년"],s["월"],s["일"])
    date = datetime.strptime(date, "%Y%m%d")
    return datetime.strftime(date, "%a")

df["요일"] = df.apply(getYoil,axis=1)
print(df)

# 노선별 이용객수 평균
# sns.barplot(x="노선",y="이용객수", data= df)

# 노선별 데이터 수
# sns.barplot(x="노선", data= df)

# 노선별 이용객수 평균(요일별로 따로)
sns.barplot(x="노선", y="이용객수",hue="요일", data=df)

plt.show()






