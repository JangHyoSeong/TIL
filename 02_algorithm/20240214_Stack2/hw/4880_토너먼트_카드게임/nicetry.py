import sys
sys.stdin = open('input.txt')

def divide(students, N):

    if N == 1:
        return students[0]
    elif N == 2:
        return RPS(students[0], students[1])

    else:
        
        start = 0
        end = N
        mid = (start + end + 1) // 2
        left_students = students[start:mid]
        right_students = students[mid:end]

        while N != 1:
            students = []
            N = (N+1)//2
            students.append(divide(left_students, mid))
            students.append(divide(right_students, end-mid))

        return students[0]
            
             
    
def RPS(a, b):
    if a == 1:
        if b == 2:
            return b
        else:
            return a
        
    elif a == 2:
        if b == 3:
            return b
        else:
            return a
        
    elif a == 3:
        if b == 1:
            return b
        else:
            return a


T = int(input())

for testcase in range(1, T+1):

    N = int(input())
    students = list(map(int, input().split()))

    winner = divide(students, N)

    print(f'#{testcase} {winner}')