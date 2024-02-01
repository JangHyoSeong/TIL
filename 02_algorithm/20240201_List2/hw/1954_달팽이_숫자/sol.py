import sys
sys.stdin = open('input.txt')

# 상수 정의
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# 델타서칭을 위한 배열
dfs_1 = [-1, 0, 1, 0]
dfs_2 = [0, 1, 0, -1]


# 이동 방향으로 이동해도 되는지 판별하는 함수
def isOK(snail, col, row, size, moving):

    # 앞으로 이동할 방향을 미리 확인
    next_col = col + dfs_1[moving]
    next_row = row + dfs_2[moving]

    # 배열의 범위에서 벗어난다면 False
    if next_col < 0 or next_col >= size:
        return False
    if next_row < 0 or next_row >= size:
        return False
    
    # 앞에 이미 값이 있다면 False
    if snail[next_col][next_row] != 0:
        return False
    
    # 앞의 False 조건들을 모두 빠져나오면 True
    return True


T = int(input())

for testcase in range(1, T+1):

    size = int(input())

    # 2차원 배열을 0으로 초기화
    snail = [[0] * size for _ in range(size)]


    # 초기 변수 설정
    col = 0
    row = 0
    num = 1
    moving = RIGHT

    # 배열을 모두 순회할 수 있도록 적절한 for문 범위 설정
    for i in range(size * size):
        
        # 현재 위치에 값을 할당
        snail[col][row] = num
        num += 1

        # 이동 방향으로 이동해도 되는지 판별
        if isOK(snail, col, row, size, moving):

            # 방향을 바꾸지 않아도 된다면 이동
            col += dfs_1[moving]
            row += dfs_2[moving]
            
            # 방향을 바꿔야 한다면 바꾸고 이동
        else:
            moving = (moving + 1) % 4
            col += dfs_1[moving]
            row += dfs_2[moving]

    print(f'#{testcase}')
    for i in range(size):
        for j in range(size):
            print(snail[i][j], end=' ')
        print()
