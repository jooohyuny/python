# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

# 기상청날씨
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from kma_weather"
df = pd.read_sql(sql, con)
con.close()
print(df)

# 시간별 기온을 날씨로 찾게 -> heatmap
pt = df.pivot_table(columns="KW_HOUR", values="KW_TEMP", index="KW_WFKOR")
print(pt)

sns.heatmap(data=pt, cmap="autumn")
plt.show()