import sys
sys.stdin = open('input.txt')

T = int(input())

def hexToBin(num):
    # 16진수로 표현된 문자 1개를 2진수로 표현하는 함수

    # 2진수로 표현된 숫자를 담을 리스트
    binary = []
    # 16진수를 10진수로 변환
    int_num = int(num, 16)

    # 16진수 한 글자를 2진수로 표현하면 4자리 수가 됨
    for _ in range(4):

        # 2진수 변환
        binary.append(str(int_num % 2))
        int_num //= 2

    # 기존의 binary는 순서가 역순이다
    return ''.join(reversed(binary))


for testcase in range(1, T+1):
    N, number = input().split()

    binary = []
    for c in number:
        binary.append(hexToBin(c))

    print(f'#{testcase} {"".join(binary)}')
