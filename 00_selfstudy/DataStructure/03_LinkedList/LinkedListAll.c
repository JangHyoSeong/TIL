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


//data 값을 갖고 있는 노드의 이전에 val 값을 가진 노드를 삽입
//맨 처음 노드 이전에 삽입하기 위해 이중 포인터를 사용
void insertBefore(struct Node **first, int data, int val)
{
  struct Node *newNode;
  struct Node *curr, *prev;

  curr = searchNode(*first, data);
  if (curr == NULL)
  {
    printf("insertBefore: %d가 리스트에 없어 삽입에 실패했습니다.\n", data);
  }
  else
  {
    prev = *first;
    newNode = createNode(val);

    if (curr != *first)
    {
      while (prev->next != curr)
      {
        prev = prev->next;
      }
      prev->next = newNode;
    }
    else
    {
      *first = newNode; // 첫 번째 노드를 새로운 노드로 업데이트
    }
    newNode->next = curr;
  }
}


// 입력받은 데이터에 해당하는 노드를 삭제
// top노드와 지울 데이터를 입력받음
// 첫 번째 노드도 지울 수 있도록 이중 포인터로 first를 받아옴
// 이를 통해 first는 top의 주소를 기억함(포인터 변수의 주소를 기억)
void deleteNode (struct Node **first, int data)
{
  struct Node *prev, *curr;

  curr = searchNode(*first, data);
  if (curr == NULL){
    printf("There is no data %d in the list \n", data);
  }
  else{
    if(curr != *first){
      prev = *first;
      while(prev->next != curr){
        prev = prev->next;
      }
      prev->next = curr->next;
    }
    else{
      *first = (*first) -> next;
    }
    free(curr);
  }
}



//모든 노드 할당 해제

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
  struct Node* temp, *deletedNode;

  top = createNode(1);
  insertNext(top, 3);

  temp = searchNode(top, 3);
  insertNext(temp, 5);

  temp = searchNode(top, 5);
  insertNext(temp, 7);

  printAll(top);

  deleteNode(&top, 1);
  printAll(top);
  
  insertBefore(&top, 3, 9);
  printAll(top);


  freeAll(top);

  return 0;
}