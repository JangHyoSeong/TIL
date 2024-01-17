my_list = ['가', '나', '다', '라', '마']

print(my_list[2:4])        #다 라
print(my_list[:3])         #가 나 다
print(my_list[3:])         #라 마
print(my_list[0:5:2])      #가 다 마
print(my_list[::-1])       #마 라 다 나 가

print(my_list[:100])       #슬라이싱으로는 인덱스 오류가 발생하지 않음, 하지만 예외처리가 되지 않아서 예상치 못한 상황 발생 가능. 가능하면 제대로 쓰자