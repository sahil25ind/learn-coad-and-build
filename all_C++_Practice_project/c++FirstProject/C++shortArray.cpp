#include <iostream>

void showMemAdrs(int nums[],int size);
void shortArray(int nums[],int size);
void showArray(int nums[],int size);

int main(){
    //arrange the array using bubble sort algorithm 
    int nums[] = {9,3,10,2,8,5,6,56,11,19,16,24,32,54,878,22,18,31,35,945,745,4,1,7};
    int size = sizeof(nums) /sizeof(nums[0]);

    shortArray(nums,size);
    showArray(nums,size);

    //display memory address of all the elements
    std::cout << std::endl;
    std::cout << &nums[0] << std::endl;
    std::cout << &nums[1] << std::endl;
    std::cout << std::endl;

    showMemAdrs(nums,size);

    return 0;
}
void showMemAdrs(int nums[],int size){
    for(int i =0;i<size;i++){
        std::cout << &nums[i] << std::endl;
    }
}
void shortArray(int nums[],int size){
    int temp;
    for(int i = 0;i<size-1;i++){
        for(int j = 0;j<size-i-1;j++){
            if(nums[j] > nums[j+1]){
                temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
            }
        } 
    }
}
void showArray(int nums[],int size){
    for(int i = 0;i<size;i++){
        std::cout << nums[i] << "  ";
    }
}