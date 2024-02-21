import random

N = 12
M = 5


for i in range(N):
    for j in range(N):
        print(random.randint(1, 30), end=' ')
    print()