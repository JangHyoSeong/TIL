import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    time = [list(map(int, input().split())) for _ in range(N)]

    # 종료시간을 기준으로 정렬
    time.sort(key= lambda x : x[1])

    # 종료시간이 가장 빠른 작업을 일단 실행
    count = 1
    # 지금 하는 작업의 종료시간
    lock = time[0][1]
    for i in range(1, N):
        # 지금 작업의 종료시간이 시작시간보다 빠르다면
        if lock <= time[i][0]:
            # 작업을 수행하고 종료시간을 갱신
            count += 1
            lock = time[i][1]

    print(f'#{testcase} {count}')