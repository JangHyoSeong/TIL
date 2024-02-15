import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    q = [0] * (N+1)
    front = rear = 0

    for i in numbers:
        rear = (rear+1)%(N+1)
        q[rear] = i

    for i in range(M+1):
        front = (front+1)%(N+1)
        rear = (rear+1)%(N+1)
        q[rear] = q[front]

    print(f'#{testcase} {q[front]}')