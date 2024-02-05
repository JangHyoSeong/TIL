import sys
sys.stdin = open('input.txt')

T = int(input())
for testcase in range(1, T+1):

    N, str_length = map(int,input().split())
    # 입력받기
    str_map = [list(map(str,input())) for _ in range(N)]

    for i in range(N):
        # 회문의 길이만큼 range 조정
        for j in range(0, N + 1 - str_length):
            for k in range(str_length//2):
                if str_map[i][j + k] != str_map[i][j + str_length - k - 1]:
                    break
            else:
                print(f'#{testcase} {"".join(str_map[i][j+_] for _ in range(str_length))}')

    
    # 세로 회문 탐색
    for j in range(N):
        for i in range(0, N + 1 - str_length):
            for k in range(str_length//2):
                if str_map[i+k][j] != str_map[i + str_length - k - 1][j]:
                    break
            else:
                print(f'#{testcase} {"".join(str_map[i+_][j] for _ in range(str_length))}')