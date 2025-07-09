#include <iostream>

int factorialRecursion(int x){
    if(x>1){
        return x * factorialRecursion(x-1);
    }else{
        return 1;
    }
}
int factorialIteration(int x){
    int result = 1;
    for(int i = 1;i<=x;i++){
        result *= i;
    }
    return result;
}

int main(){
    int num = 10;
    
    std::cout << factorialRecursion(num) << std::endl;
    std::cout << factorialIteration(num) << std::endl;
    

    return 0;
}