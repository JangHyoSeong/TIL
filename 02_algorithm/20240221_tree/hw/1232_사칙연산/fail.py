import sys
sys.stdin = open('input.txt')

T = 10

def inorder(n):

    if n <= N:
        left_value = inorder(left[n])
        current_value = nodes[n][1]
        right_value = inorder(right[n])
        
        if current_value == '+':
            return left_value + right_value
        
        elif current_value == '*':
            return left_value * right_value
        
        elif current_value == '-':
            return left_value - right_value
        
        elif current_value == '/':
            return left_value / right_value
        else:
            return float(current_value)
    
    return 0

for testcase in range(1, T+1):
    N = int(input())

    left = [0] * (N+1)
    right = [0] * (N+1)
    nodes = [0] + [list(input().split()) for _ in range(N)]

    for i in range(1, N+1):
        
        if not nodes[i][1].isdigit():
            left[int(nodes[i][0])] = int(nodes[i][2])
            right[int(nodes[i][0])] = int(nodes[i][3])


    print(inorder(1))