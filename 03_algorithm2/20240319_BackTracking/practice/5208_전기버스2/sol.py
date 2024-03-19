import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    # 입력받음
    stations = list(map(int, input().split()))
    # 정류장의 개수는 입력받은 리스트의 첫번째 값
    num_of_station = stations[0]

    # 시작 위치는 인덱스 1
    now_position = 1

    # 몇번 교체했는지 세는 변수
    cnt = 0

    # 현재 위치가 끝에 도착하기 전까지 반복
    while now_position < num_of_station:
        # 만약 현재 위치에서 끝까지 갈 수 있다면 반복 탈출
        if now_position + stations[now_position] >= num_of_station:
            break

        # 연산에 사용할 배열을 선언
        temp_arr = []

        # 현재 위치에서 갈 수 있는 모든 정류장을 순회
        for i in range(1, stations[now_position]+1):
            # 현재 방문할 수 있는 위치 인덱스
            move_position = now_position + i

            # 이 인덱스를 가중치를 더해 리스트에 삽입
            # 예를들어 현재 위치와 2만큼 떨어진 위치에, 4 충전지가 있었다면,
            # 이 위치에서 배터리를 교체한다면 6만큼 이동할 수 있으니, 6을 리스트에 넣어줌
            temp_arr.append(i + stations[move_position])

        # 이동할 수 있는 거리가 최대가 되는 곳으로 이동함
        moving = temp_arr.index(max(temp_arr))
        now_position += moving + 1

        # 교체 횟수를 더해줌
        cnt += 1

    print(f'#{testcase} {cnt}')