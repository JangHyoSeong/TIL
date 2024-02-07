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