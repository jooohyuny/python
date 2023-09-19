# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/samResult2.txt", names=["단어","횟수"])
df = df.sort_values(by="횟수", ascending=False)
print(df)

sns.barplot(x="단어",y="횟수",data=df.head(20))
plt.show()


