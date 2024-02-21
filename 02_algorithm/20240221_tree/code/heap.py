# 힙의 삽입 연산

def insert(n):
    # 마지막 노드 추가(완전이진트리 유지)
    global last
    last += 1
    h[last] = n     # 마지막 노드에 데이터 삽입

    c = last    # 부모 > 자식 비교를 위해
    p = c//2    # 부모 번호
    while p >= 1 and h[p]<h[c]:         # 부모가 존재하고, 부모가 더 작으면 교환
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2



def delete():
    # 삭제
    global last
    temp = h[1]  # 루트의 키 값 임시저장
    h[1] = h[last]
    last -= 1
    p = 1       # 새로 옮긴 루트
    c = p*2

    while c<=last:
        if c+1 <= last and h[c] < h[c+1]:   # 오른쪽 자식이 있고, 더 크면
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break


N = 10      # 노드 수
h = [0] * (N+1) # 최대힙
last = 0        # 힙의 마지막 노드 번호

insert(2)
insert(5)
insert(3)
insert(6)
insert(4)

print(h)