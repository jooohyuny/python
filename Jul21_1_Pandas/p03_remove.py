# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

df = pd.read_csv("C:/yun/titanic.csv")
print(df)
print("----------")

# 삭제가 의미있나...
#    - 애초에 원본을 안건드는
#    - 삭제x, 나머지 추출o

print(df.columns)
print("----------")

# 필드 삭제
df = df.drop("PassengerId",axis=1)
df = df.drop(df.columns[0],axis=1)
df = df.drop(["Pclass","Name"],axis=1)
# 성별, 나이만 빼고 나머지 다 삭제 -> 그럴거면 두개만 꺼내오면 되지않나?
df = df[["Sex","Age"]]
print(df)
print("----------")

df = pd.read_csv("C:/yun/titanic.csv")
print(df)
print("----------")

# 데이터 삭제
df = df.drop(0) # 행 번호로 지우기 - x, index로 지우기
df = df.set_index(df["Pclass"]) # 객실등급으로 찾게
df = df.drop(3) # 객실등급이 3등급인거 삭제
# 성별이 남자 삭제 -> 성별이 여자 추출
# df = df.set_index(df["Sex"])
# df = df.drop("male")
df = df[df["Sex"]=="female"]
print(df)
print("----------")

# OracleDB에 오픈웨더맵
con = connect("yun/yun@195.168.9.85:1521/xe")
sql = "select * from owm_weather"
df2 = pd.read_sql(sql,con)
con.close()
print(df2)
print("----------")

# 습도필드 제거하고
df2 = df2.drop("OW_HUMI", axis=1)
# 날짜 기온 날씨 순으로 보이게 필드 정렬
df2 = df2[["OW_DATE","OW_TEMP","OW_DESC"]]
print(df2)
# 평균기온보다 낮은 데이터 제거하고
df2 = df2[df2["OW_TEMP"].mean() <= df2["OW_TEMP"]]
# 다 조회
print(df2)


