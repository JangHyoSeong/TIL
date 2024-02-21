import sys
sys.stdin = open('input.txt')

T = 10

# 후위 순회
# 식을 후위 계산식으로 calc 스택에 삽입
def inorder(n):

    # 연산자라면(자식이 있다면) 자식으로 순회하고 연산자를 마지막에 삽입
    if n <= N and len(nodes[n]) == 4:
        inorder(nodes[n][2])
        inorder(nodes[n][3])
        calc.append(nodes[n][1])

    # 연산자가 아니라면 스택에 바로 삽입
    elif n <= N:
        calc.append(nodes[n][1])

for testcase in range(1, T+1):
    N = int(input())

    # 트리의 노드들을 입력받음
    nodes = [0] + [list(input().split()) for _ in range(N)]
    stack = []
    calc = []
    
    # 그냥 정수로 표현가능한 변수는 전부 정수로 변환
    for i in range(1, N+1):
        if len(nodes[i]) == 4:
            nodes[i][0] = int(nodes[i][0])
            nodes[i][2] = int(nodes[i][2])
            nodes[i][3] = int(nodes[i][3])
        else:
            nodes[i][0] = int(nodes[i][0])
            nodes[i][1] = int(nodes[i][1])

    inorder(1)

    # 후위 계산식으로 표현된 계산식을 계산
    for c in calc:
        if isinstance(c, int):
            stack.append(c)
        else:
            second = float(stack.pop())
            first = float(stack.pop())

            if c == '+':
                stack.append(first + second)

            elif c == '-':
                stack.append(first - second)

            elif c == '*':
                stack.append(first * second)

            else:
                stack.append(first / second)
     
    print(f'#{testcase} {int(stack[0])}')