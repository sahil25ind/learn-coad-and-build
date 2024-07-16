#include <stdio.h>
#include <stdlib.h>
#include <string.h>     //some strings stufs
#include <stdbool.h>
#include <time.h>
#include <math.h>
#include <windows.h>
#include <ctype.h>
                    //short the value of the array in assending order
void sort(int array[],int size);  //prototype of the function because its not the main function
void sortedprint(int array[],int size);

int main(){
  int array[]={7,8,4,6,9,1,3,2,5,84,54,74,1,4};
 // char array[]={'A','D','F','Z','Y','C','G','H','E','W','S','B'};
  int size=sizeof(array)/sizeof(array[0]);

  printf("***** sorting an array of integer *****\n");
  printf("Array: {7,8,4,6,9,1,3,2,5,84,54,74,1,4} \n\n");
  sort(array,size);
  printf("sorted array: ");
  sortedprint(array,size);
  printf("\n\n");

  return 0;
}
void sort(int array[],int size){
  for(int i=0;i<size-1;i++){
    for(int j=0;j<size-1;j++){
      if(array[j]>array[j+1]){
          int temp = array[j];
          array[j] = array[j+1];
          array[j+1] = temp;
      }
    }
  }

}
void sortedprint(int array[],int size){
  for(int i=0;i<size;i++){
    printf("%d ",array[i]);
  }
}
