# -*- coding:utf-8 -*-
# pip install --upgrade pip setuptools wheel
# pip install opencv-python==3.4.0.12
import cv2

a = cv2.imread("C:/yun/test.png", cv2.IMREAD_GRAYSCALE)
print(a)
# 이미지/사운드/영상 : 컴에는 10101로 저장
#     그 데이터를 인코딩만 할 줄 알면 된다

# ML/DL
# 내일 기온 예측 -> 숫자
# 내일 날씨 예측 -> 글자
#            -> 이미지
#            -> 사운드
