# -*- coding:utf-8 -*-
import pandas as pd

a = pd.DataFrame()
a["이름"] = ["아아","뜨아"]
a["가격"] = [4000,3500]
print(a)
print('----------')

# pd.Series
b = pd.Series(["라떼",5000], index=["이름","가격"])
a = a.append(b, ignore_index=True)  # 기존 0,1,2체제 무시
print(a)
print('----------')

# dict추가
c = {"이름" : "에스프레소", "가격" : 3000}
a = a.append(c, ignore_index=True) # 기존 dict의 체제 무시
print(a)



