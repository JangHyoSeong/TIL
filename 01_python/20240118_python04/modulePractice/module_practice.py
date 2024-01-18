import random
import my_math

lotto = random.sample(range(1, 46),6)
print(sorted(lotto))

a = my_math.add(3, 5)
print(a)

# 모듈 적는 순서(대충 국룰)

# 1st : core
import os, sys

# 2nd : built-in
import math

# 3rd : third party library
import requests
# from django.db.models import Model

'''
써드파티 라이브러리 다운받을 때 꼭 해야하는 것
1. 공식 문서 보기
2. 릴리즈 히스토리 확인하기
'''

'''
프로젝트 시작할때 requirements.txt 파일을 만들고
프로젝트에서 사용하는 라이브러리의 버전을 모두 기록해야함
pip freeze > requirements.txt 
--> 컴퓨터에 설치되어있는 모든 패키지가 표시됨
'''
