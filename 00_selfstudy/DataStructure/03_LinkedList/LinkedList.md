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

