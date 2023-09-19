# -*- coding:utf-8 -*-

# NumPy(np.array) : 
#        기능 좋은 list [][]
#        의미 알아보기가 좀 그렇다...
#        후속기술들 선수과목
# score[0][1]
# score[0,1]

# Pandas(pd.dataframe) : Python Data Analysis Library
#        MS Excel의 표같은
#        R에도

# 설치 : cmd에서 pip install pandas
import pandas as pd

# list같은거
a = pd.Series([123,45,88])
print(a)
print(a[0])
print('---------')

# 엑셀 표 같은거
b = pd.DataFrame()
b["이름"] = ["새우깡","양파링","포카칩"]
b["가격"] = [4000,5000,6000]
print(b)
print('---------')
print(b["이름"])  # 특정 필드 조회
print('---------')
print(b.iloc[1]) # 1번 데이터 조회
print('---------')
# 기본적으로는 번호로 찾게 되어 있는데
print(b.loc[2])

# 찾는 기준을 이름으로
b = b.set_index(b["이름"])
print(b)
print('---------')
print(b.loc["새우깡"])

# 번호로 찾을때는 iloc, 기준으로 찾을때는 loc












