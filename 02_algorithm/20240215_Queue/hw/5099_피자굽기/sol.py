import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    size, num = map(int, input().split())
    cheese = deque([int(x), i] for i, x in enumerate(input().split()))
    oven = deque()
    
    for i in range(size):
        oven.append(cheese.popleft())


    while cheese:
        pizza = oven.popleft()
        pizza[0] //= 2

        if pizza[0] == 0:
            oven.append(cheese.popleft())
        else:
            oven.append(pizza)

    while oven:
        pizza = oven.popleft()
        pizza[0] //= 2

        if pizza[0] != 0:
            oven.append(pizza)

    print(f'#{testcase} {pizza[1] + 1}')