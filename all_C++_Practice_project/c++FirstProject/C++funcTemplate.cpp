#include <iostream>

template <typename t,typename u>
auto small(t x,u y){    //if using auto keyword then you have to move the function up here above main if not adding auto then
    return x>y?y:x;     //you can do it normal way with prototyping and everything and even template <typename Thing, typename Thing2>
}                  //but if you are adding auto (for auto seleting return type) then move function above main function like this     

int main(){
    
    int rsult;

    std::cout << small(3.14159,'0') << std::endl;

    return 0;
}
