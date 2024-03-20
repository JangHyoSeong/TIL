# 1~6번 까지 노드가 존재

def make_set(n):
    return [i for i in range(n)]    # 집합의 대표자 인덱스 정보를 가짐


parents = make_set(7)

def find_set(x):
    # x의 대표자가 누군지 찾는 작업
    if parents[x] == x:
        return x
    
    return find_set(parents[x])


def union(x, y):
    # x, y 집합을 연결하는 작업

    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합이라면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return

union(1, 3)
union(2, 3)
union(5, 6)

print(parents)