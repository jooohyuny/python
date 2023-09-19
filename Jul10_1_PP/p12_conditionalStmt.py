# -*- coding:utf-8 -*-

score = int(input("시험점수 : "))

#if(score >80){
#    잘했다
#}else if(score > 60){
#    그래
#} else{
#    노력해
#}

if score>80:
    print("good")
elif score>60:
    print("soso")
elif score>50:
    print("so....")
else:
    print("hey")

# 3항연산, switch-case문
# if문으로 해도 됨, 소스가 길어져서 문제지 -> 파이썬은 관심이 없음
# if문으로 하면 불가능한가 -x, 길어질뿐
# switch(직책){
#    case "DBA":
#        백업
#        전원관리
#    case "DBP":
#        CRUD
#    case "DBU":
#        잘쓰기
# }

