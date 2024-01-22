#include <stdio.h>

void addTwo(int* ptr)
{
  printf("ptr = %d \n", ptr);
  printf("*ptr = %d \n", *ptr);
  *ptr = *ptr + 2;
  printf("*ptr =%d \n", *ptr);
}

int main(){

  int x;

  x = 5;
  printf("add of x = %d\n", &x);
  addTwo(&x);

  printf("x = %d after function call \n", x);


  return 0;
}