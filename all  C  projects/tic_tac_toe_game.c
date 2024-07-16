#include <stdio.h>		//make a tic tac toe game
#include <stdlib.h>		//play against computer
#include <string.h>
#include <ctype.h>		//it should be  3 X 3 
#include <math.h>
#include <stdbool.h>

char matrix[3][3];

void inti_matrix(); 		//set matrix to ' ' empty space
void get_player_move();		//get player move and set it to marix
void get_computer_move();	//get computer move and set it to marix
void display_matrix();		//display the matrix (veriable)
char check();				//check for possible combinations and return it

int main(){
	printf("this is a simple tic tac toe game.\n");
	printf("you will be playing against the computer.\n");
	char ch;
	ch=' ';
	inti_matrix(); 	//loop here
	do{
		display_matrix();
		get_player_move();
		ch=check();
		if(ch!=' '){break;}
		get_computer_move();
		ch=check();
	}while(ch == ' ');
	
	if(ch == 'X'){
		printf("\nplayer win!\n");
	}else{
		printf("\ncomputer wins!\n");
	}
	display_matrix();

	system("pause");

	return 0;
}
void inti_matrix(){		//set matrix to empty space
	int i,j;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			matrix[i][j]=' ';
		}
	}
}
void get_player_move(){	//getting player moves
	int x,y;
	printf("Enter X,Y coordinates for your move: ");
	scanf("%d%*c%d",&x,&y);
	x--;y--;
	if(matrix[x][y]!=' '){
		printf("Invalid move. try again.\n");
		get_player_move();
	}else{ matrix[x][y]='X'; }	// X  is for player
}
void get_computer_move(){	//getting computer moves
	int x,y;
	for(x=0;x<3;x++){
		for(y=0;y<3;y++){
			if(matrix[x][y]==' '){
				break;
			}
		}
		if(matrix[x][y]==' '){
			break;
		}
	}
	if(x*y==9){
		printf("its a Draw\n");
	}else{
		matrix[x][y]='O';	// O  is for computer
	}
}							
void display_matrix(){	//display the matrix
	int i;				
	for(i=0;i<3;i++){
		printf("\n %c | %c | %c \n",matrix[i][0],matrix[i][1],matrix[i][2]);
		if(i!=2){
			printf("\n---|---|---\n");
		}
	}
	printf("\n");
}
char check(){	//checking for any possible combination and returning it
	int i;
	for(i=0;i<3;i++){	//checking rows/horizontally
		if(matrix[i][0] == matrix[i][1] && matrix[i][0] == matrix[i][2]){ return matrix[i][0];	}
	}
	for(i=0;i<3;i++){	//checking vertically/column
		if(matrix[0][i]==matrix[1][i] && matrix[0][i]==matrix[2][i]){ return matrix[0][i];	}
	}	//checking 1st diagonal
	if(matrix[0][0]==matrix[1][1] && matrix[1][1]==matrix[2][2]){ return matrix[0][0];	}	//checking 2nd diagonal
	if(matrix[0][2]==matrix[1][1] && matrix[1][1]==matrix[2][0]){ return matrix[0][2];	}

	return ' ';
}