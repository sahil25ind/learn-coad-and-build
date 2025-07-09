#include <iostream>
#include <cstring>  //allow you to manipulate strings (strcat() function here)
#include <vector>   //allow you to use vectors std::vector <datatype> name = {};
#include <optional> //allow you to use optional veriabla and optional value (either have value (behave like normal variable) or it does't have a value) 

struct human{
    std::string name;
    int age = 0;
    int hand = 2;
    int leg = 2;
    int head = 1;
    int finger = 5;
    int eyes = 2;
};

struct students{
    std::string name;
    double cgpa;
    bool enrolled = true;
};

void showStruct(students &student);
void modefyStruct(students &student,std::string name = " ",double cgpa = -1.0,std::optional<bool> enroll = std::nullopt);

int main(){
    //here i am doing it manually
    //struct hare BTW struct are defined outside of the main function
    // student student1 = {"sahil kumar",6.4,true};
    // student student2;
    // student2.name = "Pravin Kumar";
    // student2.cgpa = 8.9;
    // student2.enrolled = false;

    // std::cout << student1.name << std::endl;
    // std::cout << student1.cgpa << std::endl;
    // std::cout << student1.enrolled << std::endl;

    // std::cout << student2.name << std::endl;
    // std::cout << student2.cgpa << std::endl;
    // std::cout << student2.enrolled << std::endl;

    //and here i am doing it using vector its much better
    // std::vector <students> student = {
    //     {"sahil kumar",6.4,false},
    //     {"Pravin Kumar",7.9},
    //     {"Nitish Kumar",9.2},
    //     {"Anish Kumar",8.2},
    //     {"sakesh bhaiya",9.3},
    //     {"fochu bhaiya",9.8,false}
    // };

    // for(int i = 0;i<student.size();i++){   //student.size() (size()) is only for vectors it return no of elements in th vector
    //     std::cout << std::endl;
    //     std::cout << i << ". " << student[i].name << std::endl;
    //     std::cout << i << ". " << student[i].cgpa << std::endl;
    //     std::cout << i << ". " << student[i].enrolled << std::endl;
    // }

    // creating human structs using vector just #include <vector>
    // std::vector <human> humans = {
    //     {"sahil kumar",21,2,2,1,5,2},{"Pravin Kumar",19,2,2,1,5,2},{"ghinga lala",29,3,2,1,6,2}
    // };

    // for(int i = 0;i<humans.size();i++){
    //     std::cout << "human" << i+1 << std::endl;
    //     std::cout << humans[i].name << std::endl;
    //     std::cout << humans[i].age << std::endl;
    //     std::cout << humans[i].eyes << std::endl;
    //     std::cout << humans[i].hand << std::endl;
    //     std::cout << humans[i].leg << std::endl;
    //     std::cout << humans[i].finger << std::endl;
    //     std::cout << humans[i].head << std::endl;
    //     std::cout << std::endl;
    // }

    //pass struct as arguments in function
    
    students student1 = {"sahil Nitish",21,false};
    students student2 = {"Anish gopal",23};

    std::cout << "modefying student1 here" << std::endl;
    modefyStruct(student1,"Sahil Kumar");

    showStruct(student1);
    showStruct(student2);

    return 0;
}
void showStruct(students &student){
    std::cout << &student << std::endl;
    std::cout << student.name << std::endl;
    std::cout << student.cgpa << std::endl;
    std::cout << student.enrolled << std::endl;
}
void modefyStruct(students &student,std::string name = " ",double cgpa = -1.0,std::optional<bool> enroll = std::nullopt){
    if(name != " "){
        student.name = name;
    }
    if(cgpa != -1.0){
        student.cgpa = cgpa;
    }
    if(enroll.has_value()){
        std::cout << enroll.has_value() << std::endl;
        std::cout << enroll.value() << std::endl;
        student.enrolled = enroll.value();
    }
}