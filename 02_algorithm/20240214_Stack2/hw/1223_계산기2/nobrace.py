import sys
sys.stdin = open('input.txt')

for testcase in range(1, 11):

    N = int(input())
    result = 0

    # 괄호를 추가시켜서 제대로 연산될수 있도록 바꿈
    infix = input()

    # 후위계산식을 빈 문자열로 선언
    postfix = ''

    # 변환을 위한 스택 생성
    stack = [0] * 100
    top = -1

    # 우선순위를 정의한 딕셔너리
    icp = {'*':2, '/':2, '+':1, '-':1}
    isp = {'*':2, '/':2, '+':1, '-':1}


    for tk in infix:

        if tk.isdigit():
            postfix += tk
        elif top == -1:
            top += 1
            stack[top] = tk

        # 여는 괄호는 push, top원소보다 우선순위가 높으면 push
        elif tk in '*/+-' and isp[stack[top]] < icp[tk]:
            top += 1
            stack[top] = tk
            
        # 연산자이고 우선순위가 낮다면
        elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:   

            # 우선순위가 높은 것을 만날때까지 pop
            while top >= 0 and isp[stack[top]] >= icp[tk]:
                postfix += stack[top]
                top -= 1

            # 그 후 tk를 push
            top += 1
            stack[top] = tk

    while top >= 0:
        postfix += stack[top]
        top -= 1
            

    # 후위표기식을 순회
    for tk in postfix:

        # 연산자라면, 숫자 두개를 꺼내고 계산함
        if tk == '+':
            first = stack[top]
            second = stack[top-1]
            top -= 2

            top += 1
            # 계산한 값을 다시 스택에 넣음
            stack[top] = first + second

        elif tk == '*':
            first = stack[top]
            second = stack[top-1]
            top -= 1
            stack[top] = first * second
        

        #숫자라면 push
        else:
            top += 1
            stack[top] = int(tk)

    result = stack[top]


    print(f'#{testcase} {result}')