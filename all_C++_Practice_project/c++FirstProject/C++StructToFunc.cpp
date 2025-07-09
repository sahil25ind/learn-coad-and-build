#include <iostream>
#include <vector>
#include <optional>

struct persions{
    std::string name;
    int age;
    bool alive = true;
};

void modefyPersions(persions &persion, std::string name = "", int age = -1, std::optional <bool> alive = std::nullopt);
void showVector(std::vector <persions> &persionVector);
void showPersion(persions &persion);

int main(){     //use the vector
    std::vector <persions> persionVector = {
        {"Sahil Kumar",21},{"Pravin Kumar",19},{"Dead Persion",89,false}
    };

    std::cout << &persionVector[0].name << std::endl;
    modefyPersions(persionVector[0],"",20);
    showVector(persionVector);

    // persions persion1 = {"sahil kumar",21};
    // persions persion2 = {"Dead Kumar",98,false};

    // sahilStr(persion1,"sahil kumar");
    // showPersion(persion1);

    return 0;
}
void modefyPersions(persions &persion, std::string name, int age, std::optional <bool> alive){
    
    if(!name.empty()){
        persion.name = name;
    }
    if(age != -1){
        persion.age = age;
    }
    if(alive.has_value()){
        persion.alive = alive.value();
    }

}
void showVector(std::vector <persions> &persionVector){
    std::cout << &persionVector[0] << std::endl;
    for(int i = 0;i<persionVector.size();i++){
        std::cout << persionVector[i].name << std::endl;
        std::cout << persionVector[i].age << std::endl;
        std::cout << persionVector[i].alive << std::endl;
    }

}
void showPersion(persions &persion){
    std::cout << "persion1 = " << &persion << std::endl;
    std::cout << "Name = " << persion.name << std::endl;
    std::cout << "Age = " << persion.age << std::endl;
    std::cout << "Alive = " << persion.alive << std::endl;
}