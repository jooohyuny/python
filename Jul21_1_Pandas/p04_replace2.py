# -*- coding:utf-8 -*-
import pandas as pd

# 타이타닉
df = pd.read_csv("C:/yun/titanic.csv")
print(df)
print("----------")
print(df.columns)
print("----------")

# 이름, 성별 필드 뺴고 다 지우고 -> 이름, 성별만 추출
df = df[["Name","Sex"]]

# male -> 남자, female -> 여자
df["Sex"] = df["Sex"].replace({"male" : "남자", "female": "여자"})

# 이름에서 Mr -> 미스터
# df["Name"] = df["Name"].replace("Mr","미스터")
def replaceMr(t):
    return t.replace("Mr.","미스터")
df["Name"] = df["Name"].apply(replaceMr)
print(df)
print("----------")

# 이름에서 성떼고 이름만 남기기
# def removeFamilyname(n):
#     return n.split(",")[0]
# df["Name"] = df["Name"].apply(removeFamilyname)
df["Name"] = df["Name"].apply(lambda n:n.split(",")[0])
print(df)
print("----------")

df = pd.read_csv("C:/yun/titanic.csv")
print(df[df["Age"].isnull()])
df["Age"] = df["Age"].fillna(900)
df["대"] = df["Age"].apply(lambda a:"%d0대" % (a//10))
df["대"] = df["대"].replace("900대","모름")
print(df)
print("----------")

# 나이대별로 산사람/죽은사람 수 
print(df.groupby(["대","Survived"])["PassengerId"].count())
print("----------")







