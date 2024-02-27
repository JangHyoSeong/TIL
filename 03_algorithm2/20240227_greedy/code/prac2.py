'''
0 1 2 3 4 5 5 4 3 2 1 0을 재귀호출하여 구현한다
'''

def f(x):
    if x == 6:
        return
    print(x, end= ' ')
    f(x+1)
    print(x, end= ' ')
    
    
f(0)