import sys
sys.stdin = open('input.txt')

for i in range(10):
    case_num = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    col, row = ladder[-1].index(2), 99
 
    while row != 0:
        if ladder[row][col - 1] == 1:
            while ladder[row][col - 1] == 1:
                col -= 1
            row -= 1
        elif ladder[row][col + 1] == 1:
            while ladder[row][col + 1] == 1:
                col += 1
            row -= 1
        else:
            row -= 1
 
    print(f'#{case_num} {col-1}')