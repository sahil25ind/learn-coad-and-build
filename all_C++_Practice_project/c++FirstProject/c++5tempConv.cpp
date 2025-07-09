#include <iostream>
#include <cmath>

void CtoF();
void FtoC();

int main(){
    // make temp convertor from celcious to farenhight
    int option;

    std::cout << "***** Temperature Convertor *****" << std::endl;
    std::cout << "1. Celsius(C) to Fahrenheit(F).\n2. Fahrenheit(F) to Celsius(C).\n3. Exit.\nEnter your Choice: ";
    std::cin >> std::ws >> option;
    
    while(option != 1 && option != 2 && option != 3){
        std::cout << "Enter your Choice: ";
        std::cin >> std::ws >> option;
    }

    switch(option){
        case 1:
            CtoF();
        break;
        case 2:
            FtoC();
        break;
        case 3:
            std::cout << "Exiting..." << std::endl;
            exit(0);
        break;
        default:
        std::cout << "Something went Wrong!" << std::endl;
    }

    return 0;
}
void CtoF(){
    double cTemp,result;
    char doAgain = 'y';
    while(doAgain == 'y'){
        std::cout << "\n***** Celsius(C) to Fahrenheit(F) *****" << std::endl;
        std::cout << "Enter the Celsius Temperature: ";
        std::cin >> std::ws >> cTemp;

        result = (cTemp * 9/5) + 32;

        std::cout << "result = " << result << " (F)" << std::endl;
        std::cout << "Would you like to use it again (y/n): ";
        std::cin >> std::ws >> doAgain;
    }
    std::cout << std::endl;
    main();
}
void FtoC(){
    double fTemp,result;
    char doAgain = 'y';
    while(doAgain == 'y'){
        std::cout << "\n***** Fahrenheit(F) to Celsius(C) *****" << std::endl;
        std::cout << "Enter the Fahrenheit Temperature: ";
        std::cin >> std::ws >> fTemp;

        result = (fTemp - 32) * 5/9;

        std::cout << "result = " << result << " (C)" << std::endl;
        std::cout << "Would you like to use it again (y/n): ";
        std::cin >> std::ws >> doAgain;
    }
    std::cout << std::endl;
    main();
}