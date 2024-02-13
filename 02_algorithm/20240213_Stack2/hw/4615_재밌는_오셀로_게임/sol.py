import sys

sys.stdin = open('input.txt')

BLACK = 1
WHITE = 2

def is_reversi(stones, N, x, y, color):
    if x < 0 or x >= N or y < 0 or y >= N or stones[x][y] == 0:
        return False
    elif stones[x][y] != color:
        return True



T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())

    stones = [[0] * N for _ in range(N)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    stack = []

    for i in range(M):
        x, y, color = map(int, input().split())
        stones[x-1][y-1] = color
        stack.append((x, y))

        while stack:
            x, y = stack.pop()

            for dx, dy in directions:
                temp_x = x-1 + dx
                temp_y = y-1 + dy
                if is_reversi(stones, N, temp_x, temp_y, color):
                    stack.append((temp_x, temp_y))

            if stack:
                pass

            # if not is_reversi(stones, N, x, y):
            #     while stack:
            #         reversi_x, reversi_y = stack.pop()
            
        
            # if is_reversi(stones, N, temp_x, temp_y):
            #     stack.append((temp_x, temp_y))
            #     reversi_x, reversi_y = temp_x, temp_y
            #     while stack:
            #         for ddx, ddy in directions:
            #             reversi_x += ddx
            #             reversi_y += ddy
            #             if is_reversi(stones, N, reversi_x, reversi_x):









            # elif stones[temp_x][temp_y] != color:

            #     while stones[temp_x][temp_y] != color:
            #         stack.append((temp_x, temp_y))
            #         if stack:
            #             while stack:
            #                 reverse_x, reverse_y = stack.pop()
            #                 stones[reverse_x][reverse_y] = color

            #         stack.append((temp_x, temp_y))
            #         temp_x += dx
            #         temp_y += dy

