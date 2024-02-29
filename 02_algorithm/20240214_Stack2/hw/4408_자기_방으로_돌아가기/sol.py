import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N = int(input())
    move = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        # 숫자가 작은 방에서 큰 방으로 이동하게끔 설정
        if move[i][0] > move[i][1]:
            move[i][0], move[i][1] = move[i][1], move[i][0]
        # 짝수방을 모두 홀수방으로 옮김
        if move[i][0]%2==0:
            move[i][0] -= 1
        if move[i][1]%2==0:
            move[i][1] -= 1

    # 복도 리스트. 학생이 지나갈때마다 1이 증가. 최대값이 되는 부분의 값이 걸리는 시간
    corridor = [0] * 402

    for i in range(N):
        for j in range(move[i][0], move[i][1]+1):
            corridor[j] += 1

    print(f'#{testcase} {max(corridor)}')