# 재귀함수로 표현

def quickSort(lst):

    if len(lst) <= 1:   # 정렬 대상을 분할할때 더이상 분할할 수 없으면
        return lst

    else:
        pivot = lst[0]  # 퀵 소트 pivot위치를 시작점으로 잡음(크게 상관없음)
        # pivot보다 작은 대상만 모음
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        
        # pivot보다 큰 대상만 모음
        greater_than_pivot = [x for x in lst[1:] if x > pivot]

        # 재귀적으로 호출
        return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)


arr = [3, 6, 8, 10, 1, 2, 1]
N = len(arr)

sorted_arr = quickSort(arr)

print(sorted_arr)