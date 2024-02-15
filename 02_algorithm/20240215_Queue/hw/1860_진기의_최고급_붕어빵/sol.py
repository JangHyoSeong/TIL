import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M, K = map(int, input().split())

    arrival = list(map(int, input().split()))
    arrival.sort()

    result = 'Possible'

    # 첫 손님이 도착한 시간에
    bread = (arrival[0] // M) * K
    left_sec = arrival[0] % M
    bread -= 1

    if bread < 0:
        result = 'Impossible'

    for i in range(0, N-1):
        bread += ((arrival[i+1] - arrival[i] + left_sec) // M) * K
        left_sec = (arrival[i+1] - arrival[i] + left_sec) % M
        bread -= 1
        if bread < 0:
            result = 'Impossible'
            break

    print(f'#{testcase} {result}')