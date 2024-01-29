import sys

sys.stdin = open('input.txt')

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = max(numbers)
    min_num = min(numbers)

    print(f'#{testcase} {max_num - min_num}')
