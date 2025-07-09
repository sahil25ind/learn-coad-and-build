#include <iostream>
#include <ctime>
#include <iomanip>

int findNumIndex(std::string numbers[],int size,std::string myNumber);

int main(){
    
    // int nums[] = {1,2,3,4,5,6,7,8,9,10};
    std::string numbers[] = {"123895","321675","95246","825525"};
    // int size = sizeof(nums) / sizeof(nums[0]);
    int size = sizeof(numbers) / sizeof(numbers[0]);
    // int myNum;
    std::string myNumber;
    int index;

    while(true){
        std::cout << "Enter a mobile number to search in the array: ";
        std::cin >> myNumber; //since taking string input. need to flash the input buffer
        std::cin;   // flashing the input buffer (removing the new line character)

        index = findNumIndex(numbers,size,myNumber);

        if(index != -1){
            std::cout << myNumber << " is at index: " << index << std::endl;
        }else{
            std::cout << myNumber << " is not in the array." << std::endl;
        }
    }
    return 0;
}
int findNumIndex(std::string numbers[],int size,std::string myNumber){
    for(int i = 0;i<size;i++){
        if(numbers[i] == myNumber){
            return i;
        }
    }
    return -1;
}