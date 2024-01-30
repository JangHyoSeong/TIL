import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # 모두 나누었다면 1이 될테니, 1이 아니라면 계속 반복
    while N != 1:

        while N % 2 == 0:
            N //= 2
            a += 1

        while N % 3 == 0:
            N //= 3
            b += 1

        while N % 5 == 0:
            N //= 5
            c += 1

        while N % 7 == 0:
            N //= 7
            d += 1

        while N % 11 == 0:
            N //= 11
            e += 1

    print(f'#{testcase} {a} {b} {c} {d} {e}')