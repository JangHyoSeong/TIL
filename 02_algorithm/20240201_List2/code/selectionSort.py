def selectionSort(arr, n):

    # 구간의 시작을 i로 둠.
    # 마지막 원소는 정렬 후 가장 큰 원소일테니 비교하지 않아도 됨
    for i in range(n-1):
        minIdx = i          # 가장 첫 값을 min값으로 초기화
        for j in range(i+1, n):
            if arr[minIdx] > arr[j]:    # 최소값을 만나면 갱신
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]