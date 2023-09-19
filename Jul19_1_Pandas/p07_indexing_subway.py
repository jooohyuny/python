# -*- coding:utf-8 -*-
import pandas as pd

subwayDF = pd.read_csv("C:/yun/subway.csv",names=["년","월","일","노선","역","승차인원","하차인원"])
print(subwayDF)
print('----------')
print(subwayDF.tail(3)) # 마지막 3개
print('----------')
print(subwayDF.head(5)[["년","월","일"]]) # 첫 5개 날짜
print('----------')
print(subwayDF.iloc[10:16]) # 10 ~ 15번 데이터
print('----------')
print(subwayDF.iloc[20][["노선","역"]]) # 20번 데이터 노선, 역이름
print('----------')
subwayDF = subwayDF.set_index(subwayDF["노선"])# 노선번호로 찾을수있게 세팅
print('----------')
print(subwayDF.loc[" 2호선"]) # 2호선만 조회
print('----------')

print(subwayDF.loc[" 3호선"][["역","승차인원","하차인원"]])# 3호선 역명 타고 내리고
print(subwayDF.loc[" 3호선",["역","승차인원","하차인원"]])# 3호선 역명 타고 내리고
print('----------')

# 탄 사람수가 5만 넘는거
print(subwayDF[subwayDF["승차인원"]>50000])
print('----------')

# 내린 사람수가 100명 안되는거 년,월,일,노선,역
print(subwayDF[subwayDF["하차인원"]<100][["년","월","일","노선","역"]])
print('----------')

# 서울역 데이터 조회
# 역으로 인덱스를 바꿔서 찾던지
# subwayDF = subwayDF.set_index(subwayDF["역"])
# print(subwayDF.loc["서울역"])
# 그대로 두고 검색하는 느낌으로 하던지
print(subwayDF[subwayDF["역"]=="서울역"])
print('----------')
# 역 이름에 '서울'이 들어가는거
#                                startswith
#                                endswith
#                                contains
print(subwayDF[subwayDF["역"].str.contains("서울")])
print('----------')
# 역 이름에 '입구' 들어가는거 노선,역명
print(subwayDF[subwayDF["역"].str.contains("입구")][["노선","역"]])
print('----------')

print(subwayDF.shape[0])

# for문으로 하나하나 다 나오게
for i in range(subwayDF.shape[0]):
    print(subwayDF.iloc[i])
    print("----------")



