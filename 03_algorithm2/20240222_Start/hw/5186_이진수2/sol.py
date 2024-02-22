import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    num = float(input())

    # 결과로 사용할 문자열
    bin = ''
    
    # 12번 반복, 이진수 변환을 완료한다면 break로 탈출
    for i in range(12):

        # 이진수 계산을 위한 자릿수 설정
        temp = 2 ** (-i-1)

        # 이진수 변환
        if num - temp >= 0:
            bin += '1'
            num -= temp
        else:
            bin += '0'

        # 변환이 끝났다면 종료
        if num == 0.0:
            break

    # 12번 반복동안 이진수로 변환하지 못했다면 overflow 출력
    else:
        bin = 'overflow'


    print(f'#{testcase} {bin}')