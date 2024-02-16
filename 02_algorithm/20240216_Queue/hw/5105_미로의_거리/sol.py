import sys
from collections import deque
sys.stdin = open('input.txt')


# 미로에서 이동 가능한지 여부를 리턴하는 함수
def isValid(maze, x, y):
    size = len(maze)

    # 미로의 크기를 벗어나면 return False, 아니라면 return True
    return x < size and x >= 0 and y < size and y >=0 and maze[x][y] != 1

T = int(input())

for testcase in range(1, T+1):
    size = int(input())
    maze = [list(map(int, input()))for _ in range(size)]

    # 시작점을 찾음
    for i in range(size):
        if 2 in maze[i]:
            start_x = i
            start_y = maze[i].index(2)
            break
    
    queue = deque()
    # 노드의 방문 여부를 확인할 2차원리스트 선언
    # 리스트에 저장할 것은 위치의 깊이(가중치)이다
    visited = [[0] * size for _ in range(size)]

    result = 0

    # 델타탐색을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 시작점을 queue에 push
    queue.append((start_x, start_y))

    # bfs 시작
    while queue:
        # queue에서 pop
        now_x, now_y = queue.popleft()

        # 도착했다면
        if maze[now_x][now_y] == 3:
            # 도착한 위치의 가중치를 저장
            # 문제의 설명에 맞추기 위해 -1
            result = visited[now_x][now_y] - 1
            break
        
        # 4방향으로 델타탐색
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # 미로를 벗어나지 않고, 방문한적 없다면 이동
            if isValid(maze, new_x, new_y) and visited[new_x][new_y] == 0:
                # 이동할 위치의 깊이를 현재위치 + 1로 설정
                visited[new_x][new_y] = visited[now_x][now_y] + 1
                # queue에 push
                queue.append((new_x, new_y))

    print(f'#{testcase} {result}')