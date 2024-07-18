#include <stdio.h>      // make a guessing game using random number generator
#include <stdlib.h>     // 
#include <math.h>
#include <time.h>

int main(){
    srand(time(0));
    int sec_num=rand()%99+1;
    int guess;
    int guess_count;

    printf("***** this is a simple guessing game ***** \n");
    printf("you have only 10 guesses \n");
    
    for(int i=1;i<=10;i++){
    printf("\nEnter a guess: ");
    scanf("%d",&guess);
    if(guess == sec_num){
        printf("\nYou Won!!! \nsecret number is %d \n",sec_num);
        break;
    }else if(guess>sec_num){
        printf("\nEntered guess is a little to high.\n");
    }else if(guess<sec_num){
        printf("\nEntered guess is a little to low.\n");
    }
    guess_count++;
    }
    if(guess == sec_num){
        printf("guess count: %d \n",guess_count);
    }else if(guess != sec_num){
        printf("\nYou Lose!\nYou run out of guesses.\n");
    }
system("pause");
    return 0;
}
