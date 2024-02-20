import sys
sys.stdin = open('input.txt')

def inorder(root):
    # 중위 순회를 진행하는 함수
    # 재귀적으로 호출됨
    # 인자로 받는 값은 부모노드

    # 부모 노드가 0이 아니라면(존재한다면)
    if int(root):
        # 왼쪽 노드로 이동
        inorder(left[root])
        # 현재 트리의 값을 출력
        print(nodes[root-1][1], end='')
        # 오른쪽 노드로 이동
        inorder(right[root])


for testcase in range(1, 11):
    N = int(input())

    nodes = [list(input().split()) for _ in range(N)]

    # 트리의 자식, 부모 정보를 갖는 배열
    left = [0] * (N+2)
    right = [0] * (N+2)
    parrent = [0] * (N+2)

    for node in nodes:
        
        # 인덱스 에러를 피하기 위해 다음과 같이 코드 구현
        num_of_item = len(node)
        
        if num_of_item == 3:
            left[int(node[0])] = int(node[2])
        elif num_of_item == 4:
            left[int(node[0])] = int(node[2])
            right[int(node[0])] = int(node[3])

    print(f'#{testcase}', end= ' ')
    inorder(1)
    print()