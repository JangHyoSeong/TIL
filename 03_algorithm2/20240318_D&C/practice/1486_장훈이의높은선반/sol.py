import sys
sys.stdin = open('input.txt')

def select(i, N, temp_sum, shelf):
    global min_height

    # 부분집합의 모든 원소를 결정했다면
    if i == N:
        # 선반보다 크고, 기존의 최소값보다 작다면
        if temp_sum >= shelf and temp_sum < min_height:
            # 최소값을 갱신
            min_height = temp_sum
        return

    # 이미 최소값을 넘었다면 종료
    if temp_sum > min_height:
        return
    
    # i번째 위치의 원소의 여부를 결정하고 두 경우로 나누어서 함수 실행
    select(i+1, N, temp_sum + height[i], shelf)
    select(i+1, N, temp_sum, shelf)




T = int(input())

for testcase in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    # 모두 더했을때의 값을 최솟값으로 시작. 점점 줄여나갈것
    min_height = sum(height)

    # 재귀 함수를 통해 부분집합을 찾고, 그 중 최소값을 찾을 것
    select(0, N, 0, B)

    print(f'#{testcase} {min_height - B}')