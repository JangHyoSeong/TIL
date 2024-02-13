import sys

sys.stdin = open('input.txt')

BLACK = 1
WHITE = 2

def is_reversi(stones, N, x, y, color):
    if x < 0 or x >= N or y < 0 or y >= N or stones[x][y] != 0:
        return False

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        temp_x, temp_y = x + dx, y + dy
        while 0 <= temp_x < N and 0 <= temp_y < N and stones[temp_x][temp_y] != 0:
            if stones[temp_x][temp_y] == color:
                return True
            temp_x += dx
            temp_y += dy

    return False

T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())

    stones = [[0] * N for _ in range(N)]

    for i in range(M):
        x, y, color = map(int, input().split())
        stones[x - 1][y - 1] = color

        # 돌을 놓은 위치 주변에 있는 상대방 돌을 뒤집기
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                temp_x, temp_y = x - 1 + dx, y - 1 + dy
                if is_reversi(stones, N, temp_x, temp_y, color):
                    while stones[temp_x][temp_y] != color:
                        stones[temp_x][temp_y] = color
                        temp_x += dx
                        temp_y += dy
