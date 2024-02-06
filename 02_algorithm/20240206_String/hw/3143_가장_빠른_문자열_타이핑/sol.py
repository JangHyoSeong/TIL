import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    A, B = input().split()

    len_A = len(A)
    len_B = len(B)
    count = 0

    while A.find(B) != -1:
        count += 1
        A = A.replace(B, '', 1)

    typing = len_A - count * (len_B - 1)
    print(f'#{testcase} {typing}')