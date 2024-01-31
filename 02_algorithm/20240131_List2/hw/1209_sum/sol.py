import sys
sys.stdin = open('input.txt')

for testcase in range(1, 11):
    t = int(input())    # 테스트케이스

    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0



    dia_line_sum1 = 0
    dia_line_sum2 = 0
    for i in range(100):
        dia_line_sum1 += numbers[i][i]
        dia_line_sum2 += numbers[99-i][i]

    for i in range(100):
        hor_line_sum = 0
        ver_line_sum = 0

        for j in range(100):
            hor_line_sum += numbers[i][j]
            ver_line_sum += numbers[j][i]

        temp_max = max(hor_line_sum, ver_line_sum)

        if max_sum < temp_max:
            max_sum = temp_max

    if max_sum < dia_line_sum1:
        max_sum = dia_line_sum1

    if max_sum < dia_line_sum2:
        max_sum = dia_line_sum2


    print(f'#{t} {max_sum}')

