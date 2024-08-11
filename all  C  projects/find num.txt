#include <stdio.h>  //already used bubble shorting algorithm
#include <stdlib.h> //use serch by dividing method
#include <string.h>
#include <math.h>
#include <time.h>
#include <windows.h>
#include <ctype.h>
#include <stdbool.h>
//new ones from here
#include "limits.h"
#include "assert.h"
#include "errno.h"
#include "float.h"
int main(){ //find rand num in this array print num and index of num
  //  int array[]={10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};
    int array[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
    srand(time(0));
    int sec_num=(rand()%90)+10; // generate between 10 to 99
    int size=sizeof(array)/sizeof(array[0]);
    int max_no=size-1;  //last index position no

    if(sec_num>array[0] && sec_num<array[max_no]){
        int half = size/2;
        
        if(sec_num < array[half]){
            int a = half/2;

            if(sec_num < array[a]){
                int a1 = a/2;

                if(sec_num < array[a1]){
                    int a11 = a1/2;
                
                }else if(sec_num > array[a1]){
                    int a12 = a1 + (a1/2);
                
                }else if(sec_num == array[a1]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[a1]);
                printf("Index position of secret number is: %5d \n",a1);
                }

            }else if(sec_num > array[a]){
                int a2 = a+(a/2);

                if(sec_num < array[a2]){
                    int a21 = a2-((a2 - a) /2);
                
                }else if(sec_num > array[a2]){
                    int a22 = a2+((a2 - a) /2);
                
                }else if(sec_num == array[a2]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[a2]);
                printf("Index position of secret number is: %5d \n",a2);
                }

            }else if(sec_num == array[a]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[a]);
                printf("Index position of secret number is: %5d \n",a);
            }

        }else if(sec_num > array[half]){
            int b = half+(half/2);

            if(sec_num < array[b]){
                int b1 = b-((b - half)/2);

                if(sec_num < array[b1]){
                    int b11 = b1-((b1-half)/2);
                
                }else if(sec_num > array[b1]){
                    int b12 = b1+((b1-half)/2);
                
                }else if(sec_num == array[b1]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[b1]);
                printf("Index position of secret number is: %5d \n",b1);
                }

            }else if(sec_num > array[b]){
                int b2 = b+((b - half)/2);

                if(sec_num < array[b2]){
                    int b21 = b2-((b2 - b)/2);
                
                }else if(sec_num > array[b2]){
                    int b22 = b2+((b2 - b)/2);
                
                }else if(sec_num == array[b2]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[b2]);
                printf("Index position of secret number is: %5d \n",b2);
                }

            }else if(sec_num == array[b]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[b]);
                printf("Index position of secret number is: %5d \n",b);
            }

        }else if(sec_num == array[half]){
            printf("\nfound the number\n");
            printf("secret number is: %5d \n",array[half]);
            printf("Index position of secret number is: %5d \n",half);
        }
        
    }else{
        printf("\nnumber not found\n");
    }

    return 0;
}
