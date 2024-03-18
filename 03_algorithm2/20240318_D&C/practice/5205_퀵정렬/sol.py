import sys
sys.stdin = open('input.txt')

def quickSort(arr):
    # 퀵 소트 함수
    arr_len = len(arr)

    # 더이상 분할이 되지 않으면 그대로 리턴
    if arr_len <= 1:
        return arr

    # pivot은 가운데 값으로 정함
    pivot = arr[arr_len//2]

    # pivot보다 작은, 같은, 큰 리스트를 정의
    left_arr = [x for x in arr if x < pivot]
    mid_arr = [x for x in arr if x == pivot]
    right_arr = [x for x in arr if x > pivot]

    # 왼쪽, 오른쪽 리스트에 대해서 다시 퀵소트 진행
    # 분할이 되지 않을때까지 반복하면서 정렬이 될 것
    return quickSort(left_arr) + mid_arr + quickSort(right_arr)


T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = quickSort(arr)

    print(f'#{testcase} {arr[N//2]}')