import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    
    bracket = list(input())

    stack = []
    now = 0
    is_valid = True

    for c in bracket:
        if c == '(':
            stack.append(c)
            now += 1
        else:
            if now == 0:
                is_valid = False
                break
            stack.pop()
            now -= 1
            
    if now != 0:
        is_valid = False

    print(f'#{testcase} {is_valid}')