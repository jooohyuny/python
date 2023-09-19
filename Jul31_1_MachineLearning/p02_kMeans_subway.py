# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.cluster._kmeans import KMeans
from sklearn.neighbors._classification import KNeighborsClassifier

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/subway.csv", names=["년","월","일","노선","역","타","내려"])

# 역별 타/내린 평균 구해서
df = df.groupby("역")[["타","내려"]].mean()
print(df)

# 비슷한 역끼리 그룹
trainData = df.to_numpy()
km = KMeans(10)
df["그룹"] = km.fit_predict(trainData)
print(df)

sns.scatterplot(x="타",y="내려",hue="그룹",
                data=df,palette="pastel")
plt.show()
# 역명 -> 그룹 역 출력
name = input("역명 : ")
# print(df.loc[name])
# print(df.loc[name]["그룹"])
print(df[df["그룹"] == df.loc[name]["그룹"]])