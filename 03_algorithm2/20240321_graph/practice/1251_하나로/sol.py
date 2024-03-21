import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    # 섬의 x, y좌표를 입력받음
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))

    E = float(input())

    # 인접 행렬을 만듦
    graph = [[0] * N for _ in range(N)]

    # 존재하는 모든 섬에 대해서 간선의 가중치를 계산함
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = E * ((island_x[i]-island_x[j])**2 + (island_y[i] - island_y[j])**2)

    # visited 리스트
    visited = [False] * N
    sum_weight = 0

    # 시작점을 0이라 두고 prim알고리즘 시작
    pq = []
    heappush(pq, (0, 0))

    while pq:
        # 가중치가 가장 작은 간선부터 우선순위 queue에서 pop
        weight, node = heappop(pq)

        # 방문한 섬이라면 연산x
        if visited[node]:
            continue

        # 방문 처리
        visited[node] = True

        # 가중치 더함
        sum_weight += weight

        # 현재 섬에서 갈수있는 모든 섬을 조사
        for to in range(N):
            # 0이 아니고, 방문한 적이 없다면
            if graph[node][to] == 0 or visited[to]:
                continue
            # 우선순위 queue에 삽입
            heappush(pq, (graph[node][to], to))

    print(f'#{testcase} {sum_weight:.0f}')