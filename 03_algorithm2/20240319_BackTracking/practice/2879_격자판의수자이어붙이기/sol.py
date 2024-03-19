import sys
sys.stdin = open('input.txt')

def make_move(x, y, i, move):
    # 모든 방향으로 델타탐색을 6번 수행하는 함수

    # 6번 이동해서 문자열의 길이가 7이 됐다면
    if i == 7:
        # set에 삽입 (중복이면 들어가지 않음)
        moves.add(move)
        return
    
    # 아직 6번 이동하지 않았다면 델타탐색을 통해 이동
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 4 and 0 <= ny < 4:
            make_move(nx, ny, i+1, move + board[nx][ny])



T = int(input())

for testcase in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]

    # 중복을 지우기 위해 set 사용
    moves = set()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 모든 보드 판을 순회하면서 작업 수행
    for i in range(4):
        for j in range(4):
            make_move(i, j, 1, board[i][j])
            


    print(f'#{testcase} {len(moves)}')