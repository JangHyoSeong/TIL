import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    lazer = list(input())
    str_len = len(lazer)
    steel = 0
    count = 0

    for i in range(str_len-1):
        if lazer[i] == '(' and lazer[i+1] == '(':
            count += 1
            steel += 1
        elif lazer[i] == '(' and lazer[i+1] == ')':
            steel += count
        elif lazer[i] == ')' and lazer[i+1] == ')':
            count -= 1
    print(f'#{testcase} {steel}')