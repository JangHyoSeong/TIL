import sys

sys.stdin = open('input.txt')

t = int(input())

for i in range(t):
    length = int(input())
    target = input().split('0')
    target_list = list(map(len, target))
    print(f"#{i + 1} {max(target_list)}")