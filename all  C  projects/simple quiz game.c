#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main()
{int j=0,score=0;
    char questions[][100]={"1. what is your name?: ","2. who is vedal?: ","3. what do you wanna do and make?: "};
    char options[][100]={"A. sahil kumar","B. pravin kumar","C. movie","D. anime movie","A. vtuber","B. AI","C. vedal987","D. turtle","A. software Engeneer and AI","B. goof around","C. waste time","D. waste time by making friends and being social"};
    char answer[]={'D','D','A'};
    char guess;
    int question_size=sizeof(questions)/sizeof(questions[0]);
    int options_size=sizeof(options)/sizeof(options[0]);
    
    
    printf("***** its a simple quiz game. *****\n");
    for(int i=0;i<question_size;i++){
        printf("\n*************************************\n");
        printf("%s \n",questions[i]);
        printf("*************************************\n");
        for(int i=0;i<options_size/question_size;i++, j++){
            printf("%s \n",options[j]);
        }
        
        scanf("%c",&guess);
        scanf("%*c");
        guess=toupper(guess);
        if(guess==answer[i]){
            printf("correct\n");
            score++;
        }else{
            printf("wrong\n");
        }
    }
    printf("\n**********************\n");
    printf("final score: %d/%d",score,question_size);
    printf("\n**********************\n");
    
    return 0;
}
