# 아래 함수를 수정하시오.
def find_min_max(numbers):
    min = 2**31 - 1
    max = 0

    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number

    return min, max

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)