import sys
sys.stdin = open('input.txt')

for testcase in range(1, 11):

    N = int(input())
    result = 0

    # 괄호를 추가시켜서 제대로 연산될수 있도록 바꿈

    infix = '('
    infix += input()
    infix += ')'
    postfix = ''
    stack = [0] * 100
    top = -1

    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}


    for tk in infix:
        # 여는 괄호는 push, top원소보다 우선순위가 높으면 push
        if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
            top += 1
            stack[top] = tk
            

        elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:   # 연산자이고 우선순위가 낮다면
            while isp[stack[top]] >= icp[tk]:   # 우선순위가 높은 것을 만날때까지 pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = tk
        elif tk == ')':
            while stack[top] != '(':
                postfix += stack[top]
                top -= 1
            top -= 1  # 여는 괄호를 pop으로 버림
            

        else:
            postfix += tk

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

        #숫자라면 push
        else:
            top += 1
            stack[top] = int(tk)

    result = stack[top]


    print(f'#{testcase} {result}')