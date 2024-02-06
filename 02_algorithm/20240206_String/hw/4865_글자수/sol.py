import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    str1 = list(map(str,input()))
    str2 = input()

    new_str1 = set(str1)

    count_max = 0

    for c in new_str1:
        temp_count = 0
        for i in str2:
            if c == i:
                temp_count += 1
        if count_max < temp_count:
            count_max = temp_count

    print(f'#{testcase} {count_max}')