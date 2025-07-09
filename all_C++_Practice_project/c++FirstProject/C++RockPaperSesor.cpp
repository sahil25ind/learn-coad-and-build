#include <iostream>
#include <ctime>

char getPlayerMove();
char getComputerMove();
void checkWinner(char player,char computer);
void showMove(char showChoice,std::string turn);

int main(){
    //rock paper scissor
    while(true){    //this is a infinite loop with no escape lol !!!
        char playerChoice;
        char computerChoice;

        playerChoice = getPlayerMove();
        computerChoice = getComputerMove();
        showMove(playerChoice,"You");
        showMove(computerChoice,"Computer");

        checkWinner(playerChoice,computerChoice);
    }
    
    return 0;
}
char getPlayerMove(){
    char choice;
    do{
        std::cout << "\n***** Game of Rock Paper Scissor *****" << std::endl;
        std::cout << "'R' for Rock.\n'P' for Paper.\n'S' for scissor.\nEnter your choice: ";
        std::cin >> choice;
        choice = toupper(choice);

    }while(choice != 'R' && choice != 'P' && choice != 'S');
    
    std::cout << std::endl;

    return choice;
}
char getComputerMove(){
    //randomly guess rock paper scissor
    srand(time(NULL));

    int rnum = (rand()%3)+1;    //generate random num between 1 to 3

    switch(rnum){
        case 1:
        return 'R';
        break;
        case 2:
        return 'P';
        break;
        case 3:
        return 'S';
        break;
    }
    return '@';
}
void checkWinner(char player,char computer){
    if(player == 'R' && computer == 'R'){
        std::cout << "Its a Draw! :|" << std::endl;
    }else if(player == 'P' && computer == 'P'){
        std::cout << "Its a Draw! :|" << std::endl;
    }else if(player == 'S' && computer == 'S'){
        std::cout << "Its a Draw! :|" << std::endl;
    }else if(player == 'R' && computer == 'P'){
        std::cout << "Computer Wins! :(" << std::endl;
    }else if(player == 'R' && computer == 'S'){
        std::cout << "Player Wins! :)" << std::endl;
    }else if(player == 'P' && computer == 'R'){
        std::cout << "Player Wins! :)" << std::endl;
    }else if(player == 'P' && computer == 'S'){
        std::cout << "Computer Wins! :(" << std::endl;
    }else if(player == 'S' && computer == 'R'){
        std::cout << "Computer Wins! :(" << std::endl;
    }else if(player == 'S' && computer == 'P'){
        std::cout << "Player Wins! :)" << std::endl;
    }
}
void showMove(char showChoice,std::string turn){

    switch(showChoice){
        case 'R':
        std::cout << turn << " Picked: Rock" << std::endl;
        break;
        case 'P':
        std::cout << turn << " Picked: Paper" << std::endl;
        break;
        case 'S':
        std::cout << turn << " Picked: Scissor" << std::endl;
        break;
    }
}