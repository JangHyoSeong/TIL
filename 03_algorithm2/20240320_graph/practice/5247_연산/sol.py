import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for testcase in range(1, T+1):
    num, target = map(int, input().split())

    # 방문 여부를 저장해둘 visited 리스트
    visited = [False] * 1000001

    # BFS를 사용하기 위해 queue사용
    queue = deque()
    # 시작할 숫자와 몇번 연산했는지 저장할 변수를 queue에 push
    queue.append((num, 0))

    # BFS 시작
    while queue:

        # queue에서 pop
        num, cnt = queue.popleft()

        # 이미 방문한 곳이라면 연산 수행하지 않음
        if visited[num]:
            continue

        # 방문한 곳 표시
        visited[num] = True

        # BFS이기 때문에 목표 숫자에 도착했다면 그 때가 최소횟수
        if num == target:
            min_cnt = cnt
            # 반복 탈출
            break

        # 주어진 숫자 범위에서 벗어나지 않는다면 queue에 push
        if 0 < num*2 <= 1000000:
            queue.append((num*2, cnt+1))
        if 0 < num-10 <= 1000000:
            queue.append((num-10, cnt+1))
        if 0 < num+1 <= 1000000:
            queue.append((num+1, cnt+1))
        if 0 < num-1 <= 1000000:
            queue.append((num-1, cnt+1))
        

    print(f'#{testcase} {min_cnt}')