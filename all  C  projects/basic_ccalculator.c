#include <stdio.h>      //making a tic tac toe game
#include <stdlib.h>     //play against computer
#include <string.h>
#include <math.h>

int main(){
    double num1,num2,answer;
    char op;
    printf("this is a simple 2 by 2 calculator\n");
start:
    printf("\nEnter num1: ");
    scanf("%lf",&num1);
    printf("\nEnter an operator(+,-,*,/): ");
    scanf(" %c",&op);
    printf("\nEnter num2: ");
    scanf("%lf",&num2);

    switch(op){
        case '+':
        answer=num1+num2;
        printf("\nresult: %.2lf \n",answer);
        break;
        case '-':
        answer=num1-num2;
        printf("\nresult: %.2lf \n",answer);
        break;
        case '*':
        answer=num1*num2;
        printf("\nresult: %.2lf \n",answer);
        break;
        case '/':
        answer=num1/num2;
        printf("\nresult: %.2lf \n",answer);
        break;
        default:
        printf("\nInvalid input!\n");
    }
    goto start;

    return 0;
}
