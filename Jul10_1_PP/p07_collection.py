# -*- coding:utf-8 -*-

# [], List, Set, Map
s = "가나다라 마바사"
print(s[0])
print(s[-1])
print(s[0:5:2])
print("------------")

a = [23,885,4141,2,941,8854,2121,8486,1688,763,25,255,2188]
print(type(a))
print(a)
print(a[0])
print(a[0:5]) # 0 ~ (5-1)까지
print(a[0:6:2]) # 0 ~ (6-1)까지 2칸씩
print(a[-1]) # 뒤에서 1번
print("------------")

a.append(999)
a.insert(1, 88888)
a[0] = 777
del a[2]
print(len(a))

#a.sort()
a.sort(reverse= True)

print(a)
print("------------")
b = {1,2,3,1,2,3,4,5,45}
print(b)
print(type(b))

print("------------")
c = [123,123,123,123,1,2,3,6,7,8]
c = set(c)
c = list(c)
c.sort()
print(c)
print("------------")

d = {"탄수화물":50, "단백질":30}
print(d)
print(type(d))
print(d['단백질'])
print(list(d.keys()))
print("지방" in d) # 키가 있나
print("단백질" in d)

# Java의 List,Map
# Python의 List, dict

# Python의 List : [1, 2, 3] : JavaScript의 배열
# Python의 dict : {키:값, 키:값} : JavaScript의 객체
# Python의 List,dict : JSON과 같다










