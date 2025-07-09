
int tic_tac_toe_AI(char gameArray[],char &player,char &computer){
    //check horizontally for computer
    if(gameArray[0] == gameArray[1] && gameArray[0] == computer && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[2] == gameArray[1] && gameArray[2] == computer && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[2] == gameArray[0] && gameArray[2] == computer && gameArray[1] == ' '){
        return 1;
    }else if(gameArray[3] == gameArray[4] && gameArray[3] == computer && gameArray[5] == ' '){
        return 5;
    }else if(gameArray[5] == gameArray[4] && gameArray[5] == computer && gameArray[3] == ' '){
        return 3;
    }else if(gameArray[5] == gameArray[3] && gameArray[5] == computer && gameArray[4] == ' '){
        return 4;
    }else if(gameArray[6] == gameArray[7] && gameArray[6] == computer && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[8] == gameArray[7] && gameArray[8] == computer && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[8] == gameArray[6] && gameArray[8] == computer && gameArray[7] == ' '){
        return 7;
    }
    //check vertically for computer
    if(gameArray[0] == gameArray[3] && gameArray[0] == computer && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[3] == gameArray[6] && gameArray[3] == computer && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[6] == gameArray[0] && gameArray[0] == computer && gameArray[3] == ' '){
        return 3;
    }else if(gameArray[1] == gameArray[4] && gameArray[1] == computer && gameArray[7] == ' '){
        return 7;
    }else if(gameArray[4] == gameArray[7] && gameArray[4] == computer && gameArray[1] == ' '){
        return 1;
    }else if(gameArray[7] == gameArray[1] && gameArray[1] == computer && gameArray[4] == ' '){
        return 4;
    }else if(gameArray[2] == gameArray[5] && gameArray[2] == computer && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[5] == gameArray[8] && gameArray[5] == computer && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[8] == gameArray[2] && gameArray[2] == computer && gameArray[5] == ' '){
        return 5;
    }
    //check d1 for computer
    if(gameArray[0] == gameArray[4] && gameArray[0] == computer && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[4] == gameArray[8] && gameArray[4] == computer && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[8] == gameArray[0] && gameArray[0] == computer && gameArray[4] == ' '){
        return 4;
    }
    //check d2 for computer
    if(gameArray[2] == gameArray[4] && gameArray[2] == computer && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[4] == gameArray[6] && gameArray[4] == computer && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[6] == gameArray[2] && gameArray[2] == computer && gameArray[4] == ' '){
        return 4;
    }

    //check horizontally for player
    if(gameArray[0] == gameArray[1] && gameArray[0] == player && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[2] == gameArray[1] && gameArray[2] == player && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[2] == gameArray[0] && gameArray[2] == player && gameArray[1] == ' '){
        return 1;
    }else if(gameArray[3] == gameArray[4] && gameArray[3] == player && gameArray[5] == ' '){
        return 5;
    }else if(gameArray[5] == gameArray[4] && gameArray[5] == player && gameArray[3] == ' '){
        return 3;
    }else if(gameArray[5] == gameArray[3] && gameArray[5] == player && gameArray[4] == ' '){
        return 4;
    }else if(gameArray[6] == gameArray[7] && gameArray[6] == player && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[8] == gameArray[7] && gameArray[8] == player && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[8] == gameArray[6] && gameArray[8] == player && gameArray[7] == ' '){
        return 7;
    }
    //check vertically for player
    if(gameArray[0] == gameArray[3] && gameArray[0] == player && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[3] == gameArray[6] && gameArray[3] == player && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[6] == gameArray[0] && gameArray[0] == player && gameArray[3] == ' '){
        return 3;
    }else if(gameArray[1] == gameArray[4] && gameArray[1] == player && gameArray[7] == ' '){
        return 7;
    }else if(gameArray[4] == gameArray[7] && gameArray[4] == player && gameArray[1] == ' '){
        return 1;
    }else if(gameArray[7] == gameArray[1] && gameArray[1] == player && gameArray[4] == ' '){
        return 4;
    }else if(gameArray[2] == gameArray[5] && gameArray[2] == player && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[5] == gameArray[8] && gameArray[5] == player && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[8] == gameArray[2] && gameArray[2] == player && gameArray[5] == ' '){
        return 5;
    }
    //check d1 for player
    if(gameArray[0] == gameArray[4] && gameArray[0] == player && gameArray[8] == ' '){
        return 8;
    }else if(gameArray[4] == gameArray[8] && gameArray[4] == player && gameArray[0] == ' '){
        return 0;
    }else if(gameArray[8] == gameArray[0] && gameArray[0] == player && gameArray[4] == ' '){
        return 4;
    }
    //check d2 for player
    if(gameArray[2] == gameArray[4] && gameArray[2] == player && gameArray[6] == ' '){
        return 6;
    }else if(gameArray[4] == gameArray[6] && gameArray[4] == player && gameArray[2] == ' '){
        return 2;
    }else if(gameArray[6] == gameArray[2] && gameArray[2] == player && gameArray[4] == ' '){
        return 4;
    }


    return -1; //index of array for the move
}