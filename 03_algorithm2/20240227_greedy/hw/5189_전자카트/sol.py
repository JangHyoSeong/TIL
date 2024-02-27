import sys
sys.stdin = open('input.txt')


def findMin(now, acc):
    # 재귀적으로 최소값을 찾을 함수
    global min_sum

    if all(visited):    # 모든 방을 방문했다면
        # 마지막으로 0번 구역으로 돌아올만큼 더함
        acc += arr[now][0]
        if min_sum > acc:
            min_sum = acc
    
    # 이미 최소값을 넘었다면 중지
    elif acc > min_sum:
        return
        
    else:
        # 모든 경우의수를 고려
        for next in range(1, N):

            # 현재 위치가 아니며, 방문하지 않은 곳이라면
            if now != next and not visited[next]:
                # 방문 표시 후 누적합 갱신, 이동
                visited[next] = True
                findMin(next, acc + arr[now][next])
                # 돌아오면서 이동을 False로 바꿈
                visited[next] = False



T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 임의의 큰 수
    min_sum = 2**31 - 1

    # 방문 여부를 저장하는 리스트
    visited = [False] * N
    # 시작점은 우선 True
    visited[0] = True

    findMin(0, 0)

    print(f'#{testcase} {min_sum}')