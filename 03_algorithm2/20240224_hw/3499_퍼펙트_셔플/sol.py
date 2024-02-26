import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    card = list(input().split())

    shuffle = []

    if N%2:
        for i in range(0, N//2 + 1):
            shuffle.append(card[i])
            if i + N//2 + 1 < N:
                shuffle.append(card[i + N//2 + 1])


    else:
        for i in range(0, N//2):
            shuffle.append(card[i])
            shuffle.append(card[i + N//2])

    print(f'#{testcase} {" ".join(shuffle)}')
        