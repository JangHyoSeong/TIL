my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.

for key in my_set:
    print(my_dict.get(key))

var = 'dict의 키로 사용한 자료형'
my_dict[var] = '변수로도 키 설정 가능'
print(my_dict)