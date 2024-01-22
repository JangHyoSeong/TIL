# 아래 함수를 수정하시오.
def even_elements(old_numbers):

    even_numbers = []
    even_numbers.extend(old_numbers)
    for idx, num in enumerate(even_numbers):
        if num % 2 == 1:
            even_numbers.pop(idx)

    
    return even_numbers





my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
