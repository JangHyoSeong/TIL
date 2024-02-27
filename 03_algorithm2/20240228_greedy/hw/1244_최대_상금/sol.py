import sys
sys.stdin = open('input.txt')

def change(number, i, j):

    str_num = str(number)
    a = int(str_num[-i])
    b = int(str_num[-j])

    new_num = number - a * 10**(i-1) + b * 10**(i-1) + a * 10**(j-1) - b * 10**(j-1)

    return new_num

def shuffle(count, number):
    global max_number

    if count == change_count:
        if max_number < number:
            max_number = number

    else:
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                shuffle(count+1, change(number, i, j))





T = int(input())

for testcase in range(1, T+1):
    board, change_count = map(int, input().split())
    str_board = str(board)

    N = len(str_board)

    max_number = 0

    shuffle(0, board)

    print(f'#{testcase} {max_number}')

