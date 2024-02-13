import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    postfix = list(input().split())
    result = 0

    stack = []


    # 후위 표기식을 순회
    for tk in postfix:

        # 숫자라면 스택에 삽입
        if tk.isdigit():
            stack.append(int(tk))

        # 연산자라면
        elif tk in '/*+-':

            # 두 숫자를 pop하여 연산 수행
            # 만약 indexerror가 발생한다면 error를 저장하고 break
            try:
                second = stack.pop()
                first = stack.pop()
            except IndexError:
                result = 'error'
                break

            # 각각의 연산 수행, 오류가 발생할 상황 처리
            if tk == '+':
                stack.append(first + second)
            if tk == '*':
                stack.append(first * second)
            if tk == '/':
                if second == 0:
                    result = 'error'
                    break
                stack.append(first // second)
            if tk == '-':
                stack.append(first - second)

        # . (연산이 종료된다면)
        elif tk == '.':

            # 숫자와 연산자의 개수가 맞지 않았을 경우 error 저장
            if len(stack) != 1:
                result = 'error'

            # 오류 없이 끝났다면 제대로 결과를 반환
            else:    
                result = stack.pop()
            break


    print(f'#{testcase} {result}')