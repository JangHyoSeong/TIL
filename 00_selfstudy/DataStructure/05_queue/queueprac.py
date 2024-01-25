# list로 queue 구현하기

my_queue = list()

for i in range(1, 11):
    my_queue.append(i)     # 값 삽입

for i in range(10):
    print(my_queue.pop(0)) # 0번 인덱스를 pop하면 queue 구현

# queue 라이브러리 사용
import queue

# 일반 queue
my_queue = queue.Queue()
my_queue.put(0) # 값 삽입
my_queue.get()  # 값 추출
my_queue.qsize() # 크기

# LifoQueue()
# 선입선출 구조, 사실상 스택

my_queue = queue.LifoQueue()

# PriorityQueue()
# d우선순위가 있는 큐, 우선순위가 가장 큰 요소를 먼저 제거
my_queue = queue.PriorityQueue()
my_queue.put((5,0))
my_queue.put((10,7))
print(my_queue.get())
