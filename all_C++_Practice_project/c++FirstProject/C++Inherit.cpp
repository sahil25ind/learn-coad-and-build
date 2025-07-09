#include <iostream>

class animals{
    public:     //only public can ve inherite
        bool alive = true;
        int head = 1;

        void eat(){
            std::cout << "this animal is eating" << std::endl;
        }
    public:     //and this is allowed you can do this
        int tails = 1;

        void moveTail(){
            std::cout << "this animal is moving its tail" << std::endl;
        }
};
class cat:public animals{   //so public is the only thing that seems to work that allows to inherate animals
    public:
        void speak(){
            std::cout << "Meow Meow!" << std::endl;
        }
};
class dog:public animals{
    public:
        void speak(){
            std::cout << "Woof Woof!" << std::endl;
        }
};

int main(){
    cat cat1;
    dog dog1;

    std::cout << "Cat is alive: " << cat1.alive << std::endl << "Cat has no of head: " << cat1.head << std::endl;
    cat1.eat();
    cat1.speak();
    cat1.moveTail();

    std::cout << "Dog is alive: " << dog1.alive << std::endl << "dog has no of head: " << dog1.head << std::endl;
    dog1.eat();
    dog1.speak();
    dog1.moveTail();

    return 0;
}