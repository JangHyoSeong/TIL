import sys

sys.stdin = open('input.txt')


for tc in range(int(input())):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]
    ans = 0
    for i in range(N):
        count_c = 0
        count_r = 0
        for j in range(N):
            # 가로
            if puzzle[i][j] == '1':
                count_c += 1
            # 현재 칸의 숫자가 0이거나 끝까지 갔다면
            if (puzzle[i][j] == '0' or j == N-1):
                # 카운트된 수가 K라면 단어가 들어갈 수 있는 곳임 
                if count_c == K:
                    ans += 1
                count_c = 0
            # 세로
            if puzzle[j][i] == '1':
                count_r += 1
            if (puzzle[j][i] == '0' or j == N-1):
                if count_r == K:
                    ans += 1
                count_r = 0
    print(f'#{tc+1} {ans}')