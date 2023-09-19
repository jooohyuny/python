# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

yData=[10,30,5,32,2]
xData=["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"]

# 기본
# plt.bar(xData,yData)
# plt.show()

# 디자인
# plt.bar(xData,yData,color="red",width=0.5,edgecolor="orange", linewidth="3")
# cs = ["red","orange","yellow","green","blue"]
# plt.bar(xData,yData,color=cs,width=0.5,edgecolor="orange", linewidth="3")
# plt.show()

# 여러개(옆에)
# yData2=[12,33,57,3,23]
# xData2 = np.arange(len(yData2))
# xData3 = xData2 - 0.4   # -0.4 0.6 ...
# plt.bar(xData,yData, align="edge")

# -0.4 0.6 ...
# plt.bar(xData3,yData, width=0.4, align="edge")
# 0 1 ...
# plt.bar(xData,yData2, width=0.4, align="edge",color="green")
# plt.show()

# 여러개(위에 - 누적합)
yData2=[12,33,57,3,23]
plt.bar(xData,yData, color="red")
plt.bar(xData,yData2, color="blue",bottom=yData)
plt.show()




