import sys
sys.stdin = open('input.txt')


for testcase in range(1, 11):
    size = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(size)]

    deadlock = 0

    for x in range(size):
        for y in range(size):
            magnetic[y][x]