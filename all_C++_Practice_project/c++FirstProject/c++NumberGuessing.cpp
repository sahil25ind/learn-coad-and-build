#include <iostream>
#include <ctime>

int main(){
    //number guessing game let the user guess the number infinitely and keep track of tries it took to guess the number
    //number limit
    int MAX = 99;
    int MIN = 10;

    int num;
    int tries;
    int guess;

    srand(time(NULL));  //initializing the seed (NULL == 0)

    num = (rand() % (MAX - MIN) + 1) + MIN;    //generate num between 10 and 99

    do{     //loop infinitely
        std::cout << "Enter a guess between (10 and 99): ";
        std::cin >> guess;  //not ignoring spaces = 0;

        tries ++;
        if(guess > num){
            std::cout << "Too High!" << std::endl;
        }else if(guess < num){
            std::cout << "Too Low!" << std::endl;
        }else{
            std::cout << "\nCongratulation You Win!" << std::endl;
            std::cout << "Secret no is: " << num << std::endl;
            std::cout << "no of tries: " << tries << std::endl;
        }

    }while(guess != num);   

    return 0;
}