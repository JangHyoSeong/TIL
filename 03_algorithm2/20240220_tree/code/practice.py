'''
input
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder (T):
    if T:
        print(T)
        preorder(left[T])
        preorder(right[T])

N = int(input())    # 정점의 개수
E = N - 1           # 간선의 개수
arr = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:  # 부모가 있으면
    c = par[c]      # 부모를 새로운 자식으로 둠
root = c            # 부모가 없다면 root

print(root)
preorder(root)