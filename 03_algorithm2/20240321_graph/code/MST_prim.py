'''
input
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop


V, E = map(int, input().split())

# 인접 행렬로 저장
# 인접 리스트로 저장하는 법도 해보자

graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split()) # 출발, 도착, 가중치
    graph[s][e] = w     # s에서 e로 가는데 w만큼 비용이 든다
    # 무방향그래프
    graph[e][s] = w


def prim(start):
    pq = []     # 우선순위 큐
    MST = [0] * V   # visited

    # 최소 비용, 가중치의 합
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 우선 순위가 가중치에 따라 정렬되어야 함 -> 가중치가 낮으면 먼저 나와야 함
    # 관리해야할 데이터 : 가중치, 노드번호
    # 1번 방법 : node를 class로 만들어 사용하기 class Node(num, weight)
    # 2번 방법 : 튜플로 관리
    heappush(pq, (0, start))
    while pq:
        weight, now = heappop(pq)

        # 방문했다면 continue
        # 왜 필요한가? -> BFS의 경우 무조건 방문하기 때문에 없어도됨
        # PRIM의 경우 일단 pq에 다 넣어두고, 가중치가 작은것부터 방문
        # 따라서 q에 똑같은 노드에 가는 길이 여러개 들어가있음
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1

        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드를 보면서 pq에 삽입
        for to in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    print(f'최소 비용 : {sum_weight}')

prim(0)