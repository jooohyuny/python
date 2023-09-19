# -*- coding:utf-8 -*-

# 기상청날씨.csv로 만들어와서
# 시간대별 평균기온

f = open("C:/yun/kmaWeather.csv", "r", encoding="utf-8")
weatherSumDict = {"12":0, "15":0, "18":0, "21":0, "24":0}
weatherCntDict = {"12":0, "15":0, "18":0, "21":0, "24":0}
weatherDict = {}
for l in f.readline():
    l = l.replace("\n", "")
    print(l)
    weatherSumDict[l[3]] += float(l[4])
    weatherCntDict[l[3]] += 1
    
hour = []
temp = []
for k,v in weatherSumDict.items():
    hour.append(k)
    temp.append(v / weatherCntDict[k])
f.close()
###########
import numpy as np
hour = np.array(hour)
temp = np.array(temp)
print(hour)
print(temp)
# 제일 추운거 몇 시
print(hour[np.argmin(temp)], temp[np.argmin(temp)])
# 제일 더운거 몇 시
# print(hour[np.argmax(temp)], temp[np.argmax(temp)])
# print(np.max(temp))
# print(temp == np.max(temp))
print(hour[temp == np.max(temp)])
print(temp[temp == np.max(temp)])
# 총 평균기온
tempAvg = np.mean(temp)
print(tempAvg)
# 총 평균기온보다 더운거 몇시
hour2 = hour[temp > tempAvg]
temp2 = temp[temp > tempAvg]
for i in range(hour2.size):
    print(hour2[i],temp2[i])


