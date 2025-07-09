#include <iostream>

int main(){
    // std::string name = "sahil kumar";
    // std::cout << "Enter your name: ";
    // std::getline(std::cin >> std::ws,name);

    // std::cout << name.length() << std::endl;     //return no of char include space null terminator not included
    // std::cout << name.at(10) << std::endl;       //this can give error out_of_range if index exceed limit while name[23] will not
    // std::cout << name.find('a') << std::endl;    //return first occurance of the char
    // name = name.replace(0,11,8,'z');             //start_index, end_index_excluded, no_of_time_to_replace, char_to_replace
    // name.clear();                                //clean the veriable string completely
    // std::cout << name.empty() << std::endl;      //return boolean value
    // name.erase(3,3);                             //erase from starting index to continus no of element else erase all of it
    // name.insert(5,10,'@');                       //insert_at_index, no_of_char, char 
    // name.append("@gmail.com");                   //append the text into the string
    
    std::string name;

    do{
        std::cout << "Enter your name: ";
        std::getline(std::cin,name);
    }while(name.empty());

    std::cout << "hello " << name << std::endl;

    return 0;
}