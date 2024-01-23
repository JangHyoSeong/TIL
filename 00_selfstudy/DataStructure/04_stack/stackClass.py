# 클래스를 사용하여 스택 구현

class Stack:

    def __init__(self):
        self.top = []

    def __len__(self):
        return len(self.top)
    
    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()
    
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("Stack underflow")
            exit()

    def isEmpty(self) -> bool:
        return len(self.top) == 0
    

stack = Stack()

print(len(stack))

stack.push(5)
stack.push(3)
stack.push(1)

print(f'스택 길이 : {len(stack)}')
print(stack.pop())
print(stack.pop())
print(stack.pop())