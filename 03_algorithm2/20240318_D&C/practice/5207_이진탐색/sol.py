import sys
sys.stdin = open('input.txt')

# 알아보기 쉽게 정의해둔 변수
LEFT = 0
RIGHT = 1

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))

    # 이진 탐색을 위해서는 반드시 정렬되어야 한다
    arr_A.sort()
    # 정답을 세기 위한 변수
    cnt = 0

    # arr_B를 순회하면서 조건에 맞는 숫자의 개수를 구함
    for num in arr_B:

        # 이진 탐색을 할 범위
        low, high = 0, N-1

        # 현재 숫자가 이진 탐색에서 어느 방향에 있는지를 담을 리스트
        dir = []

        # 이진 탐색의 성공 여부를 기록할 flag
        flag = False

        # 이진 탐색 시작, low가 high보다 작거나 같은 경우 반복
        while low <= high:

            # 중간값
            mid = (low + high) // 2

            # 만약 찾는 수가 중간에 존재한다면
            # flag를 True로 바꾸고 탐색 종료
            if num == arr_A[mid]:
                flag = True
                break
            
            # 만약 찾는 수가 중간 값보다 작다면 -> 왼쪽에 존재한다면
            elif num < arr_A[mid]:
                # dir 리스트에 왼쪽 추가
                dir.append(LEFT)
                # high의 인덱스를 중간보다 하나 작게 수정
                high = mid - 1
            
            # 찾는 수가 중간 값보다 크다면 -> 오른쪽에 존재한다면
            else:
                # dir 리스트에 오른쪽 추가
                dir.append(RIGHT)
                # low의 인덱스를 중간보다 하나 크게 수정
                low = mid + 1
        
        # 이진 탐색이 성공한 경우에만
        if flag:

            # dir을 순회하하면서, 연속된 값이 나온다면 break
            for i in range(len(dir)-1):
                if dir[i] == dir[i+1]:
                    break
            # break하지 않았다면 count를 하나 증가
            else:
                cnt += 1

    print(f'#{testcase} {cnt}')