inputValue = '1 2 3 4 5'

numbers = inputValue.split()
print(numbers)
#이러면 그냥 ['1', '2', '3', '4', '5']임 (문자)

variable = list(map(int, inputValue.split()))
#inputValue를 .split()으로 하나씩 쪼갠다
#그 후 map의 매개변수로 int 함수(정수로 형변환)을 넣어주어 문자열을 정수로 바꿈

a, b, c, d, e = list(map(int, inputValue.split()))
print(a, b, c, d, e)

print(variable)