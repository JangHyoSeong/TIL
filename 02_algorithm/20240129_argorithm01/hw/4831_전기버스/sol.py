import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    move_range, length, charge = map(int, input().split())
    charge_list = list(map(int, input().split()))

    charge_cnt = 0      # 충전 횟수
    next_charge = 0     # 충전하는 곳 위치
    current_position = 0    # 현재 위치

    # 도착할 때까지 반복
    while current_position + move_range < length:

        # 일단 현재위치에서 최대이동했을때, 충전소가 있는 경우
        next_charge = current_position + move_range

        # 현재위치에서 최대 이동거리까지 이동했을 때 충전소가 있다면
        if next_charge in charge_list:
            # 충전 횟수를 하나 더하고, 현재 위치를 충전소의 위치로 갱신
            charge_cnt += 1
            current_position = next_charge

        # 최대 이동거리에 충전소가 없다면
        else:

            # 최대 이동거리에서 하나씩 줄여서 충전소를 찾음
            for i in range(move_range, 0, -1):

                # 하나씩 줄이면서 충전소를 찾았다면 위치를 갱신, 카운트 추가
                if current_position + i in charge_list:
                    charge_cnt += 1
                    current_position += i
                    break

            #충전소가 거리내에 없다면 카운트를 0으로 만들고 break로 반복문 탈출
            else:
                charge_cnt = 0
                break

    print(f'#{testcase} {charge_cnt}')