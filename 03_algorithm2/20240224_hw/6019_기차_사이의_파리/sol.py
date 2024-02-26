import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    distance, A, B, speed = map(int, input().split())

    # 기차가 충돌하기 까지 걸리는 시간
    time = distance / (A + B)

    # 파리가 이동하는 거리
    result = time * speed

    print(f'#{testcase} {result}')


'''
나누기를 먼저 하고 곱하기를 하면 오차가 커질 수 있음
따라서 곱하기를 먼저 한 후, 나누기를 하는 것이 좋음
'''