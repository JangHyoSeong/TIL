import sys
sys.stdin = open('input.txt')

T = 10
for testcase in range(1, T+1):
    tc = int(input())

    numbers = list(map(int, input().split()))
    
    i = 1
    index = 0

    while True:
        numbers[index % 8] -= i

        if numbers[index % 8] <= 0:
            numbers[index % 8] = 0
            break
        i += 1
        index += 1
        if i == 6:
            i = 1
    index %= 8
    password = numbers[index+1:] + numbers[:index+1]

    print(f'#{tc} {" ".join(map(str, password))}')