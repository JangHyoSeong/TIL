#include <stdio.h>
#include <stdlib.h>


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

  printf("(*(nodeA.next)).data = %d, (*(nodeA.next)).next = %p\n",
  (*(nodeA.next)).data, (*(nodeA.next)).next);

  return 0;

}