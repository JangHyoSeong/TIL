# Linked List란?

## 예시

```C
struct Node{
  int data;
  struct Node* next;
};

int main()
{
  struct Node nodeA, nodeB, nodeC;

  nodeA.data = 3;
  nodeA.next = &nodeB;

  nodeB.data = 5;
  nodeB.next = &nodeC;

  nodeC.data = 5;
  nodeC.next = NULL;
}
```

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
---
### 장점
- 단순한 구조로 이루어져 있어서 구현이 편함
- 데이터의 추가, 삭제, 삽입이 쉬움
- 현재 노드가 가지고 있는 포인터 정보를 사용하여 추가적인 연산 없이 다음 노드를 가져올 수 있음

### 단점
- 노드에는 다음 노드를 가르키는 포인터가 필요하기 때문에 메모리를 추가로 사용
- 헤드 노드의 정보만 갖고 있기 때문에 특정 위치에 있는 노드를 탐색하는데 많은 연산이 필요

### Array List와 비교
- Array리스트는 특정 위치 노드 찾는 것이 빠름
- Array리스트보다 데이터의 추가, 삽입, 삭제가 쉬움

### 시간 복잡도
- 맨 앞에 노드 삽입 : O(1)
- 맨 뒤에 노드 삽입 : O(n)
- 탐색 : O(n)
- 특정 노드 뒤에 삽입 : O(1)
- 특정 노드 삭제 : O(1)