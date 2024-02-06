import sys
sys.stdin = open('input.txt')

T = 10
for testcase in range(1, T+1):
    str_length = int(input())

    # 입력받기
    str_map = [list(map(str,input())) for _ in range(8)]

    count = 0
    # 가로회문탐색
    for i in range(8):
        # 회문의 길이만큼 range 조정
        for j in range(0, 9 - str_length):
            for k in range(str_length//2):
                if str_map[i][j + k] != str_map[i][j + str_length - k - 1]:
                    break
            else:
                count += 1

    
    # 세로 회문 탐색
    for j in range(8):
        for i in range(0, 9 - str_length):
            for k in range(str_length//2):
                if str_map[i+k][j] != str_map[i + str_length - k - 1][j]:
                    break
            else:
                count += 1

    print(f'#{testcase} {count}')