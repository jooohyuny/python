# -*- coding:utf-8 -*-

# subway.csv 불러서 ride와 alight의 값을 비워둔 dict에 채워넣고
# 같은 이름의 역에 자료를 

# name = 서울역, 시청역, ...
# rideSum = 30만, 20만, ...
# alightSum = 15만, 30만, ...

# 2015 ~ 2022 다 더해서
f = open("C:/yun/subway.csv","r", encoding="utf-8")
rideDict = {}
alightDict = {}
for line in f.readlines():
    line = line.replace("\n","").split(",")
    # "서울역이라는 키가 rideDict에 있나?
    if line[4] in rideDict:
        rideDict[line[4]] += int(line[5])
        alightDict[line[4]] += int(line[6]) # alight["서울역"] += ???
    else:
        rideDict[line[4]] = int(line[5])    # rideDict["서울역"] = 47000
        alightDict[line[4]] = int(line[6])    
name = []
ride = []
alight = []
for k, v in rideDict.items():   # (키, 값) tuple형태로 리턴
    name.append(k)
    ride.append(v)
    alight.append(alightDict[k])
f.close()
# print(name)
# print(ride)
# print(alight)
###########################################
import numpy as np
 
s_name = np.array(name)
rideSum = np.array(ride)
alightSum = np.array(alight)
print(s_name[rideSum < alightSum])    # 탄사람<내린사람이 많은 역 이름 찾기













