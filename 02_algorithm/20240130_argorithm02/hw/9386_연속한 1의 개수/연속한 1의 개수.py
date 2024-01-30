import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    num_len = int(input())

    binary_string = input()

    max_continuation_1 = 0  # 연속한 1의 개수의 최대값

    for i in range(num_len):

        temp = 0    # 각 자리에서 연속한 1의 개수를 세는 변수

        # 현재 값이 1이라면, 현재 값을 기준으로 순회
        # 순회하면서 1을 만난다면 temp변수를 하나 더함
        # 0을 만난다면 순회를 그만둠

        if binary_string[i] == '1':
            for j in range(i, num_len):
                if binary_string[j] == '1':
                    temp += 1
                elif binary_string[j] == '0':
                    break

            # temp가 기존의 최대값보다 크다면 최대값을 갱신함
            if  max_continuation_1 < temp:
                max_continuation_1 = temp
    print(f'#{testcase} {max_continuation_1}')