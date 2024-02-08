import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 입력받음
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    result = 0

    # 경로 탐색에 사용할 스택. 초기값은 시작위치
    stack = [S]

    # 스택이 비어있지 않다면
    while stack:

        # 스택의 마지막 값이 도착점이라면 종료
        if stack[-1] == G:
            result = 1
            break

        # node와 방향을 순회하면서
        for road in node:
            # 현재 위치에서 갈수있는 곳이 있다면 이동후 스택에 집어넣음
            if stack[-1] == road[0] and road[1] != -1:
                stack.append(road[1])
                road[1] = -1
                break

        # 현재 위치에서 갈수있는 곳이 없다면 스택 pop
        else:
            stack.pop()

    print(f'#{testcase} {result}')