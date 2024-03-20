import sys
sys.stdin = open('input.txt')

def find_set(x):
    # 부모를 찾는 함수
    if parents[x] == x:
        return x
    
    # 자기 자신이 부모일 때 까지, (가장 높은 위치) 반복
    return find_set(parents[x])

def union(x, y):
    # x, y 집합을 연결하는 함수

    # 부모를 찾음
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합이라면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    # 작은 숫자가 우선적으로 부모가 되도록 만듦
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 부모 정보를 저장할 리스트 만듦
    parents = [i for i in range(N+1)]

    # 입력받은 숫자들을 같은 집합으로 합침
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)

    # 중복 제거를 하기 위해 set를 사용
    temp_set = set()

    # 각 집합의 부모를 set에 넣음
    for i in range(1, N+1):
        temp_set.add(find_set(i))
    
    # set 원소의 개수가 집합의 개수
    print(f'#{testcase} {len(temp_set)}')