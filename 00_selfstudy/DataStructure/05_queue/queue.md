# 큐(queue)

## 큐의 정의
- 큐는 여러 개의 데이터를 관리하는 자료 구조로 데이터를 넣는 연산인enqueue와 빼는 연산인 dequeue를 제공한다. 단, 데이터를 가져올 때는 들어간 순서대로, 즉 FIFO(First In First Out) 방식으로 데이터가 나온다

## 큐의 ADT (Abstract Data Type)
- 데이터 타입 : struct Queue;
- 연산자
  - void initQueue (struct Queue *queue): 큐 queue를 초기화
  - void enqueue (struct Queue *queue, Data data): 데이터 data를 큐에 넣기
  - Data deQueue (struct Queue *queue): 제일 처음에 있는 데이터 리턴
  - int getSize (struct Queue *queue): 현재 큐에 있는 데이터의 개수를 리턴