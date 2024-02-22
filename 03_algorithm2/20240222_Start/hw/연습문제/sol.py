N = 5

arr = [[0] * 7 for _ in range(2)]
for i in range(4):
    arr[0][i] = N+i
    arr[1][-i-1] = N-i

print(arr)
