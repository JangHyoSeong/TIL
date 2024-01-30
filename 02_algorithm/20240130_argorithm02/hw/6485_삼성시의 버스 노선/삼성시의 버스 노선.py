import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N = int(input())
    
    # A, B의 값을 저장하기 위한 리스트
    min_value = []
    max_value = []

    # A, B 값을 입력받음
    for i in range(N):
        a, b = map(int, input().split())
        min_value.append(a)
        max_value.append(b)

    # 버스 정류장을 입력받음
    bus_station_num = int(input())
    bus_station = []

    for i in range(bus_station_num):
        bus_station.append(int(input()))

    # 결과로 쓸 리스트
    result = [0] * bus_station_num


    # 각 버스정류장에 버스가 몇대 오는지 확인
    for i in range(bus_station_num):
        for j in range(N):
            if bus_station[i] >= min_value[j] and bus_station[i] <= max_value[j]:
                result[i] += 1

    print(f'#{testcase}', end='')

    for i in result:
        print(f' {i}', end='')
    print()
