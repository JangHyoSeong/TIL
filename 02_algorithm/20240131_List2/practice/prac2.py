

def f(arr, N):

    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += my_set[j]
                if s == 0:
                    return True
    return False



my_set = list(map(int, input().split()))
N = len(my_set)

print(f(my_set, N))