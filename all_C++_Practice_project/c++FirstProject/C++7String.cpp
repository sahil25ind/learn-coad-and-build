#include <iostream>

std::string fullName(std::string string1,std::string string2);

int main(){
    std::string firstname = "sahil";
    std::string lastname = "kumar";
    std::string fullname;

    std::cout << "Enter your first name: ";
    std::cin >> firstname;
    std::cout << "Enter your last name: ";
    std::cin >> lastname;

    fullname = fullName(firstname,lastname);

    std::cout << "Well Hello there " << fullname << std::endl;

    return 0;
}
std::string fullName(std::string string1,std::string string2)
{
    return string1 + " " + string2;
}