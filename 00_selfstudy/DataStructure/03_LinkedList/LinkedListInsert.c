#include <stdio.h>
#include <stdlib.h>

/*
Linked List의 모든 기능을 구현한 파일
*/

struct Node
{
  int data;
  struct Node* next;
};


/*
새로운 노드 생성
*/
struct Node* createNode(int val)
{
  struct Node* newNode;
  newNode = (struct Node *) malloc (sizeof(struct Node));
  newNode -> data = val;
  newNode -> next = NULL;

  printf("newNode = %p \n", newNode);
  return newNode;
}


/*
맨 앞에서부터 모든 노드의 값 출력
*/
void printAll(struct Node* node)
{
  while(node != NULL)
  {
    printf("[%d] -> ", node->data);
    node = node -> next;
  }
  printf("// \n");
}

/*
top이 가리키는 Linked List에서 데이터의 값이 val과 같은 노드가 있으면
그 노드의 포인터를 return
만약 그런 노드가 없다면 NULL을 리턴
*/
struct Node* searchNode(struct Node* top, int val)
{
  struct Node* curr;

  curr = top;

  while(curr != NULL)
  {
    if(curr->data == val)
    {
      return curr;
    }
    curr = curr -> next;
  }
  return NULL;
}


// 입력받은 노드 이후에 노드를 하나 삽입
void insertNext(struct Node* curr, int val)
{
  struct Node* newNode;

  newNode = createNode(val);
  newNode -> next = curr -> next;
  curr -> next = newNode;
}

/*
모든 노드 할당 해제
*/
void freeAll(struct Node* node)
{
  while(node != NULL)
  {
    struct Node* nextNode = node -> next;
    free(node);
    node = nextNode;    
  }
}

int main()
{
  struct Node* top;
  struct Node* temp;

  top = NULL;

  temp = createNode(1);
  top = temp;

  temp = createNode(3);
  temp -> next = top;
  top = temp;

  temp = createNode(5);
  temp -> next = top;
  top = temp;

  temp = createNode(7);
  temp -> next = top;
  top = temp;

  printAll(top);
  
  temp = searchNode(top, 3);
  printf("temp = searchNode(3); temp = %p \n", temp);

  // 값이 3인 노드 이후에 새 노드 삽입
  insertNext(temp, 100);
  printAll(top);

  freeAll(top);

  return 0;
}