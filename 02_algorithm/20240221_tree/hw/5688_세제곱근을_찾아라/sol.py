import sys
import math
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    for i in range(1, 10**6+1):
        if i**3 == N:
            print(f'#{testcase} {i}')
            break

    else:
        print(f'#{testcase} {-1}')