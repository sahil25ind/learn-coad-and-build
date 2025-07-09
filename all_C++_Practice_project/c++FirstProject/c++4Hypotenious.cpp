#include <iostream>
#include <cmath>
    //take user input for both prependicular and base and calculate hypotenious and display it 
int main(){
    //calculate the hypotenious of a right angle triangle
    double prependicular;
    double base;
    double hypotenious;

    std::cout << "***** Calculate the Hypotenious *****" << std::endl;
    std::cout << "Enter the Prependicular: ";       //prompt for prependicular
    std::cin >> std::ws >> prependicular;           //take input for prependicular
    std::cout << "Enter the Base: ";                //prompt for the base
    std::cin >> std::ws >> base;                    //take input for base

    hypotenious = sqrt(pow(prependicular,2) + pow(base,2));     //formula for calculating the hypotenious

    std::cout << "hypotenious = " << hypotenious << std::endl;  //print it on the screen

    return 0;
}