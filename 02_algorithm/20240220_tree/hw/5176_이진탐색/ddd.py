import sys
import math
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    height = math.ceil(math.log(N+1, 2)-1)

    max_leaf = 2**height-1

    if N > max_leaf:
        root = 2**(height-2) + 1
    else:
        root = 2**height

    print(root)