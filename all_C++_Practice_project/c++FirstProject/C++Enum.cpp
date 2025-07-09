#include <iostream>

enum day{sunday = 0,monday = 1,tuesday = 2,wednusday = 3,thrusday = 4,friday = 5,saturday = 6};

int main(){

    day today = monday;
    day today1 = (day) 0;  //this is totally valid just like in C

    //this is totally valid just like in C
    switch(today){
        case monday:
        std::cout << "today is monday!" << std::endl;
        break;
        case tuesday:
        std::cout << "today is tuesday!" << std::endl;
        break;
        case wednusday:
        std::cout << "today is wednusday!" << std::endl;
        break;
        case thrusday:
        std::cout << "today is thrusday!" << std::endl;
        break;
        case friday:
        std::cout << "today is friday!" << std::endl;
        break;
        case saturday:
        std::cout << "today is saturday!" << std::endl;
        break;
        case sunday:
        std::cout << "today is sunday!" << std::endl;
        break;
        default:
        std::cout << "not a valid day!" << std::endl;
        break;
    }

    //this is totally valid just like in C
    switch(today1){
        case 1:
        std::cout << "today is monday!" << std::endl;
        break;
        case 2:
        std::cout << "today is tuesday!" << std::endl;
        break;
        case 3:
        std::cout << "today is wednusday!" << std::endl;
        break;
        case 4:
        std::cout << "today is thrusday!" << std::endl;
        break;
        case 5:
        std::cout << "today is friday!" << std::endl;
        break;
        case 6:
        std::cout << "today is saturday!" << std::endl;
        break;
        case 0:
        std::cout << "today is sunday!" << std::endl;
        break;
        default:
        std::cout << "not a valid day!" << std::endl;
        break;
    }

    return 0;
}