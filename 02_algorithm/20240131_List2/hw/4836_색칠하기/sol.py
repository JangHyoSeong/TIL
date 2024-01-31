import sys
sys.stdin = open('input.txt')

T = int(input())

# 색깔 상수 정의
RED = 1
BLUE = 2
VIOLET = 3

for testcase in range(1, T+1):

    N = int(input())
    
    # 색깔을 칠할 2차원 리스트 정의. 0으로 초기화
    canvas = [[0] * 10 for _ in range(10)]

    
    for i in range(N):
        start_x, start_y, end_x, end_y, color = map(int, input().split())

        # 시작지점의 x좌표, y좌표, 끝지점의 x, y좌표에 정해진 색을 칠함
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):

                # 색이 아무것도 칠해져있지 않다면 입력받은 색을 칠함
                if canvas[x][y] == 0:
                    canvas[x][y] = color

                # 빨강이 칠해져 있고, 현재 칠할 색이 파랑이면 보라로 바꿈
                elif canvas[x][y] == RED and color == BLUE:
                    canvas[x][y] = VIOLET

                # 파랑이 칠해져 있고, 현재 색이 빨강이면 보라로 바꿈
                elif canvas[x][y] == BLUE and color == RED:
                    canvas[x][y] = VIOLET

    # 2차원 리스트를 전부 순회하며 보라색 영역을 확인함
    violet_area = 0
    for i in range(10):
        for j in range(10):
            if canvas[i][j] == VIOLET:
                violet_area += 1
                
    print(f'#{testcase} {violet_area}')