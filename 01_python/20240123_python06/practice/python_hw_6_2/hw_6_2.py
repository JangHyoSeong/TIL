# 아래 함수를 수정하시오.
def remove_duplicates_to_set(my_list):
    for idx, c in enumerate(my_list):
        if my_list.count(c) > 1:
            my_list.remove(c)

    return set(my_list)  


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
