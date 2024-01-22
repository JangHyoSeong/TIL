# 아래 함수를 수정하시오.
def remove_duplicates(old_lst):
    new_lst = old_lst[0:]
    for idx, num in enumerate(new_lst):
        if new_lst.count(num) != 1:
            new_lst.pop(idx)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
