# 자료구조 스택

### 스택의 정의
- 스택은 여러 개의 데이터를 관리하는 자료구조로 데이터를 넣는 연산인 push와 빼는 연산인 pop을 제공한다.
- 데이터를 가져올 때는 넣은 순서의 역순으로 가져올 수 있는 자료구조이다.

### 스택의 ADT(Abstract Data Type)
- 데이터 타입 : struct Stack;
- 연산자
  - void initStack(struct Stack *s) : 스택 s를 초기화
  - void push(struct Stack *s, Data data) : 데이터 data를 스택 s에 push
  - Data pop(struct Stack *s) : 제일 마지막에 push한 데이터를 리턴
  - Boolean isEmpty(struct Stack s) : 스택이 비어 있으면 True, 아니면 False 리턴

### 스택이란?
- LIFO : Last In First Out
- push : 시간복잡도 O(1)
- pop : 시간복잡도 O(1)