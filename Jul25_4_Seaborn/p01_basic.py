# -*- coding:utf-8 -*-
from cx_Oracle import connect
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from owm_weather order by ow_date"
df = pd.read_sql(sql, con)
con.close()
print(df)



sns.lineplot(x="OW_DATE", y="OW_TEMP", data=df, palette="summer")
plt.title("날씨")
plt.show()
# matplotlib : np.array대상, 직접 다 설정
# Seaborn : Matplotlib을 쓰기 편하게 해주는 lib
#     pd.DataFrame대상
#     자동으로 그림
#     부족한거 Matplotlib으로
#     테마기능
    