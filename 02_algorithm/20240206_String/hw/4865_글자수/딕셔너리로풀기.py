import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    str1 = input()
    str2 = input()

    dict_1 = {}
    dict_2 = {}
    for i in str2:
        dict_2.setdefault(i, 0)

    for i in str2:
        dict_2[i] += 1

    temp = 0
    for i in str1:
        if temp < dict_2[i]:
            temp = dict_2[i]

    print(f'#{testcase} {temp}')