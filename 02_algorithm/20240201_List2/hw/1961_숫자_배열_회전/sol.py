import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    size = int(input())

    arr = [list(map(int, input().split())) for _ in range(size)]

    print(f'#{testcase}')
    for i in range(size):
        for j in range(size):
            print(arr[size-j-1][i], end='')
        print('', end=' ')

        for j in range(size):
            print(arr[size-i-1][size-j-1], end='')
        print('', end=' ')

        for j in range(size):    
            print(arr[j][size-i-1], end='')

        print()