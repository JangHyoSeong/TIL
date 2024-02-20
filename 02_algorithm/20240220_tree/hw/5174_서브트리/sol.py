import sys
sys.stdin = open('input.txt')


def countSubTree(N):
    # 서브트리의 노드가 몇 개인지 세기위한 함수
    # 자식노드로 이동하면서 재귀적으로 호출됨
    global count

    # 왼쪽 자식 노드가 있다면, 왼쪽으로 이동
    if left[N]: #left[1] -> 1번 왼쪽자식노드
        count += 1
        countSubTree(left[N])

    # 오른쪽 자식 노드가 있다면, 오른쪽으로 이동
    if right[N]:
        count += 1
        countSubTree(right[N])

T = int(input())

for testcase in range(1, T+1):
    E, N = map(int, input().split())
    
    edges = list(map(int, input().split()))

    # 왼쪽, 오른쪽 자식노드의 여부를 저장하는 배열
    left = [0] * (E+2)
    right = [0] * (E+2)

    # 배열에 값을 입력
    for i in range(0, E):
        root, leaf = edges[i*2], edges[i*2+1]

        if left[root] == 0:
            left[root] = leaf
        else:
            right[root] = leaf

    # 자신을 포함하기에 count는 1부터 시작
    count = 1
    # 함수를 실행. N의 위치에서 시작하기에 초기값을 N을 줌
    countSubTree(N)
    print(f'#{testcase} {count}')
