class Queue:

    def __init__(self, maxsize):
        self.size = maxsize
        self.items = [None] * maxsize
        self.rear = 0
        self.front = 0

    def enQueue(self, item):
        if self.isFull():
            print('Queue is full')
        else:
            self.rear  =(self.rear + 1) % self.size
            self.items[self.rear]  = item

    def deQueue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            self.front = (self.front + 1) % self.size
            return self.items[self.front]
    
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear+1) % self.size == self.front
    

q = Queue(3)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
print(q.items)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.items)