import sys
sys.stdin = open('input.txt')

def find(lev, start, target):
    # 부분수열 만드는 함수
    global result_sum
    global count

    if lev == N:
        if result_sum == K:
            count += 1
            return
        else:
            return
    elif result_sum == K:
        count += 1
        return
    elif result_sum > K:
        return
    
    else:
        for i in range(start, N):
            result_sum += numbers[i]
            find(lev+1, i+1, target)
            result_sum -= numbers[i]

result_sum = 0

T = int(input())

for testcase in range(1, T+1):

    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0

    find(0, 0, K)

    print(f'#{testcase} {count}')