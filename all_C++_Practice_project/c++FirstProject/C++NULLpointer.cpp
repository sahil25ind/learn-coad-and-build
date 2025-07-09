#include <iostream>

int main(){
    int x = 12345;
    int *pX = nullptr;

    // pX = &x;
    std::cout << *pX << std::endl;


    if(pX == nullptr){
        std::cout << "memory is not assigned!" << std::endl;
    }else{
        std::cout << "memory is assigned successfully!" << std::endl;
    }

    return 0;
}