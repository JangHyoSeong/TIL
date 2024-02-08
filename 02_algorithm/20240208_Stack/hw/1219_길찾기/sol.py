import sys
sys.stdin = open('input.txt')

for testcase in range(1,11):
    T, N = map(int, input().split())

    # 일단 정점과 길을 한 리스트에 입력받음
    graph = list(map(int, input().split()))
    

    # 각 인덱스는 어떤 정점으로 향하는지 나타냄
    # 예를들어 road1[0]의 값은 정점 0이 어느 정점으로 향하는지 알려줌
    road1 = [None] * 100
    road2 = [None] * 100
    result = 0

    # 길을 먼저 road1에 넣어주고, road1에 이미 값이 있다면 road2에 넣음
    for i in range(0, len(graph), 2):
        if road1[graph[i]] is None:
            road1[graph[i]] = graph[i+1]
        else:
            road2[graph[i]] = graph[i+1]

    # 방문한 정점은 visited 스택에 저장. 0에서 시작하니 초기값으로 0을 넣음
    visited = [0]

    # 지나간 길을 지우기 위해 temp변수를 사용
    # 지우지 않으면 무한루프에 빠질 수 있음
    temp = visited[0]

    # 스택이 빌때까지 반복
    while visited != []:

        # 목적지에 도착한 경우 break
        if road1[visited[-1]] == 99 or road2[visited[-1]] == 99:
            result = 1
            break

        # None이 아니라면 == 길이 있다면
        if road1[visited[-1]] is not None:
            # 방문한 정점을 스택에 삽입
            visited.append(road1[visited[-1]])
            # 지나온 길을 지움
            road1[temp] = None
            # 어떤 길을 지나갔는지 기억함
            temp = visited[-1]
        
        # 일단 road1을 먼저 검사한 후, road2가 None이 아니라면
        # 앞에서 한 작업과 동일
        elif road2[visited[-1]] is not None:
            visited.append(road2[visited[-1]])
            road2[temp] = None
            temp = visited[-1]

        # road1, road2가 둘 다 None이라면 == 길이 없다면
        # 스택에서 pop(다른 경로를 찾음)
        else:
            visited.pop()
            if visited != []:
                temp = visited[-1]


    print(f'#{T} {result}')