import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(f'#{testcase} {numbers[M%N]}')