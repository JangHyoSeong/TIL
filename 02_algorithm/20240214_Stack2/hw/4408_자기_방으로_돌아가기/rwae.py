import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    moves = [list(map(int, input().split())) for _ in range(N)]
    
    # 각 방에 대한 도착 예상 시간을 저장할 리스트
    arrival_times = [0] * 401
    
    # 각 학생의 이동 경로를 반복하면서 도착 예상 시간을 갱신
    for move in moves:
        start, end = move
        if start > end:  # 시작 위치가 더 뒤에 있는 경우, 시작과 끝 위치를 바꿔줌
            start, end = end, start
        
        # 해당 시작 위치에서 도착 위치까지 이동하는데 필요한 시간 갱신
        for i in range(start, end+1):
            arrival_times[i] += 1

    # 가장 늦게 도착하는 학생의 도착 예상 시간을 최대 이동 시간으로 설정
    max_time = max(arrival_times)
    
    print(f'#{testcase} {max_time}')
