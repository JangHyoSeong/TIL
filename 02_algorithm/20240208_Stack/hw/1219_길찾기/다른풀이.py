# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
 
T = 10
for test_case in range(1, T+1):
    # 테스크 케이스 번호와 길의 총개수 받기
    a, b = map(int, input().split())
    # 그다음 줄 순서쌍을 일단 배열로 다 받기
    input_arr = list(map(int, input().split()))
    # 배열로 받은 후 각 인덱스를 출발점, 도착점은 배열 내의 값으로 만들기
    field = [[] for _ in range(100)]
    for i in range(0, len(input_arr), 2):
        field[input_arr[i]].append(input_arr[i+1])
     
    # 각 노드가 방문된 정보, 초기값은 다 False로 저장   
    visited = [False] * 100
     
    # 정의된 DFS 함수 호출
    dfs(field, 0, visited)
     
    # 99를 방문했다면 1 하지 않았다면 0 출력
    if visited[99]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')