# -*- coding:utf-8 -*-

name =input("이름 : ")
height = float(input('키 : '))
age = int(input('나이: '))
print("--------------")
print("키는 %.1fcm, 나이는%d살" % (height,age))

# 키가 150이상
a = (height >= 150)
print(a)

# J : 연산자는 stack영역이 대상
# P : 기본형이 없 -> stack에 데이터 없  -> ?
#     알아서 적절히 돌아가게 되어있음

# 이름이 홍길동
b = (name == "홍길동")
print(b)

## and(&&), &
## or(||), |
## ^
# 키가 100 넘고, 나이가 80넘으면
c = (age >80) and (height>100)
print(c)

# 키가 100 넘든지, 나이가 80넘든지 하나만
d = (height>100) ^ (age >80)
print(d)

# 20대만(20<=age<=29)
# e = (age<30) and (age>19)
e = (20<=age<=29)
print(e)


# 나이가 20살 이상이면 어서오세요, 아니면 나가
# f = (age >=20) ? "어서오세요" : "나가"
# print(f)

print(10<<2)









