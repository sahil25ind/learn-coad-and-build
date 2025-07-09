#include <iostream>
#include <iomanip>

void checkBalance(double balance);
double deposite();
double withdraw(double balance);

int main(){
    //banking program
    int choice;
    double balance = 0;
    do{
        std::cout << "\n***** Banking Program *****" << std::endl;
        std::cout << "1. Check Balance.\n2. Deposite Balance.\n3. Withdraw Balance.\n4. Exit.\nEnter your Choice: ";
        std::cin >> choice;

        switch(choice){
            case 1:
            checkBalance(balance);
            break;
            case 2:
            balance += deposite();
            checkBalance(balance);
            break;
            case 3:
            balance -= withdraw(balance);
            checkBalance(balance);
            break;
            case 4:
            std::cout << "Thanks for Visiting.\nExiting..." << std::endl;
            break;
            default:
            std::cout << "Invalid Input!" << std::endl;
        }

    }while(choice != 4);

    return 0;
}
void checkBalance(double balance){      //display 2 digits after the decimal
    std::cout << "Your Current Balance is: $" << std::setprecision(2) << std::fixed << balance << std::endl;
}
double deposite(){
    double deposite;
    std::cout << "Enter Amount for Deposite: ";
    std::cin >> deposite;
    
    if(deposite < 0){
        std::cout << "Deposite Amount cannot be less than 0" << std::endl;
        return 0;
    }else{
        return deposite;
    }
}
double withdraw(double balance){

    double withdrow;

    std::cout << "Enter Amount for the withdraw: ";
    std::cin >> withdrow;

    if(withdrow < 0){
        std::cout << "Withdraw Amount cannot be less than 0" << std::endl;
        return 0;
    }else if(withdrow > balance){
        std::cout << "Insufficient funds! \ntransation failed! " << std::endl;
        return 0;
    }else{
        return withdrow;
    }
}