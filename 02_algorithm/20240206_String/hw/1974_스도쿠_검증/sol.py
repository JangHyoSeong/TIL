import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 검증을 위한 카운트 배열, 변수 정의
    is_valid = 1
    counts_x = [0] * 9
    counts_y = [0] * 9
    counts_9 = [0] * 9

    # 델타 탐색을 위한 배열 정의
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]


    # 가로 세로를 검증
    for i in range(9):
        for j in range(9):

            # 해당하는 값을 카운트 배열로 계산
            counts_x[sudoku[i][j] - 1] += 1
            counts_y[sudoku[j][i] - 1] += 1

        # 1이 아닌 값이 있다면 is_valid를 0으로 바꿈
        for k in range(9):
            if counts_x[k] != 1:
                is_valid = 0
                break
            if counts_y[k] != 1:
                is_valid = 0
                break
        counts_x = [0] * 9
        counts_y = [0] * 9

    # 3*3 네모 검증
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            for x in dx:
                for y in dy:
                    counts_9[sudoku[i+x][j+y]-1] += 1
            for k in range(9):
                if counts_9[k] != 1:
                    is_valid = 0
            counts_9 = [0] * 9

    
    print(f'#{testcase} {is_valid}')