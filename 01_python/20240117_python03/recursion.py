def factorial(n):
#    종료 조건:    n이 0이면 1을 반환
    if n == 0:
        return 1
#    재귀 호출:    n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

#    팩토리얼 계산 예시
result = factorial(5)


def factorial2(n):
    result = 1
    while n > 0:
        result *= n
        n-=1
    return result

print(factorial2(5))

def factorial3(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

print(factorial3(6))

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(2))

def fibo2(n):
    result = 0
    for i in n:
        pass