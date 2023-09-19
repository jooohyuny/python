# -*- coding:utf-8 -*-

# J
#   통일된 시스템
#   무슨 입/출력 장치든간에(파일, Socket, HttpRes, ...)
#   InputStream -> InputStreamReader -> BufferReader
#   OutputStream
#   어디다 입/출력을 하든지 소스가 다 똑같았다 
#   하지만 소스가 길다
# P
#   다 다름

# open(경로, 모드
#                                 r    #read ->find
#                                 w
#                                 a    #append -> write
ff = open("C:/yun/Note/0712.txt","a", encoding="utf-8")
ff.write("ㅋㅋㅋㅋ\n")
ff.write("ㅎㅎㅎㅎㅎ\n")
ff.write("090909\n")    # \n만 써도 
ff.close()