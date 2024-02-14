import sys
sys.stdin = open('input.txt')

def divide(start, end):


    # end - start == 1이라면 => 더이상 쪼갤 수 없다면
    if end - start == 1:
        return start
    
    # 2명 이상인 경우에 대해 분할 후 가위바위보 수행
    else:

        # 가운데 수, 왼쪽 오른쪽을 나누기 위해 사용
        mid = (start + end + 1) // 2

        # 왼쪽 승자를 구함
        # 쪼갤 수 있다면 계속 학생수를 쪼갬
        # 끝까지 쪼개서 1명이 되었다면 left변수에 저장됨
        # 오른쪽도 동일한 방식
        left = divide(start, mid)
        right = divide(mid, end)


        # 끝까지 쪼개진 left와 right가 가위바위보를 함
        return RPS(left, right)
            
             
def RPS(a, b):
# 가위바위보 진행
    if students[a] == 1:
        if students[b] == 2:
            return b
        else:
            return a
        
    elif students[a] == 2:
        if students[b] == 3:
            return b
        else:
            return a
        
    elif students[a] == 3:
        if students[b] == 1:
            return b
        else:
            return a


T = int(input())

for testcase in range(1, T+1):

    N = int(input())
    students = list(map(int, input().split()))

    # divide 함수의 인자는 배열의 시작점과 끝점(길이)을 받음
    winner = divide(0, N)

    print(f'#{testcase} {winner + 1}')