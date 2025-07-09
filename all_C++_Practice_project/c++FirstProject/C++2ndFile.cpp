#include <iostream>

void openCalculator();  //this is prototyping for function and also function in c++ is also same as c i think

int main(){
    //so take input from user one word input and entire line input
    using std::string;
    string name;
    int age;
    string verify,answer;

    std::cout << "are you a human?: ";
    std::cin >> verify;

    // verify = tolower(verify);

    if(verify != "yes"){
        exit(0);
    }else{
            
        std::cout << "what is your name user?: ";
        std::getline(std::cin >> std::ws , name);

        std::cout << "how old are you?: ";
        std::cin >> std::ws >> age;

        std::cout << "\nyour name is " << name << '\n';
        std::cout << "and you are " << age <<" year old" << std::endl;
        std::cout << "so you are a human? " << verify << '\n';
        std::cout << "so user we have simple and very basic calculator.wanna use it (yea/no)?: ";
        std::cin >> answer;

        // if (answer == "yes"){   //if else is also same as c i think
        //     openCalculator();   //calling the function here its a void function so it does not return anything
        // }else{
        //     exit(0);        //this exit function is the inbuild one this exit from the function with the return code
        // }

        //this a ternary operator simple replacement for if-else only it's same as C
        answer == "yes" ? openCalculator() : exit(0);

    }

    return 0;       //this to mark the end of the progream
}
void openCalculator(){
    double num1,num2,result;
    char op;
    std::cout << "***** this is a very basic and simple calculator *****" << std::endl;
    std::cout << "Enter num1: ";
    std::cin >> num1;
    std::cout << "Enter op (+,-,*,/)('q' to quit): ";
    std::cin >> op;
    std::cout << "Enter num2: ";
    std::cin >> num2;

    switch (op){
        case '+':
        result = num1 + num2;
        break;
        case '-':
        result = num1 - num2;
        break;
        case '*':
        result = num1 * num2;
        break;
        case '/':
        result = num1 / num2;
        break;
        default:
        std::cout << "not a valid operator!" << std::endl;
    }
    std::cout << "resutl = " << result << std::endl;
}