import sys
sys.stdin = open('input.txt')

def inorder(now):
    if now:
        global equ
        inorder(tree[now][1])
        inorder(tree[now][2])
        equ.append(tree[now][0])
 
for tc in range(10):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    equ, stack = [], []
    for _ in range(N):
        idx, *etc = input().split()
        idx = int(idx)
        if etc[0].isdecimal():
            tree[idx][0] = etc[0]
        else:
            tree[idx][0] = etc[0]
            tree[idx][1] = int(etc[1])
            tree[idx][2] = int(etc[2])
 
    inorder(1)
 
    for char in equ:
        if char.isdecimal():
            stack.append(char)
        else:
            a = float(stack.pop())
            b = float(stack.pop())
            if char == '+':
                stack.append(b + a)
            elif char == '-':
                stack.append(b - a)
            elif char == '*':
                stack.append(b * a)
            else:
                stack.append(b / a)
     
    print(f'#{tc+1} {int(stack[0])}')