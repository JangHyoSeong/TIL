import sys

sys.stdin = open('input.txt')

# 현재 이동상태를 나타내기 위한 상수 정의
left = 1
right = 0
down = -1

# 도착점을 만나면 return으로 즉시 종료하기 위해서 함수로 정의
# 불필요한 연산을 줄임

def ladderGame(ladder):

    # 시작점을 0부터 100까지 전부 시도
    for j in range(100):
        # 시작점 x좌표를 저장
        start_point = j

        # y좌표를 0으로 초기화
        i = 0

        # 이동 상태를 초기화
        # 이동 상태가 필요한 이유
        # 1 0 0 0 1
        # 1 1 1 1 1
        # 이런 경우에 왼쪽 1에서 시작하고 오른쪽으로 간 경우,
        # 오른쪽으로 이동했다는 정보를 갖고있지 않으면 다시 왼쪽으로 이동할 수 있음
        # -> 무한루프에 빠지거나 원하는 실행 결과가 나오지 않음

        moving_now = down

        # 시작 지점이 1이라면 동작 시행, 0이라면 x좌표를 하나 증가
        if ladder[i][j] == 1:

            # y좌표가 99가 되기 전까지 계속 반복
            while i<99:

                # IndexError를 피하기 위해 j==0, j==99인 경우를 따로 생각
                # j==0인 경우(x좌표가 0) 오른쪽으로만 움직일 수 있음
                # 따라서 오른쪽인 경우만 확인
                if j == 0 and moving_now != left:

                    # 한 칸 옆이 1이라면(길이라면) 이동
                    if ladder[i][j+1] == 1:
                        j += 1
                        moving_now = right
                        
                        
                # 마찬가지로 j=99인 경우 왼쪽으로만 이동가능하기에 왼쪽으로 가는 경우만 검사
                elif j == 99 and moving_now != right:
                    if ladder[i][j-1] == 1:
                        j -= 1
                        moving_now = left
                        
                        
                # 나머지의 경우 왼쪽 오른쪽을 모두 검사하여 이동
                elif j > 0 and j < 99:
                    if ladder[i][j+1] == 1 and moving_now != left:
                        j += 1
                        moving_now = right
                        
                    elif ladder[i][j-1] == 1 and moving_now != right:
                        j -= 1
                        moving_now = left
                        

                # 아래 칸이 2라면 함수를 종료
                if ladder[i+1][j] == 2:
                    print(f'#{testcase} {start_point}')
                    return None
                
                # 왼쪽, 오른쪽으로 이동하고 나서 아래에 길이 있다면 이동
                # 이동 상태를 down으로 설정
                if ladder[i+1][j] == 1:
                    i += 1
                    moving_now = down        

for testcase in range(1, 11):
    t = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    ladderGame(ladder)