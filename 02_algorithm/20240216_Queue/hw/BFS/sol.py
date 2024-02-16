import sys
from collections import deque
sys.stdin = open('input.txt')

N, v = map(int, input().split())
graph = list(map(int, input().split()))

visited = [False] * (N + 1)
q = deque()

q.append(1)
visited[1] = True

while q:
    now = q.popleft()
    print(now)
    for i in range(0, 2*v, 2):
        if now == graph[i] and not visited[graph[i+1]]:
            q.append(graph[i+1])
            visited[graph[i+1]] = True