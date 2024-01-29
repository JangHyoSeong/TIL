T = 10

for testcase in range(T+1):
    width = int(input())
    buildings = list(map(int, input().split()))

    height_sum = 0

    for height in range(1, width -2):
        for i in range(height-2, height+3):
            pass