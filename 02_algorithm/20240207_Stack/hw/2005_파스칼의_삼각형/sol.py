import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    height = int(input())

    # 1층은 직접 정의
    # 2차원 리스트의 형식으로 파스칼의 삼각형을 만듦
    pascal = [[1]]

    # 입력받은 높이만큼 반복
    for i in range(1, height):

        # 파스칼 삼각형의 한 줄이 될 리스트
        line = []

        # 맨앞과 맨뒤라면 1을 삽입
        # 아닌 경우 주어진 조건에 맞게 값을 삽입
        for j in range(0, i+1):
            if j > 0 and j < i:
                line.append(pascal[i-1][j-1] + pascal[i-1][j])
            elif j == 0:
                line.append(1)
            elif j == i:
                line.append(1)

        # 삼각형 한 줄을 삽입
        pascal.append(line)

    print(f'#{testcase}')
    for i in pascal:
        for j in i:
            print(j, end=' ')
        print()