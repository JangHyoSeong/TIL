import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in arr:
    for j in i:
        result += j

print(result)