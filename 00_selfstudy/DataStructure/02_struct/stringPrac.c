#include <stdio.h>
#include <string.h>


int main(){

  char name[100];

  // 얘는 안됨
  // 지금 name은 주소 상수인데, 대입 연산자의 왼쪽은 변수만 가능
  // name = "John";

  strcpy(name, "John");
  // 얘는 대신 string.h 가져와야함

  printf("%s", name);



  return 0;
}