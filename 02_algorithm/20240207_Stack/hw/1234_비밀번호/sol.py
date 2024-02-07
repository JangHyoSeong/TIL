import sys

class Stack:
    
    def __init__(self, size):
    # 스택을 정의할 때는 스택의 크기를 지정해야함(MAX_SIZE)
        self.size = size
        self.data = [None] * size   # None으로 스택을 채움
        self.top = -1   # top의 위치는 -1(없음)로 초기화

    def __str__(self):
        # instance print했을 때, stack안의 data를 바로 출력
        return f'{self.data}'


    def push(self, item):
        if self.isFull():
            print('Stack is full')
            return None
        # 인자로 스택에 넣을 값을 받음
        # 스택이 None으로 초기화되어있기에 append는 사용하면안됨
        self.top += 1
        self.data[self.top] = item

    def get(self):
        # top에 있는 데이터 리턴
        return self.data[self.top]

    def pop(self):
        # 스택이 비어있는 경우
        if self.isEmpty():
            print('Stack is empty')
            return None
        # pop 한 위치는 굳이 초기화하지 않아도 됨
        # 덮어쓰일 예정
        self.top -= 1
        return self.data[self.top +1]
    
    def isEmpty(self):
        # 스택이 비어있으면 True, 아니라면 False 반환
        return self.top == -1
    
    def isFull(self):
        # 스택이 전부 찼다면 True, 아니라면 False
        return self.top + 1 == self.size

sys.stdin = open('input.txt')

for testcase in range(1, 11):
    password_len, password = map(int, input().split())

    # 스택의 최대크기를 비밀번호의 길이만큼 설정 후 생성
    stack = Stack(password_len)

    # 비밀번호의 뒤에서부터 각 자리수를 스택에 넣음
    # 따라서 비밀번호가 0이 될때까지 반복
    while password != 0:

        # 스택이 비어있다면, 비밀번호의 마지막글자를 스택에 삽입
        if stack.isEmpty():
            stack.push(password%10)
            password //= 10 # 스택에 삽입한 비밀번호 자릿수는 삭제

        # 스택이 비어있지 않다면 스택에 top에 있는 값과 현재 비밀번호 마지막 값을 비교
        # 실질적으로는 연속된 숫자를 비교하는 것
        else:
            # 스택의 top과 비밀번호의 마지막숫자가 같지않다면 스택에 삽입
            if stack.get() != password%10:
                stack.push(password%10)
                password //= 10
            
            # 스택의 top과 비밀번호의 마지막 숫자가 있다면, pop
            # 이로써 연속된 숫자가 지워지는 효과
            else:
                stack.pop()
                password //= 10

    # 나머지 스택에 저장되어있는 값은 사라지지않은 값
    while not stack.isEmpty():
        password = password * 10 + stack.pop()

    print(f'#{testcase} {password}')