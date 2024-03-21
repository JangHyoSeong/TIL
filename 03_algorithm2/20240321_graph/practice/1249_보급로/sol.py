import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop
INF = 21e8
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra(start):
    pq = []

    heappush(pq, (0, start))
    time[0][0] = 0

    while pq:
        now_time, now = heappop(pq)

        if time[now[0]][now[1]] < now_time:
            continue

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new = (nx, ny)
                next_time = table[nx][ny]
                new_time = now_time + next_time

                if new_time < time[nx][ny]:
                    time[nx][ny] = new_time
                    heappush(pq, (new_time, new))


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    table = [list(map(int, input())) for _ in range(N)]

    time = [[INF] * N for _ in range(N)]

    dijkstra((0, 0))

    print(f'#{testcase} {time[N-1][N-1]}')