import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

INF = 21e8

def dijkstra(start):
    # 다익스트라 함수

    # 우선순위 큐
    pq = []
    # 시작 값을 넣어줌, 시작위치의 누적거리 초기화
    heappush(pq, (0, start))
    distance[0] = 0

    # 갈 수 있는 모든 노드의 최소거리 계산
    while pq:
        # 현재까지 누적거리, 현재 위치
        dist, now = heappop(pq)

        # 지금 이동에서 이미 최소누적거리를 초과했다면 고려하지 않음
        if distance[now] < dist:
            continue

        # 현재 위치에서 갈 수 있는 모든 간선을 조사
        for to in graph[now]:
            # 다음 노드로 이동할 때 이동거리
            next_dist = to[0]
            # 다음 노드 번호
            next_node = to[1]

            # 다음 노드로 이동할 때 누적 이동거리
            new_dist = next_dist + dist

            # 만약 이번 분기에서의 누적 이동거리가 기존의 최소값보다 크다면 고려하지 않음
            if new_dist > distance[next_node]:
                continue

            # 이번 분기가 최소값이라면 갱신
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


T = int(input())

for testcase in range(1, T+1):
    V, E = map(int, input().split())

    # 인접 리스트
    # 예를 들어 graph[0]은 0번 노드에서 갈 수 있는 노드들과 그 거리에 대한 값을 가짐
    graph = [[] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([w, e])

    # 누적 최소 이동 거리를 저장할 리스트
    distance = [INF] * (V+1)
    dijkstra(0)

    print(f'#{testcase} {distance[V]}')