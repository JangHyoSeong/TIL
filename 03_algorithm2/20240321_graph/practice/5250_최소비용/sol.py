import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush
INF = 21e8
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra(start):
    pq = []

    # 초기 값을 우선순위 큐에 넣음
    # (현재까지 누적 연료, 위치)
    heappush(pq, (0, start))

    # 누적 연료 사용량을 저장할 리스트
    fuel = [[INF] * N for _ in range(N)]

    # 시작값의 연료를 0으로 초기화
    fuel[start[0]][start[1]] = 0

    # queue가 전부 빌 때까지
    while pq:
        # 현재 노드에서 누적 연료 사용량, 위치
        now_fuel, now = heappop(pq)

        # 만약 이 경우의 수에서 누적 연료 사용량이 최소 연료 사용량보다 크다면
        # 이 경우의 수는 이미 최소가 아님, 고려하지 않음
        if fuel[now[0]][now[1]] < now_fuel:
            continue

        # 인접 위치를 델타탐색으로 검색
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            # 이동할 위치가 인덱스를 벗어나지 않는다면
            if 0 <= nx < N and 0 <= ny < N:
                # 이동할 위치의 좌표
                new_node = [nx, ny]

                # 현재 위치의 가중치
                now_weight = table[now[0]][now[1]]

                # 이동할 위치의 가중치
                next_weight = table[nx][ny]
                
                # 이동할 때 드는 연료, 최소 1이 들고, 높이차가 나는경우 고려
                next_fuel = max(1, next_weight - now_weight + 1)

                # 누적 연료 사용량은 지금까지 사용한 연료 + 움직이면서 사용할 연료
                new_fuel = now_fuel + next_fuel

                # 만약 누적연료사용량이 기존에 구해둔 누적연료 사용량보다 크다면 고려하지 않음
                if new_fuel >= fuel[nx][ny]:
                    continue

                # 이번 값이 최소값이라면 최소값을 갱신함
                fuel[nx][ny] = new_fuel
                # 이 경우의 수를 우선순위큐에 다시 삽입
                heappush(pq, (new_fuel, new_node))

    return fuel


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    start = [0, 0]

    fuel = dijkstra(start)
    print(f'#{testcase} {fuel[N-1][N-1]}')