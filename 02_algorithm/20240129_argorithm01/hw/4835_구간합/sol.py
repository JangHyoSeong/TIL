import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, (input().split()))
    numbers = list(map(int, input().split()))

    max = 0
    min = 2 ** 31 - 1

    for i in range(N - M + 1):
        arr_sum = 0

        for j in range(M):
            arr_sum += numbers[i + j]

        if max < arr_sum:
            max = arr_sum
        if min > arr_sum:
            min = arr_sum




    print(f'#{testcase} {max - min}')