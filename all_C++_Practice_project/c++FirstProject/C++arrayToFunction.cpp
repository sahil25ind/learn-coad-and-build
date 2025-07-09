#include <iostream>
#include <ctime>
#include <iomanip>

void displayArray(std::string iLoveYou[],int size);

int main(){
    std::string iLoveYou[] = {"suki","maji suki","dai suki","aishiteru"};
    int size = sizeof(iLoveYou)/sizeof(iLoveYou[0]);

    displayArray(iLoveYou,size);

    return 0;
}
void displayArray(std::string iLoveYou[],int size){
    
    for(int i = 0; i < size; i++){
        std::cout << iLoveYou[i] << std::endl;
    }

}