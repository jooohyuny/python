# -*- coding:utf-8 -*-
f = open("C:/yun/naverNews.txt","r", encoding="utf-8")
txt = None
wcDict = {} # str -> int
for line in f.readlines():
    line = line.replace("\n","").split("\t")
    for word in line[1].split(" "):
        if word in wcDict:
            wcDict[word] += 1
        else:
            wcDict[word] = 1
# f2 = open("C:/yun/wcNewsResult.txt","a", encoding="utf-8")
for k, v in wcDict.items():
    print(k,v)
#     f2.write("%s\t%d\n" % (k,v))
# f2.close()

f.close()