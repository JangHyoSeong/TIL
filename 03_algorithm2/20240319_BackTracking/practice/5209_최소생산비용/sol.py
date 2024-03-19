import sys
sys.stdin = open('input.txt')

def findCost(i, N, now_cost):
    # 최소 비용을 찾는 함수
    global min_cost

    # 순열의 모든 항목을 정했다면
    if i == N:
        # 이때 최소값이 갱신 가능하다면 갱신
        if min_cost > now_cost:
            min_cost = now_cost
        return
    
    # 이미 최소값을 넘겼다면 리턴
    if now_cost >= min_cost:
        return
    
    # 순열을 생성하고 가능한 모든 경우를 탐색
    for j in range(i, N):
        P[i], P[j] = P[j], P[i]
        findCost(i+1, N, now_cost + table[i][P[i]])
        P[i], P[j] = P[j], P[i]




T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 99 * N
    P = list(range(N))

    findCost(0, N, 0)

    print(f'#{testcase} {min_cost}')