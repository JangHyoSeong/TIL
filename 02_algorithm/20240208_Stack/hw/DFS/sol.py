import sys
sys.stdin = open('input.txt')

def dfs(i, V):
    visited = [0] * (V+1)   # visited, stack 생성 및 초기화
    stack = []
    visited[i] = 1  # 시작점 방문
    print(i)    # 정점에서 할 일
    while True: # 탐색
        for w in adjl[i]:   # 현재 방문한 정점에 인접하고 방문안한 정점
            if visited[w] == 0: # 방문한적없다면
                stack.append(i) # 방문한 정점 push
                i = w
                visited[i] = 1  # 방문했다는 표시
                print(i, end=' ')
                break
        else:
            if stack: # 스택이 비어있지 않으면
                i = stack.pop()
            else:   # 스택이 비어있다면
                break
    print()

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # adjl[i] 행 i에 인접인 정점번호

for i in range(E):
    n1, n2 = i*2, i*2 + 1
    adjl[n1].append(n2)
    adjl[n2].append(n1)     # 방향이 없는 경우

# print(adjl) # 각 정점이 몇번에 인접한지 저장