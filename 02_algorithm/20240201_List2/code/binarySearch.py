import random
import time

def binarySearch(a, N, key):
    start = 0
    end = N-1

    while start <= end:         # 검색 구간이 유효하면 반복
        middle = (start + end)//2   # 중앙 원소 인덱스

        if a[middle] == key:        # 검색 성공
            return True
        
        elif a[middle] > key:       # 현재 값이 key보다 크면
            end = middle - 1        # 작은쪽으로 인덱스를 이동

        else:                       # 현재 값이 key보다 작으면
            start = middle + 1        # 큰 쪽으로 인덱스를 이동
    return False

# 재귀함수로 구현
def binarySearch2(a, low, high, key):
    if low > high:
        return False
    
    else:
        middle = (low + high) // 2

        if key == a[middle]:
            return True
        
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        
        elif key > a[middle]:
            return binarySearch2(a, middle+1, high, key)
    

arr = [random.randint(1, 50000) for _ in range(12345678)]
arr.sort()

start = time.time()
print(binarySearch(arr, 12345678, 400))
end = time.time()

print(f'{end - start :.10f} sec')