#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
first_start:
    int h,m,s;
    printf("***** this is a simple timer ***** \n");
start:
    printf("\nset the timer for hours: ");
    scanf("%d",&h);
    if(h<0){
        printf("\nInvalid input. try again.\n");
        goto start;
    }else if(h>99){
        printf("\n99 is the MAX limit.hour should be less then or equal to 99.\n");
        goto start;
    }
start1:
    printf("\nset the timer for minutes: ");
    scanf("%d",&m);
    if(m<0){
        printf("\nInvalid input. try again.\n");
        goto start1;
    }else if(m>59){
        printf("\n59 is the MAX limit.minutes should be less then or equal to 59.\n");
        goto start1;
    }
start2:
    printf("\nset the timer for secounds: ");
    scanf("%d",&s);
    if(s<0){
        printf("\nInvalid input. try again.\n");
        goto start2;
    }else if(s>59){
        printf("\n59 is the MAX limit.secounds should be less then or equal to 59.\n");
        goto start2;
    }printf("\n\n");

    for(int i=h;i>=0;i--){
        for(int i=m;i>=0;i--){
            for(int i=s;i>=0;i--){  //adding delay for each secound
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                for(unsigned long long int delay=0;delay<100000000;delay++){}
                printf("%2d:%2d:%2d\n",h,m,s);
                s--;
            }
            s=59;
            m--;
        }
        m=59;
        h--;
    }
    printf("\ntimer is over.\nreseting the timer clock.\n\n");
    goto first_start;

    system("pause");

    return 0;
}