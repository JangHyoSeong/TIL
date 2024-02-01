import sys
sys.stdin = open('input.txt')

# 이진 탐색 함수 정의
def binarySearch(length, key):
    count = 0       # 카운트 변수
    start = 1       # 시작점 정의
    end = length    # 끝 정의

    # 이진 탐색 시작
    while start <= end:

        # 중간점
        middle = (start + end) // 2

        # 찾았다면 count 리턴
        if middle == key:
            return count
        
        # 중간이 찾는 값보다 작다면 start를 중간 뒤로 옮김
        elif middle < key:
            start = middle
        
        # 중간이 찾는 값보다 크다면 end를 중간 앞으로 옮김
        elif middle > key:
            end = middle
        count += 1

    return count
        
T = int(input())

for testcase in range(1, T+1):

    page, a, b = map(int, input().split())


    a_count = binarySearch(page, a)
    b_count = binarySearch(page, b)

    if a_count < b_count:
        print(f'#{testcase} A')
    elif a_count > b_count:
        print(f'#{testcase} B')
    else:
        print(f'#{testcase} 0')