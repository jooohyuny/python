# -*- coding:utf-8 -*-
import pandas as pd

df1 = pd.read_csv("C:/yun/titanic.csv")
df2 = pd.read_csv("C:/yun/titanic.csv")
print(df1)
print(df2)
print("-------")
df3 = pd.concat([df1,df2])  # df1뒤에 df2추가
print(df3)
print("-------")
df4 = pd.concat([df1,df2],axis=1)   # df1옆에 df2추가
print(df4)
print("-------")
#join
snackDF = pd.DataFrame()
snackDF["이름"] = ["초코파이","새우깡"]
snackDF["가격"] = [5000,4000]
snackDF["제조사"] = ["오리온","농심"]

company = {"제조사" : ["오리온","농심","롯데"],
           "위치" : ["서울", "수원", "인천"]}
companyDF = pd.DataFrame(company)

city = [{"이름" : "서울","인구" : 100},
        {"이름" : "수원","인구" : 50},
        {"이름" : "인천","인구" : 30}]
cityDF = pd.DataFrame(city)
print(snackDF)
print("---------------")
print(companyDF)
print("---------------")
print(cityDF)
print("---------------")

# inner join
# 양쪽 다 제조사 필드가 있어서, 그 기준으로 자동으로 붙임
# df5 = pd.merge(snackDF,companyDF)
# print(df5)

# 만약에 양쪽 다 있는 필드가 여러개면?
df5 = pd.merge(snackDF,companyDF, on="제조사")
print(df5)

# outer join
df6 = pd.merge(snackDF,companyDF, on="제조사", how="outer")
print(df6)

# 필드명 다르면
df7 = pd.merge(companyDF,cityDF, left_on="위치", right_on="이름")
print(df7)

# 인구수가 가장 많은 도시에서 만들어진 과자 평균가
# subquery : 쓰면 데이터 수가 줄고 - v
# join : 쓰면 데이터 수가 폭증 - x
# 1) 형태를 알수가 없고
# 2) 효율성 따질거면 Python을 안했어야
# -> df 셋 다 붙여서
df8 = pd.merge(snackDF,companyDF)
df8 = pd.merge(df8,cityDF,left_on="위치",right_on="이름")
print(df8)
print(df8[df8["인구"] == df8["인구"].max()]["가격"].mean())














