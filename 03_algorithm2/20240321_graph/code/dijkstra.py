'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappush, heappop

INF = 21e8 # 임의의 큰 값

V, E = map(int, input().split())

start = 0       # 시작 노드 (문제마다 다름)

# 인접 리스트
graph = [[] for _ in range(V)]

# 누적 거리를 저장할 리스트
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = [] # 우선순위 큐

    # weight, 노드 번호를 push
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0
    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # pq의 특성으로 인해 더 긴거리여도 이미 pq에 들어있음
        # -> now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 누적 거리가 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적거리를 최단거리로 갱신
            
            # next_node의 인접 노드들을 pq에 추가
            heappush(pq, (new_dist, next_node))

dijkstra(0)
print(distance)