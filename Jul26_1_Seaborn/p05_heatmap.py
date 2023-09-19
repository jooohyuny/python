# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

# 지하철
df = pd.read_csv("C:/yun/subway.csv", names=["년","월","일","노선","역","타고","내리고"])
df["이용객수"] = df["타고"] + df["내리고"]

# 피벗테이블(테이블을 요약해놓은 테이블)
# 월별 이용객수를 노선으로 찾게
pt = df.pivot_table(columns="월", values="이용객수", index="노선")
print(pt)

sns.heatmap(data=pt, cmap="summer")
plt.show()