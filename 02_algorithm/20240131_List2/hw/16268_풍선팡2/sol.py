import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M = map(int, input().split())

    # IndexError가 생기지 않게 앞뒤로 더미데이터 삽입
    pollen = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    pollen.insert(0, [0] * (M + 2))
    pollen.extend([0] * (M + 1))

    max_pollen = 0

    # 2차원 리스트를 순회하며 최대값을 구함
    # 2차원 배열의 테두리는 더미데이터이므로 범위를 (1,M) (1,N)으로 잡음
    for i in range(1, N):
        for j in range(1, M):
            temp_pollen = pollen[i][j] + pollen[i-1][j] + pollen[i+1][j] + pollen[i][j+1] + pollen[i][j-1]
            if max_pollen < temp_pollen:
                max_pollen = temp_pollen

    print(f'#{testcase} {max_pollen}')