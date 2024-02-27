import sys
sys.stdin = open('input.txt')


def findMin(i, j, temp_sum, N):
    # 주어진 조건의 최소값을 찾는 함수
    # 재귀적으로 호출되며 가능한 모든 방향을 탐색

    # 최소값을 저장할 전역변수
    global min_sum

    # 만약 이동이 주어진 범위를 벗어나면 함수 호출 중지
    if i == N or j == N:
        return None
    
    # 만약 지금까지의 합이 이미 최소값을 넘어간다면 중지
    elif temp_sum > min_sum:
        return None
    
    # 마지막 지점에 도착했다면
    elif i == N-1 and j == N-1:
        # 그 지점의 값을 더하고, 최소값보다 작다면 갱신
        temp_sum += arr[i][j]
        if min_sum > temp_sum:
            min_sum = temp_sum
    
    # 각각 아래, 오른쪽으로 이동, 합계를 더함
    findMin(i+1, j, temp_sum+arr[i][j], N)
    findMin(i, j+1, temp_sum+arr[i][j], N)
    


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 임의의 큰 숫자
    min_sum = 2**31-1

    # 재귀함수 시작
    findMin(0, 0, 0, N)
    print(f'#{testcase} {min_sum}')