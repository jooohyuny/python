# -*- coding:utf-8 -*-

# Java : 전세계적으로 많이 쓰이는
#        작업한거 공유하는 문화 -> maven
#        클래스명이 중복 될거고
#    package : 클래스명 중복될때 구분
#            패키지명이 중복되면 방법이 없으니
#            com.회사명.프로그램명.주제
#    import : 패키지명 생략하고 싶을때 쓰는 옵션사항
# 오리지널 버전 : 
#     패키지명.클래스명 변수명 = new 패키지명.클래스명();
#     java.lang.String s = new java.lang.String("ㅋ");
#     java.util.Random r = new java.util.Random();

# 편하게 쓰고 우리가 직접사용한 버전 : 먼저 import시키고 클래스명을 쓴다
#    import java.util.Random;
#    Random r = new Random();
####################################
# P : 전세계적으로 많이 쓰이는
#     작업한거 공유하는 문화(심지어 소스공개)
#     클래스명이 중복 될거고
#    package : 클래스명 중복될때 구분
#            패키지명이 중복되면 방법이 없지만
#            그래도 자유
#    import : 다른 모듈에 있는거 쓰려면 해야하는 필수사항

#import animal.pet #import 패키지명.모듈명
#d = animal.pet.dog("후추",3)
#d.showInfo()

# import animal.pet as ap  # import 패키지명.모듈명 as 별칭
# d = ap.dog("후추", 3)     # 별칭.클래스명 ...
# d.showInfo()

from animal.pet import dog  # from 패키지명.모듈명 import 가져올거
from animal.pet import cat
d = dog("후추", 3)  # 클래스명...
d.showInfo()

# class cat:
#     pass

c = cat()   # 클래스명 /함수명 중복되면 가까이 있는거
c.showInfo()

# from animal.pet import dog as apd
# d = apd("후추",3)
# d.showInfo()








