import sys
sys.stdin = open('input.txt')

decode = {(3, 2, 1, 1) : 0,
          (2, 2, 2, 1) : 1,
          (2, 1, 2, 2) : 2,
          (1, 4, 1, 1) : 3,
          (1, 1, 3, 2) : 4,
          (1, 2, 3, 1) : 5,
          (1, 1, 1, 4) : 6,
          (1, 3, 1, 2) : 7,
          (1, 2, 1, 3) : 8,
          (3, 1, 1, 2) : 9
          }


def verify(password):

    code = 0
    for i in range(0, 7, 2):
        code += password[i] * 3
        code += password[i+1]

    if code % 10 == 0:
        return True
    else:
        return False

T = int(input())

for testcase in range(1, T+1):

    
    N, M = map(int, input().split())
    raw_data = [input() for _ in range(N)]
    binary_data = []


    for i in range(N):
        binary_line = ''
        for j in range(M):
            binary_line += bin(int(f'{raw_data[i][j]}', base=16))[2:].zfill(4)
        
        if binary_line not in binary_data and binary_line.strip('0') != '':
            binary_data.append(binary_line)

    length = len(binary_data)
    

    password = []
    result = 0


    for i in range(length):
        
        now = 0
        count = 0
        change = 0
        word_idx = 8
        flag = False

        code = [0] * 8
        one_word = [0] * 4

        for j in range(4*M-1, -1, -1):

            if i > 0 and binary_data[i][j] == binary_data[i-1][j]:
                continue
            if flag == False:
                if int(binary_data[i][j]) == 0:
                    continue
                else:
                    if i < length-1 and binary_data[i][j] == binary_data[i+1][j]:
                        continue
                    else:
                        flag = True
                        now = 1
                        count += 1
                        change += 1

            else:
                if now == int(binary_data[i][j]):
                    count += 1
                else:
                    one_word[4-change] = count
                    change += 1
                    now = (now+1) % 2
                    count = 1

            if change == 4 and word_idx == 1:
                flag = False
                count = 0
                num = 0
                change = 0

                for k in range(4):
                    one_word[k] //= ratio
                one_word[0] = 7 - one_word[1] -one_word[2] -one_word[3]
                code[word_idx-1] = decode[tuple(one_word)]
                word_idx = 8
                if code not in password:
                    password.append(code)
                

            elif change == 5:
                count = 1
                num = 1
                change = 1

                ratio = min(one_word)
                for k in range(4):
                    one_word[k] //= ratio
                print(code)
                code[word_idx-1] = decode[tuple(one_word)]
                word_idx -= 1

    for num in password:
        if verify(num):
            result += sum(num)
    
    print(f'#{testcase} {result}')