# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# Python list
a = pd.DataFrame()  # 빈 DataFrame
a["이름"] = ["홍길동", "김짱구","권짱구"]  # 변수명["필드명"] = Python list
a["나이"] = [18,20,26]
print(a)
print('--------------')

# np.array
b = pd.DataFrame()
b["이름"] = np.array(["홍길동", "김짱구","권짱구"])  # 변수명["필드명"] = np.array()
b["나이"] = np.array([18,20,26])
print(b)
print('--------------')

# 2차원 list/np.array
# c = [["홍길동",18],["김짱구",20],["권짱구",26]]
c = np.array([["홍길동",18],["김짱구",20],["권짱구",26]])
c = pd.DataFrame(c, columns = ["이름","나이"])
print(c)
print('--------------')

# dict + list
d = {"이름" : ["홍","이"],
     "나이" : [10,20]}
d = pd.DataFrame(d)
print(d)
print('--------------')

# list + dict
# 자주 쓸거같은 느낌....
e = [{"이름" : "홍", "나이" : 10},
     {"이름" : "이", "나이" : 20}]
e = pd.DataFrame(e)
print(e)
print('--------------')









