import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop
INF = 21e8

def dijkstra(start, target):
    # 다익스트라 연산

    pq = []

    # 최단거리를 저장할 리스트
    distance = [INF] * (N+1)

    # 시작 지점을 우선순위큐에 넣고 시작
    heappush(pq, (0, start))
    # 시작 위치까지의 최단거리는 0
    distance[start] = 0

    while pq:

        dist, now = heappop(pq)

        # 이미 최단거리가 아니라면 넘어감
        if distance[now] < dist:
            continue

        # 현재 집에서 갈수있는 집을 모두 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 새 누적거리 구함
            new_dist = dist + next_dist

            # 새로 구한 누적 거리가 최단거리라면, 우선순위큐에 넣고 갱신
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    
    return distance[target]


T = int(input())

for testcase in range(1, T+1):
    N, M, target = map(int, input().split())
    
    # 인접 리스트
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])

    # 모든 집에 대해서 연산
    max_dist = 0
    for i in range(1, N+1):
        # 갔다 오는 거리까지이니 다익스트라 2번 구함
        temp_dist = dijkstra(i, target) + dijkstra(target, i)
        max_dist = max(max_dist, temp_dist)

    
    print(f'#{testcase} {max_dist}')