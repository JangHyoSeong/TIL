import sys
sys.stdin = open('input.txt')

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def is_valid(maze, visited, x, y):
    N = len(maze)
    if x < 0 or x >= N or y < 0 or y >= N or maze[x][y] == 1 or visited[x][y] is True:
        return False
    else:
        return True
    
    # 이런식으로도 가능
    # return x >= 0 and x < N and y >= 0 and y < N and maze[x][y] != 1 and not visited[x][y]:


for testcase in range(1, 11):

    # 입력받음
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]

    # 어떤 위치를 방문했는지 기록하는 리스트. True면 방문했던 위치
    visited = [[False] * N for _ in range(N)]

    # 시작점을 찾는 과정
    start_x, start_y = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
                break
    
    # 결과를 저장할 변수
    result = 0

    # 스택에 일단 시작 위치를 push
    stack = [(start_x, start_y)]
    
    # 델타 탐색을 위한 리스트 선언
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # DFS를 사용
    # 만약 백트래킹으로 만든다면 cnt 변수를 추가하고, 일정 cnt를 넘어가면 탐색을 중지
    
    while stack:
        # 이동할 위치를 pop
        x, y = stack.pop()

        # 이동한 위치가 끝이라면 반복문 종료 후 result = 1로 설정
        if maze[x][y] == 3:
            result = 1
            break

        # 방문한 위치를 기록
        visited[x][y] = True

        # 상하좌우를 탐색하여 이동할 수 있는 위치는 스택에 삽입
        for i in range(4):
            temp_x, temp_y = x + dx[i], y + dy[i]
            if is_valid(maze, visited, temp_x, temp_y):
                stack.append((temp_x, temp_y))

        # 스택이 비었다면(이동할 수 있는 위치가 없다면) 반복문 종료
        if stack == []:
            break

    print(f'#{testcase} {result}')