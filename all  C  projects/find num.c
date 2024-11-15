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
int main(){     //find rand num in this array print num and index of num
    int array[]={10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};
  //  int array[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
  
    srand(time(0));
   // int sec_num = (rand()%90)+10;      // generate between 10 to 99
    int sec_num = 65;

    int size=sizeof(array)/sizeof(array[0]);
    int max_no=size-1;       //last index position no

    if(sec_num >= array[0] && sec_num <= array[max_no]){
        int half = size/2;
        
        if(sec_num < array[half]){
            int a = half/2;

            if(sec_num < array[a]){
                int a1 = a/2;

                if(sec_num < array[a1]){
                    int a11 = a1/2;

                    if(sec_num < array[a11]){   
                        int a111 = a11/2;

                        if(sec_num < array[a111]){   //need work here
                        int a1111 = a111/2;
                
                        }else if(sec_num > array[a111]){
                        int a1112 = a111+(a111/2);
                
                        }else if(sec_num == array[a111]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a111]);
                        printf("Index position of secret number is: %5d \n",a111);
                        }
                
                    }else if(sec_num > array[a11]){
                        int a112 = a11 + (a11/2);

                        if(sec_num < array[a112]){   //need work here
                        int a1121 = a112-((a112-a11)/2);
                
                        }else if(sec_num > array[a112]){
                        int a1122 = a112+((a112-a11)/2);
                
                        }else if(sec_num == array[a112]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a112]);
                        printf("Index position of secret number is: %5d \n",a112);
                        }
                
                    }else if(sec_num == array[a11]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[a11]);
                    printf("Index position of secret number is: %5d \n",a11);
                    }
                
                }else if(sec_num > array[a1]){  
                    int a12 = a1 + (a1/2);

                    if(sec_num < array[a12]){
                        int a121 = a12-((a12 - a1)/2);
                        
                        if(sec_num < array[a121]){   //need work here
                        int a1211 = a121-((a121-a1)/2);
                
                        }else if(sec_num > array[a121]){
                        int a1212 = a121+((a121-a1)/2);
                
                        }else if(sec_num == array[a121]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a121]);
                        printf("Index position of secret number is: %5d \n",a121);
                        }
                
                    }else if(sec_num > array[a12]){
                        int a122 = a12+ ((a12 - a1)/2);

                        if(sec_num < array[a122]){   //need work here
                        int a1221 = a122-((a122-a12)/2);
                
                        }else if(sec_num > array[a122]){
                        int a1222 = a122+((a122-a12)/2);
                
                        }else if(sec_num == array[a122]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a122]);
                        printf("Index position of secret number is: %5d \n",a122);
                        }
                
                    }else if(sec_num == array[a12]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[a12]);
                    printf("Index position of secret number is: %5d \n",a12);
                    }
                
                }else if(sec_num == array[a1]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[a1]);
                printf("Index position of secret number is: %5d \n",a1);
                }

            }else if(sec_num > array[a]){
                int a2 = a+(a/2);

                if(sec_num < array[a2]){
                    int a21 = a2-((a2 - a) /2);

                    if(sec_num < array[a21]){   
                        int a211 = a21-((a21-a)/2);

                        if(sec_num < array[a211]){   //need work here
                        int a2111 = a211-((a211-a)/2);
                
                        }else if(sec_num > array[a211]){
                        int a2112 = a211+((a211-a)/2);
                
                        }else if(sec_num == array[a211]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a211]);
                        printf("Index position of secret number is: %5d \n",a211);
                        }
                
                    }else if(sec_num > array[a21]){
                        int a212 = a21 + ((a21-a)/2);

                        if(sec_num < array[a212]){   //need work here
                        int a2121 = a212-((a212-a21)/2);
                
                        }else if(sec_num > array[a212]){
                        int a2122 = a212+((a212-a21)/2);
                
                        }else if(sec_num == array[a212]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a212]);
                        printf("Index position of secret number is: %5d \n",a212);
                        }
                
                    }else if(sec_num == array[a21]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[a21]);
                    printf("Index position of secret number is: %5d \n",a21);
                    }
                
                }else if(sec_num > array[a2]){
                    int a22 = a2+((a2 - a) /2);

                    if(sec_num < array[a22]){   
                        int a221 = a22-((a22-a2)/2);

                        if(sec_num < array[a221]){   //need work here
                        int a2211 = a221-((a221-a2)/2);
                
                        }else if(sec_num > array[a221]){
                        int a2212 = a221+((a221-a2)/2);
                
                        }else if(sec_num == array[a221]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a221]);
                        printf("Index position of secret number is: %5d \n",a221);
                        }
                
                    }else if(sec_num > array[a22]){
                        int a222 = a22+((a22-a2)/2);

                        if(sec_num < array[a222]){   //need work here
                        int a2221 = a222-((a222-a22)/2);
                
                        }else if(sec_num > array[a222]){
                        int a2222 = a222+((a222-a22)/2);
                
                        }else if(sec_num == array[a222]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[a222]);
                        printf("Index position of secret number is: %5d \n",a222);
                        }
                
                    }else if(sec_num == array[a22]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[a22]);
                    printf("Index position of secret number is: %5d \n",a22);
                    }
                
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

                    if(sec_num < array[b11]){
                        int b111 = b11-((b11-half)/2);

                        if(sec_num < array[b111]){   //need work here
                        int b1111 = b111-((b111-half)/2);
                
                        }else if(sec_num > array[b111]){
                        int b1112 = b111+((b111-half)/2);
                
                        }else if(sec_num == array[b111]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b111]);
                        printf("Index position of secret number is: %5d \n",b111);
                        }
                
                    }else if(sec_num > array[b11]){
                        int b112 = b11+((b11-half)/2);

                        if(sec_num < array[b112]){   //need work here
                            int b1121 = b112-((b112-b11)/2);
                
                        }else if(sec_num > array[b112]){
                            int b1122 = b112+((b112-b11)/2);
                
                        }else if(sec_num == array[b112]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b112]);
                        printf("Index position of secret number is: %5d \n",b112);
                        }
                
                    }else if(sec_num == array[b11]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[b11]);
                    printf("Index position of secret number is: %5d \n",b11);
                    }
                
                }else if(sec_num > array[b1]){
                    int b12 = b1+((b1-half)/2);

                    if(sec_num < array[b12]){   
                        int b121 = b12-((b12-b1)/2);

                        if(sec_num < array[b121]){   //need work here
                            int b1211 = b121-((b121-b1)/2);
                
                        }else if(sec_num > array[b121]){
                            int b1212 = b121+((b121-b1)/2);
                
                        }else if(sec_num == array[b121]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b121]);
                        printf("Index position of secret number is: %5d \n",b121);
                        }
                
                    }else if(sec_num > array[b12]){
                        int b122 = b12+((b12-b1)/2);

                        if(sec_num < array[b122]){   //need work here
                            int b1221 = b122-((b122-b12)/2);
                
                        }else if(sec_num > array[b122]){
                            int b1222 = b122+((b122-b12)/2);
                
                        }else if(sec_num == array[b122]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b122]);
                        printf("Index position of secret number is: %5d \n",b122);
                        }
                
                    }else if(sec_num == array[b12]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[b12]);
                    printf("Index position of secret number is: %5d \n",b12);
                    }
                
                }else if(sec_num == array[b1]){
                printf("\nfound the number\n");
                printf("secret number is: %5d \n",array[b1]);
                printf("Index position of secret number is: %5d \n",b1);
                }

            }else if(sec_num > array[b]){
                int b2 = b+((b - half)/2);

                if(sec_num < array[b2]){
                    int b21 = b2-((b2 - b)/2);

                    if(sec_num < array[b21]){
                        int b211 = b21-((b21-b)/2);

                        if(sec_num < array[b211]){   //need work here
                            int b2111 = b211-((b211-b)/2);
                
                        }else if(sec_num > array[b211]){
                            int b2112 = b211+((b211-b)/2);
                
                        }else if(sec_num == array[b211]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b211]);
                        printf("Index position of secret number is: %5d \n",b211);
                        }
                
                    }else if(sec_num > array[b21]){
                        int b212 = b21+((b21-b)/2);

                        if(sec_num < array[b212]){   //need work here
                            int b2121 = b212-((b212-b21)/2);
                
                        }else if(sec_num > array[b212]){
                            int b2122 = b212+((b212-b21)/2);
                
                        }else if(sec_num == array[b212]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b212]);
                        printf("Index position of secret number is: %5d \n",b212);
                        }
                
                    }else if(sec_num == array[b21]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[b21]);
                    printf("Index position of secret number is: %5d \n",b21);
                    }
                
                }else if(sec_num > array[b2]){
                    int b22 = b2+((b2 - b)/2);

                    if(sec_num < array[b22]){
                        int b221 = b22-((b22-b2)/2);

                        if(sec_num < array[b221]){   //need work here
                            int b2211 = b221-((b221-b2)/2);
                
                        }else if(sec_num > array[b221]){
                            int b2212 = b221+((b221-b2)/2);
                
                        }else if(sec_num == array[b221]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b221]);
                        printf("Index position of secret number is: %5d \n",b221);
                        }
                
                    }else if(sec_num > array[b22]){
                        int b222 = b22+((b22-b2)/2);

                        if(sec_num < array[b222]){   //need work here
                            int b2221 = b222-((b222-b22)/2);
                
                        }else if(sec_num > array[b222]){
                            int b2222 = b222+((b222-b22)/2);
                
                        }else if(sec_num == array[b222]){
                        printf("\nfound the number\n");
                        printf("secret number is: %5d \n",array[b222]);
                        printf("Index position of secret number is: %5d \n",b222);
                        }
                
                    }else if(sec_num == array[b22]){
                    printf("\nfound the number\n");
                    printf("secret number is: %5d \n",array[b22]);
                    printf("Index position of secret number is: %5d \n",b22);
                    }
                
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
