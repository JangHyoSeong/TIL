import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    num = int(input())
    triplet = 0
    run = 0

    counts = [0] * 12       # 뒤의 조건을 단순하게 만들기위해 더미로 두 칸을 더 추가함
    for i in range(6):
        counts[num % 10] += 1
        num //= 10

    i = 0
    while i<10:
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1
            continue
        if counts[i] >=1 and counts[i+1] >= 1 and counts[i+2] >=1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue
        i += 1

    if run + triplet == 2:
        print(f'#{testcase} true')
    else:
        print(f'#{testcase} false')