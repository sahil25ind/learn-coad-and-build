#include <iostream>
#include <cmath>

void printNums(int *nums,int &size){

    std::cout << 20 << std::endl;
}
int main(){  //pointer to a veriable and array as well
    int nums[] = {9,3,10,2,8,5,6,56,11,19,16,24,32,54,878,22,18,31,35,945,745,4,1,7};
    int size = sizeof(nums) / sizeof(nums[0]);

    std::cout << nums << std::endl;

    printNums(nums,size);

    // int age = 21;
    // int *pAge = &age;
    // int *pPoint = nullptr;
    // int *pPoint2 = NULL;

    // int arrayInt[5] = {1,2,3,4,5};
    // int *pArrayInt = arrayInt;

    // std::string name = "sahil kumar";
    // std::string *pName = &name;

    // std::string games[5] = {"Gta V","Gta VI","RDR 3","RDR 4","Black Mith"};
    // std::string *pGame = games;

    // std::cout << pPoint << std::endl;
    // std::cout << pPoint2 << std::endl;

    // if(pPoint == nullptr){
    //     std::cout << "this pointer is a NULL pointer" << std::endl;
    // }else{
    //     std::cout << "this pointet is pointing to name with value sahil kumar" << std::endl;
    // }

    // for(int i = 0;i<5;i++){
    //     std::cout << (pArrayInt[i] + 10) << std::endl;
    // }

    // for(int i = 0;i<5;i++){
    //     std::cout << pGame[i] << std::endl;
    //     if(pGame[i] == "Gta V"){
    //         std::cout << "Grand Theaf Auto V" << std::endl;
    //     }else if(pGame[i] == "Gta VI"){
    //         std::cout << "fuck you!" << std::endl;
    //     }else if(pGame[i] == "Black Mith"){
    //         std::cout << "Black Mith Sun BooKong" << std::endl;
    //     }else{
    //         continue;
    //     }
    // }

    // std::cout << &age << std::endl << pAge << std::endl << &pAge << std::endl;
    // std::cout << &name << endl << pName << endl << &pName << endl;
    // std::cout << games << std::endl << pGame << std::endl << &pGame << std::endl;
    // std::cout << pPoint << std::endl << &pPoint << std::endl;

    return 0;
}
