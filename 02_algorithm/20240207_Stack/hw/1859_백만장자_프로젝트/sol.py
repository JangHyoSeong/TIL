import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))

    # 결과값으로 쓸 최대 이익 변수 정의
    max_profit = 0

    # 물건을 판매할 가격인 최대가격 설정
    # 초기 값은 배열의 마지막값
    max_cost = cost[-1]

    # 배열을 뒤에서부터 순회
    # 앞에서부터 순회하면 연산이 더 많아짐
    # 뒤에서부터 순회할경우, 이전까지의 최대값보다 큰 수가 나오면
    # 팔 수 있는 최대값이 갱신되는 형태
    for i in range(N - 2, -1, -1):

        # 뒤에서부터 순회하면서, 값들이 최대값보다 작다면
        # 차익을 결과에 더함
        if cost[i] < max_cost:
            max_profit += max_cost - cost[i]

        # 최대값보다 크다면 최대값을 갱신
        else:
            max_cost = cost[i]
    
    print(f"#{case} {max_profit}")