numbers = [1, 2, 3, 4, 5]

def func(x):
    return x**2

result = list(map(func, numbers))
print(result)

result = list(map(lambda x : x**2, numbers))
print(result)