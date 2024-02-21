import sys
sys.stdin = open('input.txt')

encode = {[3, 2, 1, 1] : 0,
          [2, 2, 2, 1] : 1,
          [2, 1, 2, 2] : 2,
          [1, 4, 1, 1] : 3,
          [1, 1, 3, 2] : 4,
          [1, 2, 3, 1] : 5,
          [1, 1, 1, 4] : 6,
          [1, 3, 1, 2] : 7,
          [1, 2, 1, 3] : 8,
          [3, 1, 1, 2] : 9
          }

binary = {'1' : '0001',
          '2' : '0010',
          '3' : '0011',
          '4' : '0100',
          '5' : '0101',
          '6' : '0110',
          '7' : '0111',
          '8' : '1000',
          '9' : '1001',
          'A' : '1010',
          'B' : '1011',
          'C' : '1100',
          'D' : '1101',
          'E' : '1110',
          'F' : '1111'
          }



T = int(input())

for testcase in range(1, T+1):

    N, M = map(int, input().split())
    raw_data = [list(input()) for _ in range(N)]

    for i in range(N):
        code = []
        for j in range(M-1, -1, -1):

            if raw_data[i][j] != '0':
                code += [binary[raw_data]]