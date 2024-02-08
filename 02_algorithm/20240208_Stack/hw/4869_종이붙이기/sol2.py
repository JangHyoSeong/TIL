import sys
sys.stdin = open('input.txt')


# 재귀함수로 풀이(시간모자람)
def count_ways(N):
    if N < 20:
        return 1
    elif N == 20:
        return 3
    else:
        return count_ways(N - 10) + count_ways(N - 20) + count_ways(N - 20)


T = int(input())

for testcase in range(1, T+1):
    
    N = int(input())

    print(f'#{testcase} {count_ways(N)}')
