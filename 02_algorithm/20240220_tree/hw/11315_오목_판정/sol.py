import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    # 오목판 입력받음
    stones = [list(input()) for _ in range(N)]

    # default를 NO로 두고 시작
    result = 'NO'
    # 반복문을 벗어나기 위한 flag
    flag = False

    for i in range(0, N):
        # col 탐색
        if flag == True:
            break

        for j in range(0, N):
            # row 탐색
            if flag == True:
                break

            # 탐색 도중 돌이 놓인 곳을 발견한다면
            if stones[i][j] == 'o':

                # 오른쪽으로 순회하면서 돌이 있는지 확인
                for k in range(1,5):
                    # 범위를 벗어난다면 break
                    if j+k == N:
                        break
                    # 돌이 없다면 break
                    if stones[i][j+k] !='o':
                        break
                # 돌이 5개 있어서 break하지 않았다면
                else:
                    # 결과를 YES로 바꿈
                    result = 'YES'
                    flag = True

                # 세로의 경우 똑같은 작업 진행
                for k in range(5):
                    if i+k == N:
                        break
                    if stones[i+k][j] != 'o':
                        break
                else:
                    result = 'YES'
                    flag = True

                # 대각선(오른쪽아래)
                for k in range(5):
                    if i+k == N or j+k == N:
                        break
                    if stones[i+k][j+k] != 'o':
                        break
                else:
                    result = 'YES'
                    flag = True

                # 대각선(왼쪽아래)
                for k in range(5):
                    if i+k == N or j-k == -1:
                        break
                    if stones[i+k][j-k] != 'o':
                        break
                else:
                    result = 'YES'
                    flag = True


    print(f'#{testcase} {result}')