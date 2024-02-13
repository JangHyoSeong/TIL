import sys
sys.stdin = open('input.txt')

infix = input()

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}
operands = '/*+-'
stack = []
postfix = ''

for tk in infix:
    # 여는 괄호는 push, top원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in operands and isp[stack[-1]] < icp[tk]):
        stack.append(tk)
        

    elif tk in operands and isp[stack[-1]] >= icp[tk]:   # 연산자이고 우선순위가 낮다면
        while isp[stack[-1]] >= icp[tk]:   # 우선순위가 높은 것을 만날때까지 pop
            postfix += stack.pop()

        stack.append(tk)

    elif tk == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
            
        stack.pop()  # 여는 괄호를 pop으로 버림
        

    else:
        postfix += tk

print(postfix)