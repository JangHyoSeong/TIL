import sys
sys.stdin = open('input.txt')

def quater(i, temp_money):
    # 분기별 금액을 구하고, 1년치 돈을 계산하는 함수
    if i == 12:
        money_result.append(temp_money)
        return

    # 3개월 이용료와 그냥 사용료를 둘다 계산
    if sum(money[i:i+3]) > voucher[2]:
        quater(min(i+3, 12), temp_money + voucher[2])
    quater(i+1, temp_money + money[i])


T = int(input())

for testcase in range(1, T+1):
    voucher = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    money = [0] * 12
    money_monthly = [0] * 12
    money_result = []
    
    for i in range(12):
        money[i] = plan[i] * voucher[0]
        if money[i] > voucher[1]:
            money[i] = voucher[1]
    
    quater(0, 0)

    print(f'#{testcase} {min(voucher[3], min(money_result))}')