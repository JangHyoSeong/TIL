#include <stdio.h>

int main(){

  int x, y;
  int *p, *q;

  printf("addr of x = %u, addr of y = %u \n", &x, &y);

  x = 1;
  y = 2;
  p = &x;
  q = &x;

  *p = *p + 2;
  printf("p = %u, q = %u \n", p, q);
  printf("x = %u, y = %u \n", &x, &y);

  return 0;
}