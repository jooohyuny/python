# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

# 지하철 내고타고...
df = pd.read_csv("C:/yun/cspf.csv",
                 names=["언제", "노선","역","내고탐","내고내림","그냥탐","그냥내림"])
df["그냥합"] = df["그냥탐"]+ df["그냥내림"]
print(df)

# 내고탐, 그냥탐 관계
# sns.scatterplot(data=df, x="내고탐", y="그냥탐")
# 내고탐, 그냥탐 관계 노선별 다른색
# sns.scatterplot(data=df, x="내고탐", y="그냥탐", hue="노선", palette="Accent")
# 내고탐, 내고내림 관계 (그냥타 + 그냥내려)로 크기
sns.scatterplot(data=df, x="내고탐", y="내고내림", size="그냥합", palette="Accent")

plt.show()