import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):


    # 입력 받기
    testcase_list = list(map(str, input().split()))
    num_of_nums = int(testcase_list[1])
    char_num = list(map(str, input().split()))

    # 카운트 정렬을 사용하기 위한 카운트 배열
    counts = [0] * 10

    # 각각의 숫자가 몇개인지 숫자를 셈
    for i in range(num_of_nums):
        if char_num[i] == 'ZRO':
            counts[0] += 1

        elif char_num[i] == 'ONE':
            counts[1] += 1

        elif char_num[i] == 'TWO':
            counts[2] += 1

        elif char_num[i] == 'THR':
            counts[3] += 1

        elif char_num[i] == 'FOR':
            counts[4] += 1

        elif char_num[i] == 'FIV':
            counts[5] += 1

        elif char_num[i] == 'SIX':
            counts[6] += 1

        elif char_num[i] == 'SVN':
            counts[7] += 1

        elif char_num[i] == 'EGT':
            counts[8] += 1

        elif char_num[i] == 'NIN':
            counts[9] += 1

    print(f'#{testcase}')

    # 센 숫자만큼 출력
    for i in range(len(counts)):
        if i == 0:
            print('ZRO ' * counts[i], end='')
        elif i == 1:
            print('ONE ' * counts[i], end='')
        elif i == 2:
            print('TWO ' * counts[i], end='')
        elif i == 3:
            print('THR ' * counts[i], end='')
        elif i == 4:
            print('FOR ' * counts[i], end='')
        elif i == 5:
            print('FIV ' * counts[i], end='')
        elif i == 6:
            print('SIX ' * counts[i], end='')
        elif i == 7:
            print('SVN ' * counts[i], end='')
        elif i == 8:
            print('EGT ' * counts[i], end='')
        elif i == 9:
            print('NIN ' * counts[i], end='')
    print()