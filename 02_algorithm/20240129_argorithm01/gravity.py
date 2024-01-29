'''
9
7 4 2 0 0 6 0 7 0
'''

N = int(input())
boxes = list(map(int, input().split()))

max_drop = 0    # 가장 큰 낙차
for i in range(N):  # for i : 0 -> N - 1
    cnt = 0
    for j in range(i+1, N):  # for j : i+1 -> N-1
        if boxes[i] > boxes[j]:  # 오른쪽 박스의 개수가 더 적다면
            cnt += 1    # cnt ++
    if max_drop < cnt:  # 현재 낙차가 최대값보다 크다면
        max_drop = cnt  # 최대값을 갱신

print(max_drop)     # 출력 형식에 맞게 출력
