import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 입력을 리스트로 받음
    s = list(input())

    # 빈 스택을 정의하고, 현재 스택의 높이를 0으로 설정
    stack = []
    stack_size = 0

    # 입력받은 문자열을 전부 비울때까지 반복
    while s != []:

        # 스택이 비어있다면, 일단 s의 마지막값을 스택에 집어넣음
        if stack_size == 0:
            stack.append(s.pop())
            stack_size += 1
            continue
        
        # 스택이 비어있지 않다면 s의 마지막값을 뺀 후 temp변수에 저장
        temp = s.pop()

        # temp변수가 스택의 맨 위값과 같지않다면(연속된 문자가 같지 않다면)
        # 스택에 temp변수를 push하고 크기를 1늘림
        if temp != stack[stack_size-1]:
            stack.append(temp)
            stack_size += 1

        # temp변수가 스택의 top값과 같다면(연속된 문자라면)
        # pop을 통해 연속된 문자 2개를 지움
        else:
            stack.pop()
            stack_size -= 1


    print(f'#{testcase} {stack_size}')