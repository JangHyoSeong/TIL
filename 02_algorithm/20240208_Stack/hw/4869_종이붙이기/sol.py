import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    # 재귀함수로 푸니까 시간제한 걸려서 동적 프로그래밍으로 계산
    # 범위만큼 리스트 생성
    result = [0] * (N//10)

    # 10인 경우 경우의수는 1, 20인경우 경우의수는 3
    result[0] = 1
    result[1] = 3

    # 30인 경우 10인 경우의 수 *2 + 20인 경우의 수이다
    for i in range(2, N//10):
        result[i] += result[i-1]
        result[i] += result[i-2] * 2

    
    print(f'#{testcase} {result[-1]}')