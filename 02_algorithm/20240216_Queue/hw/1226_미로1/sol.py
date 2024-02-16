import sys
from collections import deque
sys.stdin = open('input.txt')

def isValid(maze, x, y):
    size = len(maze)
    return x < size and x >= 0 and y < size and y >=0 and maze[x][y] != 1


for testcase in range(1, 11):
    tc = int(input())
    size = 16
    maze = [list(map(int, input()))for _ in range(size)]

    for i in range(size):
        if 2 in maze[i]:
            start_x = i
            start_y = maze[i].index(2)
            break
    
    queue = deque()
    visited = [[0] * size for _ in range(size)]
    result = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1
    
    while queue:
        now_x, now_y = queue.popleft()

        if maze[now_x][now_y] == 3:
            result = 1
            break
        
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            if isValid(maze, new_x, new_y) and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))

    print(f'#{testcase} {result}')