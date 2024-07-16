#include <stdio.h>
#include <stdlib.h>

int main()
{
    int Balance;
    int Deposite,Withdraw;
    int userinput;
    Balance = 1000;
    printf("--- Hello User! --- \n");
start:
    printf("\n*** Bank Account ***\n  1.Check Account Balance\n  2.Deposite Balance\n  3.Withdraw Balance\n  4.Exit\n \nEnter no: ");
    scanf("%d",&userinput);
    switch(userinput) {
        case 1:
        printf("Your Account Balance is %d \n",Balance);
        goto start;
        break;
        case 2:
            case2:
        printf("Enter Amount: ");
        scanf("%d",&Deposite);
            if (Deposite <= 0) { printf("\aInvalid Input! try again \n");
            goto case2; }
        Balance = Balance + Deposite;
        printf("Your Updated Balance is %d \n",Balance);
            goto start;
        break;
        case 3:
            case3:
                if (Balance == 0) { printf("\aYour Account Balance is: 0\nWithdraw unsuccesful!\n");
            goto start; }

        printf("Enter Amount: ");
        scanf("%d",&Withdraw);


            if (Withdraw > Balance || Withdraw <= 0) { printf("\aInvalid Input! try again\n");
            goto case3; }

        Balance = Balance - Withdraw;
        printf("Your Remaning Balance is %d \n",Balance);
        goto start;
        break;
        case 4:
            printf("closing the program... \n");
        break;
        default:
        printf("\aInvalid Input! \n");
        goto start;
    }


}
