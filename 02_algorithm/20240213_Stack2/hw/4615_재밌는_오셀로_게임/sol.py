import sys

sys.stdin = open('input.txt')


# 델타탐색으로 이동했을 때, 돌의 색깔을 판별하기 위한 함수
def is_reversi(stones, N, x, y, color):

    # 범위를 벗어나거나, 0인 경우 0을 리턴
    # 예를들어 이동하는 방향으로 계속 이동하던 경우, 결국 범위를 벗어나거나 빈 공간을 만난다면
    # 돌을 뒤집지 말아야하기에 스택을 초기화
    if x < 0 or x >= N or y < 0 or y >= N or stones[x][y] == 0:
        return 0
    
    # 델타 탐색으로 이동하다가 다른 색깔 돌을 만난다면
    # == 이동하던 방향으로 계속 이동
    elif stones[x][y] != color:
        return 1
    
    # 계속 이동하던 와중 같은색깔 돌을 만나는 경우
    elif stones[x][y] == color:
        return 2
    

T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())

    stones = [[0] * N for _ in range(N)]
    stones[N//2-1][N//2-1] = 2
    stones[N//2-1][N//2] = 1
    stones[N//2][N//2-1] = 1
    stones[N//2][N//2] = 2

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    # 입력 받기
    for i in range(M):
        x, y, color = map(int, input().split())
        
        # x, y가 1부터 시작하기 때문에 -1을 해줌
        stones[x-1][y-1] = color


        # 모든 방향으로 탐색을 시작
        for dx, dy in directions:
            
            temp_x = x - 1 + dx
            temp_y = y - 1 + dy

            # 돌을 뒤집기 위한 stack 선언
            temp_stack = []

            # 이동한 방향이 다른색깔 돌이라면
            while is_reversi(stones, N, temp_x, temp_y, color) == 1:

                # 스택에 push한 후, 같은 방향으로 계속 이동
                # 빈 공간을 만나거나, 같은 색깔 돌을 만날 때까지 계속 진행
                temp_stack.append((temp_x, temp_y))
                temp_x += dx
                temp_y += dy

            # 같은 색깔 돌을 만난다면, 기존에 있던 다른 색깔 돌을 모두 뒤집어야 함
            if is_reversi(stones, N, temp_x, temp_y, color) == 2:
                # 스택에 들어있는 위치의 돌을 모두 뒤집음
                for reversi_x, reversi_y in temp_stack:
                    stones[reversi_x][reversi_y] = color

    black = 0
    white = 0

    # 게임보드를 모두 탐색하여 각 돌의 개수를 계산
    for i in range(N):
        for j in range(N):
            if stones[i][j] == 1:
                black += 1
            elif stones[i][j] == 2:
                white += 1

    print(f'#{testcase} {black} {white}')
