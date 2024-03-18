def merge_sort(arr):
    # 분할 과정
    arr_len = len(arr)
    if arr_len == 1: return arr


    left_arr, right_arr = arr[:arr_len//2], arr[arr_len//2:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    # 병합 과정
    result = []

    while len(left_arr) > 0 or len(right_arr) > 0:
        if len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] <= right_arr[0]:
                result.append(left_arr.pop(0))
            else:
                result.append(right_arr.pop(0))

        elif len(right_arr) > 0:
            result.append(right_arr.pop(0))
        elif len(left_arr) > 0:
            result.append(left_arr.pop(0))

    return result