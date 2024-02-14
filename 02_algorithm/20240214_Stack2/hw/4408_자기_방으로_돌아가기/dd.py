import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N = int(input())

    move = [list(map(int, input().split())) for _ in range(N)]
    time = 1

    for i in range(N):
        move[i].sort()
    for i in range(N):
        move.sort(key= lambda x: x[0])

    for i in range(N):
        flag = False
        j = i+1

        while j < N:
            if move[i][1] > move[j][0]:
                move[i][0] = 0
                move[i][1] = 0
                flag = True
                j = move[j][0]
            j += 1

        # for j in range(i+1, N):
        #     if move[i][1] > move[j][0]:
        #         move[i][0] = 0
        #         move[i][1] = 0
        #         flag = True

        if flag == True:
            time += 1
            flag = False

    print(f'#{testcase} {time}')