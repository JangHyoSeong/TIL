'''
중복수열 [1, 1, 1] ~ [6, 6, 6]까지 출력하는 코드를 구현하라
'''

path = []

def f(x):
    if x == 3:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        f(x+1)
        path.pop()

f(0)