# -*- coding:utf-8 -*-
from _datetime import datetime

# bus2015.csv
# 탄 사람 < 내린 사람 인 요일 
# 20150101 -> 월

rideDict={"Sunday":0,"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}
alightDict={"Sunday":0,"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}
f = open("C:/yun/bus2015.csv","r", encoding="utf-8")
for line in f.readlines():
    line = line.replace(" ","")
    if line.startswith("2015,03"):
        break
    line = line.replace("\n","").split(",")
#     print(line)
    date = datetime.strptime(line[0] + line[1] + line[2],"%Y%m%d")
    yoil = datetime.strftime(date,"%A")
#     print(yoil)
    rideDict[yoil] += int(line[-2])
    alightDict[yoil] += int(line[-1])

yoils, rides, alights = [], [], []
for k,v in rideDict.items():
    # print(k,v)
    yoils.append(k)
    rides.append(v)
    alights.append(alightDict[k])
    
f.close()
###########################################
import numpy as np
yoils = np.array(yoils)
rides = np.array(rides)
alights = np.array(alights)
print(yoils[rides < alights])
print(yoils)
print(rides)
print(alights)










