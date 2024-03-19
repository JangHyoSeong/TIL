import sys
sys.stdin = open('input.txt')

def findMax(i, N, probability):
    global max_probability

    # 모든 일을 배분했을때
    if i == N:
        # 최대 확률 갱신이 가능하다면 갱신
        if max_probability < probability:
            max_probability = probability
        return
    
    # 이미 최대확률보다 작아졌다면 종료
    if probability <= max_probability:
        return

    # 순열을 생성하면서 반복
    for j in range(i, N):
        P[i], P[j] = P[j], P[i]
        findMax(i+1, N, probability * arr[i][P[i]]/100)
        P[i], P[j] = P[j], P[i]

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_probability = 0
    P = list(range(N))
    findMax(0, N, 100)

    print(f'#{testcase} {max_probability:.6f}')