import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 입력받음
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 계산이 용이하게 정렬
    cargo.sort(reverse=True)
    truck.sort(reverse=True)

    # 트럭과 화물을 순회
    result = []
    for i in range(M):
        
        # 크기가 큰 화물부터 시작해서 트럭에 넣을 수 있는지 검사
        for j in range(N):
            # 넣을 수 있다면 result리스트에 값을 삽입하고 그 값을 사용할 수 없게 설정
            if cargo[j] <= truck[i]:
                result.append(cargo[j])
                cargo[j] = 100
                break
        else:
            # 아무런 짐도 넣을 수 없다면 0을 삽입
            result.append(0)

    print(f'#{testcase} {sum(result)}')