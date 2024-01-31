import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 원소의 개수, 부분집합의 합을 입력받음
    num_of_elements, sum_of_subset = map(int, input().split())

    # 1부터 12까지 원소를 가진 집합 A를 정의
    set_A = [i for i in range(1, 13)]
    count = 0

    # 부분집합 찾기, 부분집합의 개수가 2^12개이니 그만큼 반복함
    for i in range(1<<12):

        # 하나의 부분집합을 찾을때마다 초기화
        subset = []

        # 부분집합의 원소를 찾음
        for j in range(12):

            # 각 자릿수(경우의 수)를 순회하며 부분집합의 원소를 골라냄
            if i & 1<<j:
                subset.append(set_A[j])
        
        # 구한 부분집합의 길이가 입력받은 원소의 개수, 입력받은 합이라면 카운트 변수를 1증가함
        if len(subset) == num_of_elements and sum(subset) == sum_of_subset:
            count += 1

    print(f'#{testcase} {count}')