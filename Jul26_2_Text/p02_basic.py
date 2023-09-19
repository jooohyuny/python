# -*- coding:utf-8 -*-

# 무슨단어가 몇번나오나
f = open("C:/yun/sam10.txt","r",encoding="utf-8")
wordCountDict ={}
for line in f.readlines():
    line = line.replace("\n","")
    for word in line.split(" "):
        if word in wordCountDict:
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1
f.close()

for k,v in wordCountDict.items():
    print(k,v)

# import pandas as pd
# wordCountDF = pd.DataFrame(wordCountDict)
# print(wordCountDF)