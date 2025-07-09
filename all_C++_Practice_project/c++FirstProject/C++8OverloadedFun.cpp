#include <iostream>
//example of overloaded functions
void makeGames();
void makeGames(std::string game);
void makeGames(std::string game1,std::string game2);

int main(){
    makeGames("Minecraft","Gta V");

    return 0;
}
//overloaded functions are basically exact same function with different parameters
void makeGames(){
    std::cout << "you made a Game!" << std::endl;
}
void makeGames(std::string game){
    std::cout << "you made " << game << std::endl;
}
void makeGames(std::string game1,std::string game2){
    std::cout << "you made " << game1 << " and " << game2 << std::endl;
}