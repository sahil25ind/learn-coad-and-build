#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
    //simple countdown timer clock
int main(){
    int h,m,s;
    int inputLimit = 99;
    printf("***** Timer Clock *****\n");
//input limit is 99
    do{
        printf("Enter Hour: ");
        scanf("%d",&h);
    }while(h > inputLimit || h < 0);

    do{
        printf("Enter Minutes: ");
        scanf("%d",&m);
    }while(m > inputLimit || m < 0);

    do{
        printf("Enter Second: ");
        scanf("%d",&s);
    }while(s > inputLimit || s < 0);

    h = h * 3600;
    m = m * 60;
    s = s + h + m;
    //declaring a local veriabel not sure why here!. why not up there!
    int ts;

    for(s;s > 0;s--){

        sleep(1);
        h = (s / 3600);
        m = (s / 60) % 60;
        ts = s % 60;

        printf("\n%02d:%02d:%02d",h,m,ts);
    }
    printf("\n\nTIME'S UP!\n");
}
