# 0007. 2차원 리스트의 전체 합
'''
입력 예시
3 
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
21 22 23 24 25 26 27 28 29 30
'''

import sys

# txt파일의 각 줄의 내용을 input함수가 실행될때마다 넣어준다.

N = int(input())
result = []

for i in range(N):
    arr = list(map(int, input().split()))
    result.append(arr)



