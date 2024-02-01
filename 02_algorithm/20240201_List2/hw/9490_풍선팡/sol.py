import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M = map(int, input().split())

    max_pollen = 0

    pollen = [list(map(int, input().split())) for _ in range(N)]

    for col in range(N):
        for row in range(M):
            splash = pollen[col][row]
            temp_pollen = 0

            for i in range(-splash, splash+1):
                if 0 <= col + i < N:
                    temp_pollen += pollen[col + i][row]

                if 0 <= row + i < M:
                    temp_pollen += pollen[col][row + i]

            temp_pollen -= splash
            if max_pollen < temp_pollen:
                max_pollen = temp_pollen

    print(f'#{testcase} {max_pollen}')