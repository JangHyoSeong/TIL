def make_set(x):
    # parent 정보와 rank 정보를 같이 반환
    parent = [i for i in range(x)]
    rank = [0] * x # 첫 make_set 실행시 본인을 루트로 하는 노드만 존재
    return parent, rank

# 1~6번 노드가 존재
parent, rank = make_set(7)

def find_set(x):
    # 평탄화 작업 -> findset 진행할 때 루트에 붙여준다
    
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    
    return parent[x]
    
    



def union(x, y):
    # x, y 집합을 연결하는 작업

    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합이라면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    
    # 랭크가 동일한 경우는 둘 중에 하나 정해서 rank를 상승시킴
    else:
        parent[y] = x
        rank[x] += 1


