import sys
sys.stdin = open('input.txt')

T = int(input())

def insert(n):
    # 힙에 값을 삽입    
    global last
    last += 1
    heap[last] = n    

    c = last    
    p = c//2
    # 부모가 존재하고, 부모가 자식보다 크다면 교환
    while p >= 1 and heap[p]>heap[c]:         
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

for testcase in range(1, T+1):
    N = int(input())

    values = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for value in values:
        insert(value)

    result = 0
    while last >= 1:
        last //= 2
        result += heap[last]
        

    print(f'#{testcase} {result}')