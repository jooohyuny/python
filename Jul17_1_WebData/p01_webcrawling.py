# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# HTML파싱
#        Python : BeautifulSoup.py
#        Java : JSoup.jar
# cmd
#     pip install bs4
#############################################
# BigData분석용/AI훈련용 데이터 구축
# 1) 직접 발로 뛰는 방법(아침에 학원올때마다 노약자석 체크...?)
# 2) 완성된 csv파일 같은거 구하거나
# 3) 웹 데이터 활용
#       XML파싱
#       JSON파싱
#       XML/JSON이 없다면? 
#        -> 웹 크롤링(웹사이트에서 가져오는거)
#        -> HTML파싱
#############################################
# XML/JSON : 데이터를 표현하기 위한 형식
# HTML  : 웹사이트를 디자인하기 위한 언어
#    파싱이 불편할것
#    법적문제
#    보안상 사용불가
#############################################
# https://sdgn-djvemfu.tplinkdns.com/sns.get?page=1
huc = HTTPSConnection("sdgn-djvemfu.tplinkdns.com")
huc.request("GET","/")
resBody = huc.getresponse().read()
#############################################
# XML : fromstring()     -> getiterator() / find()
# JSON : loads()         -> list/dict
# HTMl : BeautifulSoup() -> find() 



#                            내용,    내장html파서, from_encoding=""
cafeSNSData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
# ???.select("css선택자")
snsTxts = cafeSNSData.select(".aSNSTxt2")
for st in snsTxts:
    print(st.text) # ???.text
    print("-----------")


huc.close()





