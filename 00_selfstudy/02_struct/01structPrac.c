#include <stdio.h>
#include <string.h>

typedef struct{
  char name[100];
  char phone[100];
  int age;
}Addressinfo;

void printAddress(Addressinfo addr)
{
  printf("Name : %s \n", addr.name);
  printf("Phone number : %s \n", addr.phone);
  printf("Age : %d \n", addr.age);
  printf("\n");
}

int main(){

  Addressinfo addr1, addr2;
  Addressinfo *ptr;

  addr1.age = 23;
  strcpy(addr1.name, "Kim");
  strcpy(addr1.phone, "010-1234-5678");

  printf("sizeof struct = %d \n", sizeof(Addressinfo));

  ptr = &addr1;

  (*ptr).age = 25;
  strcpy((*ptr).name, "Park");
  
  ptr -> age = 32;
  // 구조체 변수의 포인터의 경우 -> 연산자를 통해 데이터에 접근 가능

  return 0;
}