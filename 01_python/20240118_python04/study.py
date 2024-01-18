'''
함수를 정의할 때, 매개변수에 패킹을 사용해서
가변 인자로 받게 되면 튜플로 받는데

왜 변수에 패킹을 사용해서
다수의 데이터를 받으면 리스트로 받는 이유는 뭔가요?
'''

def some_func(*args):
    print(args)         # (1, 2, 3, 4)
    print(type(args))   # <class 'tuple'>

some_func(1, 2, 3, 4)


a, *b, c = [1, 2, 3, 4, 5]
print(b)        # [2, 3, 4]
print(type(b))  # <class 'list'>

'''
왜 이럴까?
tuple
 - 순서가 있는 시퀀스 타입
 - 순회가 가능한 iterable한 데이터
 - 여러개의 데이터를 담을 수 있는 collection
 - 내부 요소를 변경할 수 없는 immutable

list
 - 순서가 있는 시퀀스 타입
 - 순회가 가능한 iterable한 데이터
 - 여러개의 데이터를 담을 수 있는 collection
 - 내부 요소를 변경할 수 있는 mutable

함수의 매개변수 -> tuple
변수 -> list

변수에 값을 할당할 때의 기대값은 특정 데이터를 편하게 참조할 수 있는 기능
해당 데이터의 값을 변경하거나, 조작하거나, 활용하는 용도를 기대

반면 함수는  입력 값에 따른 정확한 출력 값을 기대
항상 같은 입력에 대해 같은 출력을 해야함
따라서 불변 성질을 가진 튜플을 사용
'''

'''
lambda (매개변수) : 함수 작업
 - 코드 재사용 불가능
 - 아주 간단한 로직인데, 순회가능한 어떤 데이터에 대해서
 - 각 요소들에 대해서만 똑같은 로직을 실행해야 할 때
'''
def my_sum(num1, num2):
    return num1 + num2

lambda num1, num2 : num1 + num2

my_sum_lambda = lambda num1, num2 : num1 + num2
result_1 = my_sum_lambda(3, 4)
print(result_1)

a = [1, 2, 3]
b = [4, 5 ,6]
result_2 = list(map(lambda num1, num2 : num1 + num2, a, b))
print(result_2)