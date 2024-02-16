import sys
from collections import deque
sys.stdin = open('input.txt')


# 너비 우선 탐색을 진행하는 함수
# 노드의 깊이가 얼마인지 return
def bfs(s, N, G):   # s: 시작 정점, N : 노드 개수

    # bfs를 위한 queue 선언
    q = deque()
    
    # 어느 지점을 지났는지 가중치를 저장할 배열
    # 배열에 저장되는 것은 노드의 깊이가 될 것
    visited = [0] * (N+1)

    # 시작점을 queue에 push
    q.append(s)

    # 시작점의 가중치를 1로 둠
    visited[s] = 1

    # q가 빌 때까지 bfs 탐색
    while q:
        # queue에서 pop
        t = q.popleft()

        # 현재 위치가 도착점이라면
        if t==G:
            # 현재 위치의 가중치를 return(깊이)
            return visited[t]-1 # 최단 경로 간선 수
        
        # 현재 위치에서 갈 수 있는 노드들을 탐색
        for i in adjl[t]:
            # 한번도 방문한적 없는 노드라면
            if visited[i]==0:
                # queue에 push 후, 가중치를 1더해서 저장함(깊이가 1 증가)
                q.append(i)
                visited[i] = 1 + visited[t]

    # 모든 탐색을 마쳤지만 도착지에 도착하지 못했다면 0리턴
    return 0



T = int(input())

for testcase in range(1, T+1):
    V, E = map(int, input().split())

    # 노드의 출발, 도착 정보를 저장할 리스트
    adjl = [[] for _ in range(V+1)]

    # 출발과 도착 정보를 리스트에 저장
    for i in range(E):
        n1, n2 = map(int, input().split())
        # n1 에서 갈수 있는 모든 노드를 리스트의 형식으로 
        # adjl의 n1번째 인덱스에 삽입
        adjl[n1].append(n2)

        # 방향성이 없기 때문에 반대의 경우도 성립
        adjl[n2].append(n1)
    S, G = map(int, input().split())

    result = bfs(S, V, G)

    print(f'#{testcase} {result}')