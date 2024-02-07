import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 문장을 입력받음
    sentence = input()

    # 문제 풀이를 위한 스택 선언
    bracket_stack = []
    stack_size = 0

    # 문장의 괄호가 이상하다면 0이 될 변수
    is_valid = 1

    for c in sentence:

        # 여는괄호를 만나면 스택에 괄호를 push
        # 스택의 크기(길이)도 하나 늘림
        if c == '(':
            bracket_stack.append(c)
            stack_size += 1
        elif c == '{':
            bracket_stack.append(c)
            stack_size += 1

        # 닫는 괄호를 만나면, 일단 스택이 비어있는지 검사함
        # 스택이 비어있다면 is_valid를 0으로 설정
        # 스택이 비어있지 않다면 pop을 하여 맞는 여는괄호인지 확인
        if c == ')':
            if stack_size < 1:
                is_valid = 0
                break
            stack_size -= 1
            if bracket_stack.pop() != '(':
                is_valid = 0
                break
        if c == '}':
            if stack_size < 1:
                is_valid = 0
                break
            stack_size -= 1
            if bracket_stack.pop() != '{':
                is_valid = 0
                break

    # 작업이 끝난 후 스택이 비어있지 않다면 오류
    if stack_size != 0:
        is_valid = 0

    print(f'#{testcase} {is_valid}')