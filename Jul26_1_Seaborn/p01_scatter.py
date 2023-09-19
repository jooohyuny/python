# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from owm_weather"
df = pd.read_sql(sql, con)
con.close()
print(df)

sns.scatterplot(x="OW_TEMP", y="OW_HUMI", data=df, hue="OW_DESC", size="OW_HUMI", palette="magma")
plt.show()