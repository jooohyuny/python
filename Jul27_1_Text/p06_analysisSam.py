# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from hanspell.spell_checker import check
from konlpy.tag._okt import Okt
from wordcloud.wordcloud import WordCloud

fontFile ="C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 12).get_name()
plt.rc("font",family=fontName)

f = open("C:/yun/samResult.txt", "r", encoding="utf-8")
o = Okt()
wc={}
words = ""
for l in f.readlines():
    l = l.split("\t")[0].replace("\"","")
    l = check(l).checked # 맞춤법교정
    l = o.normalize(l) # 정규화
    for w, p in o.pos(l, stem=True):
        if p == "Verb":
            if w in wc:
                wc[w] +=1
            else:
                wc[w] = 1
            words += w + " "
wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf",
               background_color="white").generate(words)
plt.imshow(wc)            
plt.show
f.close()

f2 = open("C:/yun/samResult2.txt","a",encoding="utf-8")
for k, v in wc.items():
    f2.write("%s,%d\n" % (k,v))
f2.close()
# wcList = []
# for k, v in wc.items():
#     wcList.append({"단어":k,"횟수":v})
# wcDF = pd.DataFrame(wcList)
# wcDF = wcDF.sort_values(by="횟수")
# print(wcDF)
# 
# sns.barplot(data=wcDF,x="단어",y="횟수", palette="pastel")
# plt.show()






