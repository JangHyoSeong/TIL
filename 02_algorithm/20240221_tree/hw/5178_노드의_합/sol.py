import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M, L = map(int, input().split())
    leafs = [list(map(int, input().split())) for _ in range(M)]
    
    # 전체 노드를 저장할 list
    # 자식이 없는 경우는 노드가 비어있는것으로 여김
    # 따라서 범위를 1 + N + 1으로 설정
    nodes = [0] * (N+2)

    # 리프 노드의 정보를 전체 노드에 저장
    for leaf in leafs:
        nodes[leaf[0]] = leaf[1]

    # 리프노드는 N//2+1부터이다
    # 따라서 부모 노드는 N//2부터 시작해서 하나씩 줄여가면서 값을 채운다
    for i in range(N//2, 0, -1):
        nodes[i] = nodes[i*2] + nodes[i*2+1]
        
    print(f'#{testcase} {nodes[L]}')