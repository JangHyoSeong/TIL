#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
  int data;
  struct Node *next;
}Node;

typedef struct Queue{
  Node *front;
  Node *rear;
  int size;
}Queue;

void initQueue(Queue *queue)
{
  queue -> front = NULL;
  queue -> rear = NULL;
  queue -> size = 0;
}

int isEmpty(Queue *queue)
{
  return queue->size == 0;
}

void enQueue(Queue *queue, int data)
{
  Node *newNode = (Node *)malloc(sizeof(Node));
  newNode->data = data;
  newNode->next = NULL;
  if (isEmpty(queue))
  {
    queue->front = newNode;
  }
  else
  {
    queue->rear->next = newNode;
  }
  queue->rear = newNode;
  queue->size++;
}

int deQueue(Queue *queue)
{
  int data;
  Node *temp;
  if(isEmpty(queue))
  {
    printf("Error : Queue is empty\n");
    return 0;
  }
  temp = queue->front;
  data = temp->data;
  queue->front = temp->next;
  free(temp);
  queue->size--;

  return data;
}

int main()
{
  int i;
  Queue *queue;

  initQueue(queue);
  for(i=1; i <= 10; i++)
  {
    enQueue(queue, i);
  }
  
  while(!isEmpty(queue))
  {
    printf("%d ", deQueue(queue));
  }
  printf("\n");

  return 0;
}