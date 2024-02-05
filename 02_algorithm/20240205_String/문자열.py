# 문자열 뒤집기

s = 'Reverse this strings'
s = s[::-1]

s = 'abcd'
s = list(s)
s.reverse()
s = ''.join(s)


# is, == 차이점
s1 = 'abc'
s2 = 'abc'
s3 = 'def'

s4 = s1
s5 = s1[:2] + 'c'

print(s1 is s2)
print(s1 == s2)
print(s1 is s3)
print(s1 == s3)
print(s1 is s4) # True
print(s1 == s4) # True
print(s1 is s5) # False 내용은 같지만 위치가 달라서 False
print(s1 == s5) # True

# 문자열 숫자를 정수로 변경
# int()함수가 있긴 함
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i
# ord 함수 : 해당하는 문자의 unicode 를 반환 ex) ord('A') -> 65
# chr() : 정수를 아스키코드의 문자로 변환
s = '123'
a = atoi(s)
print(a+1)