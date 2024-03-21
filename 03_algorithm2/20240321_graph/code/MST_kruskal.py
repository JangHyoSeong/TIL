'''
input
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 1. 전체 그래프를 보고 가중치가 제일 작은 간선부터 뽑자
# 코드로 구현하는 법 -> 전체 간선 정보를 저장 + 가중치로 정렬
# 2. 방문처리
# 이 때 사이클이 발생하면 안된다, 사이클 여부는 union-find 알고리즘을 활용

def find_set(x):
    if x == parents[x]:
        return x
    
    # 경로압축
    parents[x] = find_set(parents[x]) 
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())

# 간선 정보를 모두 저장
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w]) # 클래스로 하는 것이 좋음, 값이 더 많아지면 관리가 힘듦

# 가중치 기준으로 오름차순 정렬
edges.sort(key=lambda x : x[2])
parents = [i for i in range(V)] # union-find를 위한 대표자 배열

sum_weight = 0  # 누적합

# 연결된 간선이 몇개인지 세는 cnt
# 최소신장트리는 간선의 개수는 항상 노드의 개수 -1
# 따라서 최소신장트리가 완성된 이후 의미없는 연산을 줄인다
cnt = 0

# 간선들을 모두 확인한다
for s, e, w in edges:
    # 사이클이 발생하면 pass
    # -> union-find를 통해 이미 같은 집합에 속해있다면 pass
    if find_set(s) == find_set(e):
        continue

    # 사이클이 없다면 방문 처리
    union(s, e)
    sum_weight += w
    cnt += 1

    # 최소신장트리가 완성되면 반복 탈출
    if cnt == V-1:
        break


print(f'최소 비용 : {sum_weight}')