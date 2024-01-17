#include <stdio.h>

int main(){

  int sum, a;
  float average;
  int* p;
  float* fptr;

  sum = 20;
  average = 3.14;

  p = &sum;
  fptr = &average;

  printf("sum = %d, *p = %d\n", sum, *p);
  printf("average = %f, *fptr = %f\n", average, *fptr);

  *p = 10;
  *fptr = 1.234;

  printf("sum = %d\n", sum);
  printf("average = %f\n", average);


  return 0;
}