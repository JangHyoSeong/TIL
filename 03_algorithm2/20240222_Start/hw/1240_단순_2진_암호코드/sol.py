import sys
sys.stdin = open('input.txt')

decode = {(3, 2, 1, 1) : 0,
          (2, 2, 2, 1) : 1,
          (2, 1, 2, 2) : 2,
          (1, 4, 1, 1) : 3,
          (1, 1, 3, 2) : 4,
          (1, 2, 3, 1) : 5,
          (1, 1, 1, 4) : 6,
          (1, 3, 1, 2) : 7,
          (1, 2, 1, 3) : 8,
          (3, 1, 1, 2) : 9
          }


T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    raw_data = [list(map(int, input())) for _ in range(N)]

    code = []   # 암호 해독 전 코드
    password = []   # 암호 해독 후 숫자의 배열
    break_flag = 0  # 반복문 탈출을 위한 flag
    for i in range(N):
        for j in range(M-1, -1, -1):
            if raw_data[i][j] == 1:
                code = raw_data[i][j-55:j+1]
                break_flag = 1
                break
        if break_flag == 1:
            break
    
    
    for i in range(8):
        temp = tuple()
        bit = 0
        count = 0

        for j in range(7):

            if code[i*7 + j] == bit:
                count += 1
            else:
                temp += (count, )
                bit = (bit+1) % 2
                count = 1
            if j == 6:
                temp += (count, )
        
        password.append(decode[temp])

    odd = 0
    even = 0
    for i in range(8):
        if i%2:
            even += password[i]
        else:
            odd += password[i] * 3

    if (even + odd) % 10 != 0:
        print(f'#{testcase} 0')
    else:
        print(f'#{testcase} {sum(password)}')