#include <iostream>

int addEvenNum(std::string cardNum);
int addOddNum(std::string cardNum);
int addNum(int nums);

int main(){ //validate credit card (16) number is it valid card no or not

    std::string cardNum = "6011000990139424"; //this is valid card number
    int total;

    //asking user to input card number
    std::cout << "\n***** Check Your Credit Card Number *****" << std::endl;
    while(true){
        std::cout << "Enter your credit card no: ";
        std::cin >> cardNum;

        total = addEvenNum(cardNum) + addOddNum(cardNum);
    
        if(total % 10 == 0){
            std::cout << cardNum << " is Valid!" << std::endl;
        }else{
            std::cout << cardNum << " is not Valid!" << std::endl;
        }
    }

    return 0;
}
int addEvenNum(std::string cardNum){
    int evenSum = 0;
    for(int i = cardNum.length()-2;i>=0;i-=2){
        evenSum += addNum(((int)cardNum[i] - (int)'0')*2);
    }
    return evenSum;
}
int addOddNum(std::string cardNum){
    int oddSum = 0;
    for(int i = cardNum.length()-1;i>=0;i-=2){
        oddSum += ((int)cardNum[i] - (int)'0');
    }
    return oddSum;
}
int addNum(int nums){
    std::string snum = std::to_string(nums);    //convert int to string
    int total = 0;
    std::string temp;
    // 18 = 2-1 : 1,0 = 2 = 1 + 8 = 9
    for(int i = snum.length()-1;i>=0;i--){
        temp = snum[i];             //temperary veriable to store each of the letters shaperately
        total += std::stoi(temp);   //converting back to int here
    }
    // return total;
    return (nums % 10) + (nums / 10 % 10);
}