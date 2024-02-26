import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    
    wire = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(1, N):
        for j in range(0, i):
            if wire[j][0] < wire[i][0] and wire[j][1] > wire[i][1]:
                count += 1
            
            elif wire[j][0] > wire[i][0] and wire[j][1] < wire[i][1]:
                count += 1

    print(f'#{testcase} {count}')