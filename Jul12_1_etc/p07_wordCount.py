# -*- coding:utf-8 -*-

# Python이 구려 - x
# 하드웨어쪽 한계가 올텐데...
# 1TB짜리 데이터를 RAM이 어떻게 감당을...
# 전처리(1TB짜리 데이터를 서버급 컴 여러대로 병렬처리)
# -> 필요없는 데이터는 제외 -> 50MB
# -> Hadoop(Linux에서만 돌아가는, Java프로그램)

# 채팅내용부분만 무슨단어가 제일 많이 나온건가?
f = open("C:/yun/Note/KakaoTalkChats.txt","r", encoding="utf-8")
txt = None
wc = {}
for i,line in enumerate(f.readlines()):
    if i > 3:
        line = line.replace("\n","")
        if line.startswith("2023년"):
            try:
                txt = line.split(" : ")[1]
            except:
                pass
        else:
            txt = line
        if txt != None and txt != "":
            for word in txt.split(" "):
                if word in wc:
                    wc[word] += 1
                else:
                    wc[word] = 1
f2 = open("C:/yun/Note/wcResult.txt","a", encoding="utf-8")
for k, v in wc.items():
    f2.write("%s\t%d\n" % (k,v))
f2.close()

f.close()









