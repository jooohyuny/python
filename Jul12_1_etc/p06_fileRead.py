# -*- coding:utf-8 -*-

ff = open("C:/yun/Note/0712.txt","r", encoding="utf-8")

# a = ff.read()   # 전체 다 읽어서, str하나로
# print(a)
# print(type(a))

# b = ff.readline() # 다음 한 줄 읽어서, str하나로
# print(b)
# b = ff.readline()
# print(b)
# print(type(b))

# 전체 다 읽어서, 엔터키 기준으로 나눠서 list
# c = ff.readlines()
# print(c)
# print(type(c))

for l in ff.readlines():
    l = l.replace("\n","")
    print(l)


ff.close()