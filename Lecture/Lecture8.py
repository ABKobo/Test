# Lucture 8
L1 = [1, 2, 3, [4, 5]]
L2 = L1[:] # 바깥 리스트만 복사 안쪽 id 같음
L1[3][0]= -4
print(L1)  # [1, 2, 3, [-4, 5]
print(L2)  # [1, 2, 3, [-4, 5]


import copy # 복사관련 파일 가져옴
L1 = [1, 2, 3, [4, 5]] # 전부 복사 id 전부 다름 
L2 = copy.deepcopy(L1)
L1[3][0]= -4
print(L1)  # [1, 2, 3, [-4, 5]
print(L2)  # [1, 2, 3, [4, 5]

import math as m # 간추리기 가능
print(m.pi) 
print(m.sqrt(100))

from math import pi, sqrt # 특정 함수만 불러옴
print(pi) # 앞에 math. 필요 없음
print(sqrt(100))

from math import * # 전부 불러옴 (비추천)
print(pi) 
print(sqrt(100))


import sys
print(sys.builtin_module_names) # import 가능한 목록
print(sys.path) # import 가능한 경로


import Lecture8_another as my # 다른 파일 불러오기 _이외 다른 특수문자 불가
result = my.plus(10, 20) # 30
print(result)
print(my.s) # 'Hello'
print(my.__name__) # 파일 이름 print week6_2another
print(__name__) # __main__


import random # 랜덤
num = random.random()
print(num)  # random float number, 0.0 <= num < 1.0

num = random.randint(1, 10)
print(num)  # random integer number, 1 <= num <= 10

L = (1, 2, 3, 4, 5)
num = random.sample(L, 2)
print(num)  # random 2 numbers from L 리스트로 출력


import time # 시간
print(time.ctime()) # 현재 시간
time.sleep(5)  # 5초 정지
print(time.ctime())  


