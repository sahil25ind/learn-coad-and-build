#include <iostream>
#include <ctime>
#include <cmath>
#include "sahil_AI.h"

int main(){
    int size = 2;
    int *pNum = nullptr;
    int *temp = nullptr;
    pNum = new int;
    temp = new int[size];

    (*pNum) = temp[0];  //this was a stupid idea

    // *pNum = 25565;
    // pNum[1] = 6969;
    // pNum[2] = 12345;
    // pNum[3] = 321;
    // pNum[4] = 789;

    // delete pNum;
    
    std::cout << std::endl << &pNum << " -> " << pNum << " = " << *pNum << "\n" << std::endl;

    // for(int i = 0;i<size;i++){
    //     std::cout << &pNum << " -> " << &pNum[i] << " = " << pNum[i] << std::endl;
    // }

    return 0;
}