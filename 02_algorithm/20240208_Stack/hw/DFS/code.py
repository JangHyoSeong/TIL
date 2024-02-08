import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = [start] # 다음 조사대상
    visited = []
    while stack:    # 조사 대상이 없어질때까지
        now = stack.pop()
        print(now, end=' ')
        # 다음번 조사대상 (인접 리스트adj[now] 모두 조사)
        for next in adjl[now]:
            if visited[next] ==0:
                stack.append(next)



V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)] # adjl[i] 행 i에 인접인 정점번호
for i in range(E):
    n1, n2 = i*2, i*2 + 1
    adjl[n1].append(n2)
    adjl[n2].append(n1) 