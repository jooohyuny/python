# -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()
huc.close()

dustData = loads(resBody)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
print(df)

# sns.histplot(data=df, x="PM10", palette="summer")
# sns.pairplot(data=df, palette="summer") # hist + scatter
# sns.violinplot(data=df, x="PM10", palette="summer")
sns.violinplot(data=df, x="MSRRGN_NM", y="PM10", palette="summer")
plt.show()
