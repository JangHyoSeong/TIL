import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M= map(int,input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_kill = 0
            
            for x in range(M):
                for y in range(M):
                    temp_kill += flies[i+x][j+y]

            for x in range(1, M-1):
                for y in range(1, M-1):
                    temp_kill -= flies[i+x][j+y]

            if max_kill < temp_kill:
                max_kill = temp_kill
                a = i
                b = j

    print(f'#{testcase} {max_kill}')