di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni and 0 <= nj < N:
                print((ni, nj), end = ' ')
                # somefunction(arr[ni][nj]) # 이런 식으로 사용될것
        print()
