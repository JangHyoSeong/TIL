import sys
sys.stdin = open('input.txt')

def change(number, i, j):
    # 숫자를 섞는 함수
    # i, j번째 숫자를 섞고 섞인 숫자를 리턴
    str_num = str(number)
    a = int(str_num[-i])
    b = int(str_num[-j])

    new_num = number - a * 10**(i-1) + b * 10**(i-1) + a * 10**(j-1) - b * 10**(j-1)

    return new_num

def shuffle(count, number):
    # 재귀적으로 호출하면서 섞었을 때 최대값을 찾음
    global max_number

    # 정해진 횟수만큼 섞었다면, 최대값을 비교, 갱신
    if count == change_count:
        if max_number < number:
            max_number = number

    # 아직 정해진 횟수만큼 섞지 않았다면
    else:
        # 자릿수만큼 두번 순회하면서 섞어줌
        for i in range(1, N+1):
            for j in range(1, N+1):
                # 같은 자릿수일때는 넘어감
                if i == j:
                    continue

                # i, j번째 숫자를 섞음
                new_number = change(number, i, j)

                # 0이 앞으로 가서 숫자가 작아지는 경우 제외
                if len(str(new_number)) == N:

                    # 실행되는 횟수를 줄이기 위해 이미 진행한 작업이라면 실행하지않음
                    if (count+1, new_number) not in valid:
                        # 현재 횟수와 숫자 상태를 valid라는 리스트에 튜플로 집어넣음
                        # 이를 통해 중복적인 실행 방지
                        valid.append((count+1, new_number))
                        # 재귀적으로 호출하면서 다음 단계로 이동
                        shuffle(count+1, new_number)


T = int(input())

for testcase in range(1, T+1):
    board, change_count = map(int, input().split())
    str_board = str(board)

    # 숫자의 길이
    N = len(str_board)

    # 중복적인 실행을 방지하기 위해 필요한 리스트
    valid = []
    # 전역변수로 사용할 max값
    max_number = 0

    # 함수 시작
    shuffle(0, board)

    print(f'#{testcase} {max_number}')