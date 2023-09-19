# -*- coding:utf-8 -*-

class WordCount:
    def __init__(self,w,c):
        self.word = w
        self.count = c
        
    def show(self):
        print(self.word,self.count)
##################################
f = open("C:/yun/Note/wcResult.txt","r", encoding="utf-8")
wcs = []
for line in f.readlines():
    line = line.replace("\n","").split("\t")
    wc = WordCount(line[0],int(line[1]))
    wcs.append(wc)
#    

# (lambda p1, p2, ... : 리턴)(값,값,...)
# Python이 알아서 객체 하나씩 리턴해주는데   
wcs.sort(key=(lambda wcwc:wcwc.count), reverse=True)    
# wcs.sort(key=(lambda wcwc:wcwc.word))    
for v in wcs:
    v.show()
f.close()
