# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
    new_tuple = ()
    temp_lst = list(old_tuple)
    temp_lst.sort()
    new_tuple = tuple(temp_lst)

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
