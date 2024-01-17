#함수 연습

# 어떤 함수를 정의하는데, 2개의 매개변수를 가진다.
def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2

# 함수를 호출한다
some_func('가', '나')

# 함수를 호출한 결과를 변수에 담아보자
answer = some_func(1, 2)
print(answer)       # None이 출력됨 (why? 값이 없음)

# 리스트는 순서가 있는 값이고, 정렬 되어있음을 보장하지는 않는다.
# 리스트를 오름차순으로 정렬하고 싶다
numbers = [4, 3, 2, 1]
# 메서드 : 누군가가 가지고 있는 함수
# 내장 함수 : 파이썬이 기본적으로 가지고 있는 함수

# 리스트가 갖고있는 sort메서드 사용
result = numbers.sort()
print(result)           #None 출력
print(numbers)
# sort()메서드는 리턴하는 것이 아니라 원래 리스트를 정렬하는것

# 내장함수 sorted() 사용
numbers = [4, 3, 2, 1]

result = (sorted(numbers))  # sorted 함수는 누구를 정렬해줘야하는지 정해줘야 함. 따라서 인자를 넘겨줌
print(result)
print(numbers)

# .sort()는 return이 필요없었음
# sorted()는 return이 필요함

def other_func(parm1, parm2):
    result = parm1 * parm2
    print(result, '함수 내부에서 실행')
    return result

answer = other_func(2, 3)
print('함수 외부에서 실행')

# 이러면 안됨
'''
def sorted(iterable, key=None, reverse=False)
    pass
sorted(list, True)
'''
#answer = sorted(numbers, True)  # 키워드 인자로 안넣으면 머가 먼지 모름
answer = sorted(numbers, reverse=True)
print(answer)


# 이래도 안됨
def other_func(*args, name):
    pass

# other_func(1, 2, 3, 4, 5, 6, 7)   #name에 못주고 앞에서 다먹음
other_func(1, 2, 3, 4, 5, 6, 7, name='흠')  #이건 됨

# LEGB
a = 1
b = 2

def enclosed():
  a = 10
  c = 3

  def local(c): 
    print(a,b,c)  #10 2 500     #local(500)에서 호출되었기 때문

  local(500)  
  print(a,b,c)  #10 2 3

enclosed()
print(a,b)  #1 2

# 자신의 영역(local)에서 부터 시작해서 한 단계씩 찾는 level을 올림


# global 변수 바꾸는 법

globalNum = 100

def local(parm):
   parm += 3
   return parm
   

globalNum = local(globalNum)

# 이렇게 쓰는게 젤 좋다