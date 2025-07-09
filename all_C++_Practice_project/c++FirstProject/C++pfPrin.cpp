#include <iostream>

void displayArray(int nums[],int &size){

    std::cout << &size << std::endl;
    
    for(int i = 0;i<size;i++){
        std::cout << nums[i] << " ";
    }
}

void sortArray(int nums[],int &size){

    std::cout << &size << std::endl;
    
    for(int j = 0;j<size-1;j++){
        for(int i = 0;i<size-1-j;i++){
            if(nums[i]>nums[i+1]){
                nums[i] = nums[i] ^ nums[i+1];
                nums[i+1] = nums [i] ^ nums[i+1];
                nums[i] = nums[i] ^ nums[i+1];
            }
        }
    }
}

int main(){
    int nums[] = {1,2,5,3,4,6,7,8,9,0};
    int size = sizeof(nums) / sizeof(nums[0]);

    std::cout << &size << std::endl;
    
    sortArray(nums,size);
    displayArray(nums,size);

    return 0;
}
