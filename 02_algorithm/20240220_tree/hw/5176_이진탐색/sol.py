import sys
sys.stdin = open('input.txt')


def createTree(n):
    # 주어진 조건에 맞는 트리를 생성하는 함수
    # 재귀적으로 호출되며 트리에 값을 넣음
    global count

    # node가 N개이니 범위를 설정
    if n <= N:
        # n*2는 자신의 왼쪽 자식
        # 자신보다 작은 값이 들어가야함
        # 그렇기에 count가 1 증가하기 전에 호출됨
        # 결국 재귀적 호출이 끝난다면 가장 아래 가장 왼쪽부터 1, 2, 3 ...숫자가 할당됨
        createTree(n*2)

        tree[n] = count
        count += 1

        # n*2 + 1은 자신 기준 오른쪽 자식
        # 결국 맨 마지막 오른쪽 노드는 가장 큰 숫자가 들어가게 됨
        createTree(n*2+1)


T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    count = 1

    # 트리 노드에 있는 값을 저장
    tree = [0] * (N+1)

    # 1번(부모)의 경우부터 순차적으로 할당
    createTree(1)
    print(tree)
    print(f'#{testcase} {tree[1]} {tree[N//2]}')