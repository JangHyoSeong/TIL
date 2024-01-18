my_dict = {'a' : 1}
my_list = []
# my_list[0] = my_dict        #이러면 에러
my_list.append(my_dict)


# 각 문자열을 모두 정수로 바꿔서 리스트에 담으세요
# 반복문을 사용하여

numbers_words = '1 2 3 4 5 6 7 8 9 10'
numbers = []
for char in numbers_words:
    if char != ' ' and char.isnumeric():
        numbers.append(int(char))

print(numbers)

numbers = list(map(int, numbers_words.split()))
print(numbers)


# 이 경우는?
numbers_words = [
    '1 2 3 4 5',
    '6 7 8 9 10',
    '11 12 13 14 15'
]
numbers = []
for words in numbers_words:
    conversion_list = list(map(int, words.split()))
    numbers.append(conversion_list)

print(numbers)

numbers = [1, 2, 3, 4]
numbers = [list(map(int, words.split())) for words in numbers_words]
print(numbers)

numbers = [[0 for _ in range(10)] for i in range(10)]
print(numbers)