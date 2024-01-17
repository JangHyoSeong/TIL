#include <stdio.h>
#include <string.h>

typedef struct{
  char name[100];
  char phone[100];
  int age;
}Addressinfo;

void addAge1(Addressinfo addr)
{
// 함수 호출시 204바이트를 복사하게 됨
  addr.age++;
}

void addAge2(Addressinfo *addr)
{
  (*addr).age++;
  addr -> age++;
  // 이렇게도 사용 가능
}

void printAddress(Addressinfo addr)
{
  printf("Name : %s \n", addr.name);
  printf("Phone number : %s \n", addr.phone);
  printf("Age : %d \n", addr.age);
  printf("\n");
}

void printAddressBook(Addressinfo addrBook[], int n)  //구조체 배열도 인자로 사용가능
{
  int i;
  for(i = 0;i<n;i++){
    printAddress(addrBook[i]);
  }
}

int main(){

  Addressinfo addrBook[100];  // 이러면 204 * 100 사이즈 메모리사용



  return 0;
}