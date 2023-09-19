# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/cspf.csv", names=["월", "노선","역","내고탐","내고내림","그냥탐","그냥내림"])
df2 = df.groupby("노선")[["내고탐","그냥탐","내고내림","그냥내림"]].mean()

no = df2.index  # 1호선, 2호선, ...
no2 = np.arange(len(no))    # 0,1,2, ...
prn = df2["내고탐"]
pan = df2["내고내림"]
frn = df2["그냥탐"]
fan = df2["그냥내림"]

f = (frn + fan) / 2
f = (f / f.max()) * 1000

# 돈내고 많이 타면, 돈내고 많이 내림
# 근데 그거랑 무임시리즈랑은 무관
plt.scatter(prn, pan, s=f, color="green", alpha=0.5)
plt.title("지하철")
plt.show()










