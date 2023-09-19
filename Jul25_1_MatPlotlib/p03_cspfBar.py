# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

df = pd.read_csv("C:/yun/cspf.csv", names=["월", "노선","역","내고탐","그냥탐","내고내림","그냥내림"])
print(df)

df2 = df.groupby("노선")[["내고탐","그냥탐","내고내림","그냥내림"]].mean()
print(df2)

no = df2.index  # 1호선, 2호선, ...
no2 = np.arange(len(no))    # 0,1,2, ...
prn = df2["내고탐"]
frn = df2["그냥탐"]
pan = df2["내고내림"]
fan = df2["그냥내림"]

plt.bar(no2-0.4,prn, color = "red",width = 0.4, align="edge")
plt.bar(no2-0.4,frn, color="blue",width = 0.4, align="edge", bottom=prn)
plt.bar(no2,pan, color = "green" ,width = 0.4, align="edge")
plt.bar(no2,fan,color="yellow",width = 0.4, align="edge", bottom=pan)
plt.title("CSPF")
plt.xticks(no2, no, rotation=45)
plt.legend(["내고탐","그냥탐","내고내림","그냥내림"])
plt.show()










