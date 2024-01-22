#include <stdio.h>
#include <stdlib.h>


struct Node{
  int data;
  struct Node* next;
};

/*
LinkedList를 계속 생성하고 연결하는 과정
temp로 노드를 생성한 후, 
temp -> next = top
top = temp
이렇게 꼭대기(맨 앞)노드를 생성 가능
*/


/*
새로운 노드를 생성하는 함수
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

void printAll(struct Node* node)
{
  while(node != NULL)
  {
    printf("[%d] -> ", node->data);
    node = node -> next;
  }
  printf("// \n");
}

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
  struct Node *top;
  struct Node *temp;

  top = NULL;

  temp = (struct Node *) malloc (sizeof(struct Node));
  temp -> data = 1;
  temp -> next = NULL;

  top = temp;

  temp = (struct Node *) malloc (sizeof(struct Node));
  temp -> data = 3;
  temp -> next = NULL;

  temp->next = top;
  top = temp;

  temp = (struct Node *) malloc (sizeof(struct Node));
  temp -> data = 5;
  temp -> next = NULL;

  temp->next = top;
  top = temp;

  temp = createNode(7);
  temp -> next = top;
  top = temp;

/*
  printf("top = %p \n", top);
  printf("top->next = %p \n", top->next);
  printf("top->next->next = %p \n", top->next->next);
  printf("top->next->next->next = %p\n", top->next->next->next);
  printf("top->next->next->next->next = %p\n", top->next->next->next->next);

  printf("top->data = %d\n", top->data);
  printf("top->next->data = %d\n", top->next->data);
  printf("top->next->next->data = %d\n", top->next->next->data);
  printf("top->next->next->next->data = %d\n", top->next->next->next->data);
*/

/*
  while(temp != NULL)
  {
    printf("[%d] -> ", temp->data);
    temp = temp -> next;
  }
  printf("// \n");
  printf("top = %p \n", top);
  printf("top->data = %d \n", top->data);


  while(top != NULL)
  {
    printf("[%d] -> ", top->data);
    top = top -> next;
  }
  printf("// \n");
  printf("top = %p \n", top);
  printf("top->data = %d \n", top->data);
*/

/*
위쪽 코드는 움직이는 위치에 따라 top이 이동하지 않음
아래쪽 코드는 top이 끝으로 이동해버려서 data를 읽어오면 오류발생
*/

printAll(top);
printf("top = %p \n", top);
printf("top->data = %d \n", top->data);

/*top에서부터 모든 노드를 할당해제하는 코드
  while(top != NULL)
  {
    struct Node* nextNode = top->next;
    free(top);
    top = nextNode;    
  }
*/
  freeAll(top);
  printf("top = %p \n", top);
  printf("top->data = %d \n", top->data);

  return 0;
}