import sys
sys.stdin = open('input.txt')

def f(i, s, N): # s: i-1까지의 합
    global min_v

    if i == N:
        if min_v > s:
            min_v = s

    # 이미 최소값보다 크다면 연산 중지
    elif s >= min_v:
        return
    
    else:
        for j in range(i, N):     # P[i]자리에 올 원소 P[j]를 결정
            P[i], P[j] = P[j], P[i]
            f(i+1, s+table[i][P[i]], N)               # 다음 자리를 결정하러 이동
            P[i], P[j] = P[j], P[i] # 원상 복구


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    P = [_ for _ in range(N)]
    P = list(range(N))

    min_v = 100
    f(0, 0, N)
    print(f'#{testcase} {min_v}')
