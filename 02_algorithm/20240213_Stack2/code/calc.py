# 식은 무조건 괄호로 둘러쌓여있어야함

infix = '(6+5*(2-8)/2)'
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

print(postfix)