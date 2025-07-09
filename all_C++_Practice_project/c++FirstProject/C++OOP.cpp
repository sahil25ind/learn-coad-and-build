#include <iostream>
#include <vector>
#include <optional>

class humans {
    public:
        std::string name = "sahil kumar";
        int age = 21;
        bool alive = true;

        //this is a constructor and has some parameters samething from java only defference -> instade of .
        //and this is called overloaded constructors same constructors with different parameter
        humans(std::string name,int age,bool alive = true){
            this -> name = name;
            this -> age = age;
            this -> alive = alive;
        }
        humans(std::string name){
            this -> name = name;
        }
        humans(){   //this one just does't do anything or accept anything
            
        }


        void describe(std::optional <bool> fuck = std::nullopt){
            std::cout << "name = " << name << std::endl;
            std::cout << "age = " << age << std::endl;
            std::cout << "alive = " << alive << std::endl;
            if(fuck.has_value()){
                std::cout << fuck.value() << std::endl << "fuck you!" << std::endl;
            }
        }
        void walk(){
            std::cout << "o shit i can walk!" << std::endl;
        }
        void speak(){
            std::cout << "holy crap i can speak!" << std::endl;
        }
        void eat(){
            if(alive){
                std::cout << "o i can eat,this shoud't be surprising i am alive after all!" << std::endl;
            }else{
                std::cout << "i am dead i cant eat, dead person dont eat!" << std::endl;
            }
        }

};

int main(){
    //if not passing arguments then dont need parameters
    humans human1("Pravin Kumar",19,true);
    humans human2;  //this has no parameters

    std::cout << human1.name << std::endl;
    std::cout << human1.age << std::endl;
    std::cout << human1.alive << std::endl;
    human1.eat();
    human1.speak();
    human1.walk();
    human1.describe();

    // humans human1 = {"Pravin Kumar",19,true};
    // // humans human2 = {"sahil Kumar",21,false};
    // humans human2;

    // std::vector <humans> humVec = {{"Pravin Kumar",19,true},{"sahil Kumar",21,false},{"Pravin Kumar",19,true}};
    
    // humVec[0].describe(true);

    // for(int i = 0;i<humVec.size();i++){
    //     std::cout << humVec[i].name << std::endl;
    //     std::cout << humVec[i].age << std::endl;
    //     std::cout << humVec[i].alive << std::endl;
    //     humVec[i].walk();
    //     humVec[i].speak();
    //     humVec[i].eat();
    // }

    // std::cout << human1.name << std::endl;
    // std::cout << human1.age << std::endl;
    // std::cout << human1.alive << std::endl;
    // human1.walk();
    // human1.speak();
    // human1.eat();

    // std::cout << human2.name << std::endl;
    // std::cout << human2.age << std::endl;
    // std::cout << human2.alive << std::endl;
    // human2.walk();
    // human2.speak();
    // human2.eat();

    return 0;
}