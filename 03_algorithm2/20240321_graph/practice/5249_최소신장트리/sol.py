import sys
sys.stdin = open('input.txt')

def find_set(x):
    # union-find를 위한 함수
    # 현재 집합의 대표자를 찾음
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    # 집합을 합치고, 대표자를 노드 번호가 가장 작은 노드로 만듦
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합이라면 작업 종료
    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())

for testcase in range(1, T+1):
    V, E = map(int, input().split())

    # 각 집합의 대표자를 저장할 리스트
    # V는 0부터 시작한 노드들의 끝 노드값이 들어있기 때문에 노드의 개수는 총 V+1개
    parents = list(range(V+1))

    #kruskal 방식을 사용하기 위해 빈 리스트 생성
    edges = []

    # 빈 리스트에 시작노드, 끝노드, 가중치를 넣음
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append([s, e, w])

    # 가중치를 기준으로 간선 오름차순 정렬
    edges.sort(key=lambda x : x[2])

    # 최소 가중치 누적합
    sum_weight = 0
    # 간선이 몇개인지 세는 cnt
    cnt = 0

    # 모든 간선들을 순회하면서
    for s, e, w in edges:

        # 시작과 끝의 대표자가 같다 -> 사이클이 존재한다
        # 이 경우 최소신장 불가능
        if find_set(s) == find_set(e):
            continue

        # 사이클이 없는 경우, 오름차순 정렬되어있기에 항상 가장 가중치가 작은 곳부터 시작
        # union을 통해 같은 집합으로 만들어줌
        union(s, e)
        sum_weight += w
        cnt += 1

        # 이미 최소신장트리가 만들어져서 무의미한 연산을 줄이기 위해 종료조건 추가
        if cnt == V:
            break

    print(f'#{testcase} {sum_weight}')