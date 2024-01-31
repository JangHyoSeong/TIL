import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    
    size_of_puzzle, len_of_word = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(size_of_puzzle)]


    count = 0

    # 일단 가로의 경우먼저 계산
    for i in range(size_of_puzzle):

        # IndexError를 막기 위해 범위를 설정
        for j in range(size_of_puzzle - len_of_word + 1):

            # 빈칸이 3개인 구간만 찾기위해 temp_word_len변수로 빈칸 길이를 측정
            temp_word_len = 0

            # 왼쪽이 빈칸으로 시작한다면, 계산에 오류가 생기기때문에 무시
            if j > 0 and puzzle[i][j-1] == 1:
                continue

            # 오른쪽으로 계속 빈칸이라면 빈칸의 길이를 계산
            while puzzle[i][j + temp_word_len] == 1:
                temp_word_len += 1

                # 인덱스의 끝에 닿으면 break로 빠져나감
                if j + temp_word_len > size_of_puzzle - 1:
                    break

            # 빈칸의 길이가 입력받은 길이와 같다면 카운트를 하나 올림
            if temp_word_len == len_of_word:
                count += 1
            

    # 세로의 경우
    for i in range(size_of_puzzle - len_of_word + 1):
        for j in range(size_of_puzzle):

            temp_word_len = 0
            if i > 0 and puzzle[i-1][j] == 1:
                continue

            while puzzle[i + temp_word_len][j] == 1:
                temp_word_len += 1
                if i + temp_word_len > size_of_puzzle - 1:
                    break

            if temp_word_len == len_of_word:
                count += 1

    print(f'#{testcase} {count}')