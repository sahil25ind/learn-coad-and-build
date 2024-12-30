#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void stopwatch();
void timer();

int main()
{start:
    int choice;
    printf("***** very basic clock that does't display time *****\n1. stopwatch.\n2. timer.\n\nEnter your(1/2) choice: ");
    scanf("%d",&choice);
    switch (choice){
    case 1:
        stopwatch();
        break;
    case 2:
        timer();
        break;
    default:
        printf("\nInvalid Input. try again\n\n");
        goto start;
    }
    printf("\n\n");
    goto start;

    system("pause");

    return 0;
}
void stopwatch()
{
    printf("\n***** this is a stopwatch ***** \n");
    int h,m,s,ms;
    h=0;
    m=0;
    s=0;
    ms=0;
    for(int i=0;i<100;i++){
        for(int i=0;i<60;i++){
            for(int i=0;i<60;i++){
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                printf("%2d:%2d:%2d\n",h,m,s);
                s++;
            }
            s=0;
            m++;
        }
        m=0;
        h++;
    }
}
void timer()
{
    int h,m,s;
    printf("\n***** this is a timer ***** \n\n");
   printf("set your timer in (hours/minutes/secound) \n");
start:
   printf("\nEnter the timer (h)hour: ");
   scanf("%d",&h);
   if(h<0){
        printf("\n(h)hour can't be less than 0.(h)hour should be greater then or equal to 0.\n");
        goto start;
   }else if(h>99){
        printf("\n99 is the max (h)hour limit.(h)hour should be less then 99.\n");
        goto start;
   }
start1:
   printf("\nEnter the timer (m)minutes: ");
   scanf("%d",&m);
   if(m<0){
        printf("\n(m)minutes can't be less than 0.(m)minutes should be greater then or equal to 0.\n");
        goto start1;
   }else if(m>59){
        printf("\n59 is the max (m)minutes limit.(m)minutes should be less then 59.\n");
        goto start1;
   }
start2:
   printf("\nEnter the timer (s)secound: ");
   scanf("%d",&s);
   if(s<0){
        printf("\n(s)secound can't be less than 0.(s)secound should be greater then or equal to 0.\n");
        goto start2;
   }else if(s>59){
        printf("\n59 is the max (s)secound limit.(s)secound should be less then 59.\n");
        goto start2;
   }
  //  printf("%2d:%2d:%2d",h,m,s);
    for(int i=h;i>=0;i--){
        for(int i=m;i>=0;i--){
            for(int i=s;i>=0;i--){
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                for(unsigned long long int delay=0;delay<100000000;delay++){ }
                printf("%2d:%2d:%2d\n",h,m,s);
                s--;
            }
            m--;
            s=59;
        }
        h--;
        m=59;
    }

}
