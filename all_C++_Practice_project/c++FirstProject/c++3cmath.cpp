#include <iostream>
#include <cmath>

int main (){
    int x = 3;
    int y = 6;
    unsigned long int z = 5;
    long double pi = 3.99999914159;
    double result;

    //these 2 are in iostream library
    // result = std::max(x,y);
    // result = std::min(x,y);

    //these 6 are in cmath library
    // result = pow(pow(2,3),2);
    // result = sqrt(pow(pow(2,3),2));
    // result = abs(-265);
    // result = round(pi);
    // result = ceil(pi);
    // result = floor(pi);

    std::cout << result << std::endl;
    
    
    return 0;
}