# 데코레이터로 사용할 함수 (인자 : 함수)
def my_decorator(func):
  def wrapper():
    # 함수 실행 전에 수행할 작업
    print('함수 실행 전')
    # 원본 함수 호출
    result = func()
    # 함수 실행 후에 수행할 작업
    print('함수 실행 후')
    return result
  return wrapper

# 데코레이터 적용
@my_decorator
def my_function():
  print('원본함수실행')

my_function()

'''
함수 실행 전
원본 함수 실행
함수 실행 후
'''