arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 배열을 우선 정렬
arr.sort()

def binarySearch(target):

    # 가장 왼쪽, 오른쪽 인덱스 구하기
    low = 0
    high = len(arr) - 1

    # 해당 숫자를 찾거나 쪼갤 수 없는 상황이면 종료
    while low <= high:
        mid = (low + high) // 2

        # 찾았다면 인덱스 반환
        if arr[mid] == target:
            return mid
        
        # 가운데 값이 target보다 크다면
        # 왼쪽에 값이 있다 -> high를 mid보다 하나 작은 값으로 설정
        elif arr[mid] > target:
            high = mid - 1

        # 가운데 값이 target보다 작다면
        # 오른쪽에 값이 있다. -> high를 mid보다 하나 큰 값으로 설정
        else:
            low = mid + 1

    return -1

print(binarySearch(32))

#################################################################

# 재귀 함수를 사용
def binarySearch(low, high, target):
    
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if target == arr[mid]:
        return mid
    
    elif arr[mid] < target:
        binarySearch(low, mid-1, target)
    else:
        binarySearch(mid+1, high, target)
    