import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 2**31 - 1
    battery = []
    stack = []
    
    for i in range(1, N):
        stack.append[(0, i)]
        visited = [False] * N

        while stack:
            (x, y) = stack.pop()
            
            for j in range(1, N):
                if not visited[j]:
                    battery[i] += arr[x][y]
                    visited[y] = True



    print(f'#{testcase} {min_sum}')