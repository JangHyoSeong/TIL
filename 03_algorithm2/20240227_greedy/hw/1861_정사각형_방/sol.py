import sys
sys.stdin = open('input.txt')


def findPosition(num):
    # num 숫자의 위치를 찾는 함수
    # 위치를 찾으면 그때 인덱스를 리턴함
    for i in range(N):
        for j in range(N):
            if rooms[i][j] == num:
                return i, j


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 델타 탐색을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 가장 많이 이동한 횟수를 저장할 변수
    max_count = 0

    # 1에서 부터 시작 (방에 들어있는 숫자)
    num = 1

    # 숫자의 끝까지 닿을때까지 반복
    while num <= N**2:

        # 현재 숫자의 위치를 찾아서 가져옴
        i, j = findPosition(num)

        # 현재 숫자(위치)에서 몇번 움직일 수 있는지 저장하는 변수
        count = 1

        # 이동할 수 없을때까지 반복할 것
        while True:
            
            # 델타탐색
            for idx in range(4):
                x = i + dx[idx]
                y = j + dy[idx]

                # 이동 가능한 곳을 찾음
                if x >= 0 and x < N and y >= 0 and y <N and rooms[x][y] - rooms[i][j] == 1:
                    # 인덱스를 바꾸어서 이동
                    i = x
                    j = y
                    count += 1
                    break
            # 4방향 모두 이동 불가능하다면 while루프 탈출
            else:
                break

        # 만약 이번의 이동이 최대값보다 크다면 갱신
        if max_count < count:
            max_count = count
            # 최대로 이동했을 때 그때 숫자를 기억해둠
            max_point = num

        # 실행 횟수를 줄이기 위해서 건너뜀
        # 예를들어 1에서부터 시작해서 1 2 3 4 5 까지 가고 멈췄다면
        # 2, 3, 4, 5는 조사하지 않아도 최대값보다 작다는 것을 알 수 있음
        # 따라서 조사가 필요없는 부분은 건너뜀
        num += count
        
        
    print(f'#{testcase} {max_point} {max_count}')