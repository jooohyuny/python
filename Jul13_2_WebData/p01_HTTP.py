# -*- coding:utf-8 -*-
from http.client import HTTPSConnection

# https://www.crazy11.co.kr/shop/shopbrand.html?xcode=243&type=Y&gf_ref=Yz11QUxnOUU=
# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500

# http or https
# huc = HTTPConnection("주소:포트")
# 연결
huc = HTTPSConnection("www.kma.go.kr")
# 요청
huc.request("GET","/wid/queryDFSRSS.jsp?zone=1111061500")   #폴더,파일,파라메터
# 응답받아와서
res = huc.getresponse()
# 응답내용
resBody = res.read()
# 응답내용 한글처리해서
print(resBody.decode())