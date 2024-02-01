import sys
sys.stdin = open('input.txt')

# 상수 정의
MIN = 0
MAX = 1


T = int(input())

for testcase in range(1, T+1):

    # 변수 입력받음
    length = int(input())
    numbers = list(map(int, input().split()))

    # 맨 처음 값은 최대값이 들어가기 때문에, flag를 최대값으로 맞춤
    flag = MAX

    # selection sort
    for i in range(length-1, 0, -1):
        
        for j in range(length-1, length - i - 1, -1):

            # 최대값을 찾는 경우
            if flag == MAX:
                if numbers[j-1] < numbers[j]:
                    numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            
            # 최소값을 찾는 경우
            elif flag == MIN:
                if numbers[j-1] > numbers[j]:
                    numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

        # 최대값, 최소값 상태를 바꿈
        if flag == MIN:
            flag = MAX
        elif flag == MAX:
            flag = MIN

    print(f'#{testcase}', end='')
    for i in range(10):
        print(f' {numbers[i]}', end='')
    print()