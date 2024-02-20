import sys
sys.stdin = open('input.txt')


for testcase in range(1, 11):
    size = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(size)]

    deadlock = 0

    for x in range(size):

        flag = False
        for y in range(size):

            if flag == True and magnetic[y][x] == 2:
                deadlock += 1
                flag = False

            elif magnetic[y][x] == 1:
                flag = True
        

    print(f'#{testcase} {deadlock}')