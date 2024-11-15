#include <stdio.h>  //using recursion to add squares of numbers
#include <stdlib.h>
void sqrAdd(int num1,int num2,int *result);
int main(){start:
  int num1,num2,result=0;
  printf("Enter num1: ");
  scanf("%d",&num1);
  printf("Enter num2: ");
  scanf("%d",&num2);

  sqrAdd(num1,num2,&result);
  printf("sum of the squares of %d to %d is: %d\n\n",num1,num2,result);
 goto start; 
  return 0;
}
void sqrAdd(int num1,int num2,int *result)
{
  if(num1>num2){
    return;
  }
  *result += num1*num1;
  sqrAdd(num1+1,num2,result);
}
