import sys
sys.stdin = open('input.txt')

T = int(input())

def insert(n):
    # 힙에 값을 삽입

    # 현재 힙의 인덱스를 전역변수로 사용
    global last

    # 값을 하나 삽입하니까 +1
    last += 1
    # 현재 인덱스에 일단 값을 삽입
    heap[last] = n    

    # 자식 인덱스 저장
    child_idx = last
    # 이진 힙에서 부모인덱스는 항상 자식인덱스의 // 2
    parent_idx = child_idx//2


    # 부모노드가 존재하고, 부모가 자식보다 크다면 교환
    while parent_idx >= 1 and heap[parent_idx]>heap[child_idx]:         
        heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx]

        # 부모, 자식의 값이 바뀐 후, 바뀐 값을 그 부모와 다시 비교해야함
        # 부모노드가 존재하지 않거나(root노드), 부모가 자식보다 작을때까지 반복
        child_idx = parent_idx
        parent_idx = child_idx//2

for testcase in range(1, T+1):

    # 값을 받아옴
    N = int(input())
    values = list(map(int, input().split()))

    # 노드의 개수는 N개. 인덱싱을 편하게 하기위해 크기를 N+1로 둠.
    # root노드의 인덱스는 1
    heap = [0] * (N+1)

    # 현재 이진힙의 가장 마지막 인덱스
    last = 0

    # 문제의 조건 : 입력 순서대로 이진 최소힙에 저장
    for value in values:
        insert(value)

    # 결과로 쓸 변수
    result = 0

    # root 노드에 닿을 때까지
    while last >= 1:
        
        # 자신의 부모노드로 이동
        last //= 2
        result += heap[last]
        

    print(f'#{testcase} {result}')