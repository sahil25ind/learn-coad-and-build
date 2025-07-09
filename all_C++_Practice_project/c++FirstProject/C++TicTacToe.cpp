#include <iostream>
#include <ctime>
#include <cmath>
#include "sahil_AI.h"

void showGame(char game[9]);
void playerMove(char game[9],char player);
void computerMove(char game[9],char player,char computer);
void checkTie(char game[9],char player,char computer,bool &playerWin,bool &compWin,bool &running);
bool gameOver(char game[9]);
void showWinner(char game[9],bool playerWin,bool compWin);
bool isWinner(char game[9],char player,char computer,bool &playerWin,bool &compWin);

int main(){     //tic tac toe game
    char spaces[9] = {' ',' ',' ',
                      ' ',' ',' ',
                      ' ',' ',' '};
    char player = 'X',computer = 'O';
    bool playerWin,compWin;
    bool running = true;

    srand(time(0));

    int randForMove;
    randForMove = rand()%2;

    std::cout << "\n***** tic tac toe *****" << std::endl;

    while(running){
        
        if(randForMove == 1){
            std::cout << "randMove = " << randForMove << std::endl;
            showGame(spaces);
            playerMove(spaces,player);
        }else{
            showGame(spaces);
            computerMove(spaces,player,computer);
            
        }
        checkTie(spaces,player,computer,playerWin,compWin,running);
        if(!running){
            break;
        }
        if(randForMove == 1){
            std::cout << "randMove = " << randForMove << std::endl;
            computerMove(spaces,player,computer);
        }else{
            showGame(spaces);
            playerMove(spaces,player);
        }
        checkTie(spaces,player,computer,playerWin,compWin,running);
        if(!running){
            break;
        }
        // std::cout << "\nrunning = " << running << std::endl;
    }

    system("pause");

    return 0;
}

void showGame(char game[9]){
    std::cout << std::endl;
    std::cout << " " << game[0] << " | " << game[1] << " | " << game[2] << " " << std::endl;
    std::cout << "---|---|---" << std::endl;
    std::cout << " " << game[3] << " | " << game[4] << " | " << game[5] << " " << std::endl;
    std::cout << "---|---|---" << std::endl;
    std::cout << " " << game[6] << " | " << game[7] << " | " << game[8] << " " << std::endl;
    std::cout << std::endl;
}
void playerMove(char game[9],char player){
    int playerInp;
    std::cout << "Enter your choice (1-9): ";
    std::cin >> playerInp;
    if(game[(playerInp-1)] == ' '){
        game[(playerInp-1)] = player;
    }else{
        playerMove(game,player);
    }
}
void computerMove(char game[9],char player,char computer){
    const int MAX = 8,MIN = 0;
    int computerInp; 

    computerInp = tic_tac_toe_AI(game,player,computer);

    if(computerInp == -1){
        computerInp = rand() % MAX+1;
    }
    
    if(game[computerInp] == ' '){
        game[computerInp] = computer;
        // computerInp = 0;
    }else{
        computerMove(game,player,computer);
    }
}
void checkTie(char game[9],char player,char computer,bool &playerWin,bool &compWin,bool &running){

    // std::cout << "checking tiesssssssssssssssssssssssssssssss" << std::endl;

    if(gameOver(game) && !isWinner(game,player,computer,playerWin,compWin)){
        showGame(game);
        std::cout << "Its a tie! \nGameOver!" << std::endl;
        running = false;
        // std::cout << "running = false" << std::endl;
        // return;
    }else if(isWinner(game,player,computer,playerWin,compWin)){
        running = false;
        showWinner(game,playerWin,compWin);
        // return;
    }

}
bool gameOver(char game[9]){
    // bool gameOver = false;
    //check for tie here
    for(int i = 0;i<9;i++){
        if(game[i] == ' '){
            // std::cout << "gameOver return false" << std::endl;
            return false;
        }
    }
    // std::cout << "gameOver return true" << std::endl;
    return true;
}
void showWinner(char game[9],bool playerWin,bool compWin){

    if(playerWin){
        showGame(game);
        std::cout << "Player Wins! \nGameOver!" << std::endl;
    }else if(compWin){
        showGame(game);
        std::cout << "Computer Wins! \nGameOver!" << std::endl;
    }

}
bool isWinner(char game[9],char player,char computer,bool &playerWin,bool &compWin){
    //checking horizontally
    if(game[0] != ' ' && game[0] == game[1] && game[1] == game[2]){
        if(game[0] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }else if(game[3] != ' ' && game[3] == game[4] && game[3] == game[5]){
        if(game[3] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }else if(game[6] != ' ' && game[6] == game[7] && game[6] == game[8]){
        if(game[6] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }
    //checking vertically
    if(game[0] != ' ' && game[0] == game[3] && game[0] == game[6]){
        if(game[0] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }else if(game[1] != ' ' && game[1] == game[4] && game[1] == game[7]){
        if(game[1] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }else if(game[2] != ' ' && game[2] == game[5] && game[2] == game[8]){
        if(game[2] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }
    //checking diagonally
    if(game[0] != ' ' && game[0] == game[4] && game[0] == game[8]){
        // std::cout << "checking d2" << std::endl;
        if(game[0] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }else if(game[2] != ' ' && game[2] == game[4] && game[2] == game[6]){
        // std::cout << "checking d1" << std::endl;
        if(game[2] == player){
            playerWin = true;
            compWin = false;
            return true;
        }else{
            compWin = true;
            playerWin = false;
            return true;
        }
    }

    // std::cout << "isWinner all false" << std::endl;
    playerWin = false;
    compWin = false;
    return false;
}