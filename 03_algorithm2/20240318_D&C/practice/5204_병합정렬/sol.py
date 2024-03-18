import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    # mergesort에서 분할 작업을 진행하는 함수
    arr_len = len(arr)

    # 분할이 전부 완료되었다면 그대로 리턴
    if arr_len == 1: return arr

    # 왼쪽, 오른쪽 리스트로 분할
    left_arr, right_arr = arr[:arr_len//2], arr[arr_len//2:]

    # 왼쪽, 오른쪽을 재귀적으로 호출하며 계속 분할함 (쪼갤 수 없을 때까지)
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # 끝까지 분할됐다면 병합을 실행
    # 결국 병합된 리스트끼리 계속 병합 -> 원본 리스트의 크기가 될 때까지 실행
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    # 정답으로 사용할 cnt변수를 전역변수로 사용
    global cnt
    # 문제의 조건에 맞다면 cnt증가
    if left_arr[-1] > right_arr[-1]:
        cnt += 1
    
    # 왼쪽, 오른쪽 리스트의 길이를 미리 구함
    left_len = len(left_arr)
    right_len = len(right_arr)
    
    # 결과로 사용할 리스트를 선언
    result = [0] * (left_len + right_len)

    # 왼쪽, 오른쪽, 결과 리스트의 인덱스 설정
    left_idx, right_idx, result_idx = 0, 0, 0

    # 인덱스의 리스트가 인덱스의 길이보다 작을 때까지 반복
    # -> 왼쪽, 오른쪽 리스트의 값을 전부 결과에 넣을 때까지
    while left_idx < left_len or right_idx < right_len:
        # 만약 두 리스트에 값이 남아있다면
        if left_idx < left_len and right_idx < right_len:
            # 크기를 비교하여 결과 리스트에 삽입
            if left_arr[left_idx] <= right_arr[right_idx]:
                result[result_idx] = left_arr[left_idx]
                left_idx += 1
                result_idx += 1
            else:
                result[result_idx] = right_arr[right_idx]
                right_idx += 1
                result_idx += 1

        # 둘 중 하나의 리스트에만 값이 남아있다면
        # 바로 결과 리스트에 삽입
        elif right_idx < right_len:
            result[result_idx] = right_arr[right_idx]
            right_idx += 1
            result_idx += 1
        elif left_idx < left_len:
            result[result_idx] = left_arr[left_idx]
            left_idx += 1
            result_idx += 1

    return result



T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result_arr = merge_sort(arr)

    print(f'#{testcase} {result_arr[N//2]} {cnt}')