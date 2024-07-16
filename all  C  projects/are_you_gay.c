#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
int main()
{   printf("*** Enter only 1 dogit \"0 = False\" or \"1 = True\" *** \n");
  start:
    bool X;
    int y;  //dont use decimals it breaks the code.

    printf("Are you Gay: ");
    scanf("%d",&y);
    if(y!=0 && y!=1){
        printf("invalid input!\n");
        goto start;
    }
    else{
    X=y;
    if(X==true){
            printf("fuck you!\n"); }
    else {  printf("so you are Gay!\n"); }
    goto start;
    return 0;
    }
}
