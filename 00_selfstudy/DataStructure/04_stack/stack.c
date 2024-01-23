#include <stdio.h>
#include <stdlib.h>

typedef struct Point{
  float x;
  float y;
}Point;

typedef struct Node{
  struct Point data;
  struct Node *next;
} Node;

typedef struct Stack{
  struct Node *top;
}Stack;

void initStack(Stack *stack)
{
  stack->top = NULL;
}

// 스택이 비었다면 1을 리턴
// 아니라면 0을 리턴
int isEmpty(Stack stack)
{
  if (stack.top = NULL)
    return 1;
  else
    return 0;
}

// 스택에 push
void push(Stack *stack, Point newData)
{
  Node *newNode = (Node*)malloc(sizeof(Node));
  if (newNode == NULL){
    fprintf(stderr, "Memory allocation failed\n");
    exit(EXIT_FAILURE);
  }

  newNode->data = newData;
  newNode->next = stack->top;
  stack->top = newNode;
}

Point pop(Stack *stack)
{
  if(stack->top == NULL){
    fprintf(stderr, "Stack is empty\n");
    exit(EXIT_FAILURE);
  }

  Node *temp = stack -> top;
  Point popppedData = temp->data;
  stack -> top = temp -> next;

  free(temp);
  return popppedData;
}

int main(){

  Stack stack;

  initStack(&stack);

  Point p1 = {1.0, 2.0};
  Point p2 = {3.0, 4.0};
  Point p3 = {5.0, 6.0};

  push(&stack, p1);
  push(&stack, p2);
  push(&stack, p3);

  Point popped = pop(&stack);
  printf("Popped: (%.2f, %.2f)\n", popped.x, popped.y);

  return 0;
}