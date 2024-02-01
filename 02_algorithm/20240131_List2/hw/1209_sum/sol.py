import sys
sys.stdin = open('input.txt')

for testcase in range(1, 11):
    t = int(input())    # 테스트케이스

    # 배열 입력받음
    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0


    # 대각선 합 초기화
    dia_line_sum1 = 0
    dia_line_sum2 = 0

    # 리스트를 대각선으로 순회하면서 대각선 합 구함
    for i in range(100):
        dia_line_sum1 += numbers[i][i]
        dia_line_sum2 += numbers[99-i][i]

    # 2차원 리스트를 순회하며 각 라인의 합을 구함
    for i in range(100):
        hor_line_sum = 0
        ver_line_sum = 0

        for j in range(100):
            hor_line_sum += numbers[i][j]
            ver_line_sum += numbers[j][i]

        # 순회가 한번 끝날때마다 최대값을 갱신함
        temp_max = max(hor_line_sum, ver_line_sum)

        if max_sum < temp_max:
            max_sum = temp_max

    # 마지막으로 대각선과 최대값을 비교
    if max_sum < dia_line_sum1:
        max_sum = dia_line_sum1

    if max_sum < dia_line_sum2:
        max_sum = dia_line_sum2


    print(f'#{t} {max_sum}')

