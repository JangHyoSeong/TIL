import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    size, num = map(int, input().split())
    cheese = list(map(int, input().split()))

    oven = []

    # 오븐에 처음으로 피자를 넣음
    for i in range(size):
        # 오븐은 2차원 리스트. 첫번째 값은 치즈, 두번째 값은 피자의 번호
        oven.append([cheese[i], i])
        
    now_pizza_index = size


    while now_pizza_index < num:

        for i in range(size):
            if oven[i][0] > 0:
                oven[i][0] //= 2

            if oven[i][0] == 0 and now_pizza_index < num:
                oven[i] = [cheese[now_pizza_index], now_pizza_index]
                now_pizza_index += 1


    while oven:
        i = 0

        while i < len(oven):
            if oven[i][0] == 0:
                pizza = oven.pop(i)
                continue

            elif oven[i][0] > 0:
                oven[i][0] //= 2
            
            i += 1

    print(f'#{testcase} {pizza[1]+1}')