import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    x = N**(1/3)

    if abs(x - round(x)) < 0.000000001:
        print(f'#{testcase} {round(x)}')

    else:
        print(f'#{testcase} {-1}')