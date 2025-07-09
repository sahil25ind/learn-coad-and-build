#include <iostream>

class Stove{
    private:    //this is private only accessable inside this class not outside
    int temperature = 0;    
    public:     //this is public accessable from anywhere inside or outside of this class
    
    Stove(int temperature){
        setTemperature(temperature);
    }
    Stove(){

    }
    //this is getter function user-defined there is not actual build-in function
    int getTemperature(){
        return temperature;
    }
    //this is setter function user-defined their is not actual build-in function 
    void setTemperature(int temperature){
        if(temperature < 0){
            this->temperature = 0;
        }else if(temperature > 10){
            this->temperature = 10;
        }else{
            this->temperature = temperature;
        }
    }
};

int main(){
    Stove stove1;
    Stove stove2(2);

    stove1.setTemperature(5);

    std::cout << stove1.getTemperature() << std::endl;
    std::cout << stove2.getTemperature() << std::endl;

    return 0;
}