import sys

sys.stdin = open(input.txt)


for tc in range(1, int(input()) + 1):
    # 버스 정류장 초기화
    bus_stop = {}
    for num in range(1, 5001):
        bus_stop[num] = 0

    # 루트 개수 입력 및 버스 정류장 카운트
    for route in range(int(input())):
        start, end = map(int, input().split())
        for num in range(start, end + 1):
            bus_stop[num] += 1

    # 답 리스트에 추가
    answer = []
    for p in range(int(input())):
        answer.append(bus_stop[int(input())])

    print(f'#{tc}', *answer)