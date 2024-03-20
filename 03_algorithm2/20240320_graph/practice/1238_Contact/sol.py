import sys
sys.stdin = open('input.txt')

from collections import deque

for testcase in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 간선의 정보를 저장할 딕셔너리
    # 키는 시작노드, value는 도착노드가 됨
    edges = {}

    for i in range(0, N, 2):
        # value는 set로 이루어짐
        if edges.get(arr[i]) is None:
            edges[arr[i]] = {arr[i+1]}
        else:
            edges[arr[i]].add(arr[i+1])

    # 시작 위치에 방문 표시
    visited = [start]

    # 더이상 이동할 수 없는 경우, 그 노드들의 위치와 이동 횟수를 저장할 리스트
    result = []

    # BFS를 위한 queue
    queue = deque()
    queue.append((start, 0))


    # BFS
    while queue:
        now, cnt = queue.popleft()
        
        # 만약 갈 수 있는 곳이 있다면
        if edges.get(now) is not None:
            # 조건분기를 위해 사용할 flag
            flag = True

            # 갈 수 있는 노드들을 방문
            for edge in edges[now]:

                # 방문한적 없는 곳이라면 방문
                if edge not in visited:

                    # 이번 노드에서 한곳이라도 방문한다면 flag = false
                    flag = False
                    queue.append((edge, cnt+1))
                    visited.append(edge)
            # 만약 이번 노드에서 한곳도 방문하지 못한다면 result에 삽입
            if flag:
                result.append([now,cnt])

        # 애초에 갈 수 있는 노드가 없다면 result에 삽입
        else:
            result.append([now, cnt])

    # 두번 정렬해서 모든 원소에 대해서 내림차순 정렬
    result.sort(key=lambda x : x[0], reverse=True)
    result.sort(key=lambda x : x[1], reverse=True)

    print(f'#{testcase} {result[0][0]}')