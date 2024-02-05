import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    input_str = input()
    input_len = len(input_str)

    for i in range(input_len//2):
        if input_str[i] != input_str[input_len - i - 1]:
            print(f'#{testcase} 0')
            break

    else:
        print(f'#{testcase} 1')