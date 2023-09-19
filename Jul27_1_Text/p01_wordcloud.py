# -*- coding: utf-8 -*-
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#pip install wordcloud==1.8.0


#matplotlib에 글자 한글
fonFile="C:/Windows/Fonts/H2SA1M.TTF"
fonName = fm.FontProperties(fname=fonFile, size=13).get_name()
plt.rc("font",family=fonName)

f = open("C:/yun/sam10.txt","r",encoding="utf-8")

txt= f.read()

wc= WordCloud(font_path="C:/Windows/Fonts/H2SA1M.TTF", background_color="white").generate(txt) # 워드클라우드 이미지 만들기
plt.imshow(wc)  # 그리기
plt.show()

