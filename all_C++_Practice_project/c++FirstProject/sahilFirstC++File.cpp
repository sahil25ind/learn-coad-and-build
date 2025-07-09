#include <iostream>
#include <iomanip>
#include <ctime>
#include <cmath>
#include <cstring>
#include <optional>
#include <vector>
#include "sahil_AI.h"
 
// //namespace it allow for 
// namespace first{
//     using namespace std;
//     string name = "sahil kumar";
// }
// namespace secound{
//     using std::string;
//     string name = "pravin kumar";
// }

void referencThem(int &a,int &b);
void arrangeThem(int a,int b);

int main(){
    /*
    std::cout << "Hello World" << '\n';
    //so do more and print on next line ok
    std::cout << "hello i am sahil" << std::endl;
    std::cout << "i am learning cpp language" << std::endl;
    std::cout << "i want to finish this as quickly as possible" << std::endl;
    std::cout << "i want to learn Japanese in few month and i dont know how" << "\n";
    std::cout << "i need help god please tell me what do i do" << "\n";
    std::cout << "i watched alot of youtubers who learned japanese in 1 year or less" << "\n";
    std::cout << "they say first learn all basic and common vocabilary and then memorise all the pharases" << std::endl;
    std::cout << "and then just emmerse means just watch japanse media and content like only japanese for 1 year" << "\n";
    std::cout << "and then you will be fluent after finishing that it may take longer but it will work they said" << std::endl;
    std::cout << "what shoud i do shoud i just follow that for 1 whole year may be that what i shoud be doing" << "\n";

    // system("pause");
    */
    //int decimal get truncated (removed) only stores int
    
    // int x;
    // x = 5.8;
    // int y = 6.2;
    // int z = x + y;

    // std::cout << "result = " << z << "\nx = " << x << "\ny = " << y;    //this is possible just like java and python

    //double can store decimal

    // double x = 1.3;
    // double y = 3.5;
    // double z = x + y;

    // std::cout << "z = " << z;
    
    //char only single character and single quote ('') for char 

    // char grade = 'A';
    // char section = 'B';
    
    // std::cout << "chars here\n" << grade << "\n" << section;

    //bool (true or false) //i could be wrong but i think it print on 0 and 1 the true and false

    // bool student = true;
    // bool employed = false;
    // bool knowJapanese = false;
    
    // std::cout << "bool here\n" << student << "\n" << employed << "\n" << knowJapanese;

    //string its an object of array of char hopefully in c it way array of char

    // std::string name = "sahil kumar";
    // std::string name2 = "pravin kumar";
    // std::string professiion = "student";

    // std::cout << name << "\n" << name2 << std::endl;
    // std::cout << "my name is " << name << " but on paper my name is " << name2 << std::endl;
    // std::cout << "I am a " << professiion;

    // const double pi = 3.14159;
    // int radious = 5;

    // int circumference = 2 * pi * radious;
    // int area = pi * (radious*radious);

    // std::cout << "pi = " << pi << std::endl;
    // std::cout << "circumference = " << circumference << std::endl;
    // std::cout << "area = " << area << "\n";

    //using and namespaces all for identically named entities as long as they are in different namespaces

    // using namespace first;   //this is a namespace you need to create namespace before main function inorder to use them 
    // using namespace std;  //this will reduce the need to write std:: everywhere not recomended
    // using std::string;   //this one does exact same thing but only with std::string so instade you write string
    // using std::cout;     //same thing here as well just remove std:: but only with std::cout and leave it cout

    // string name = "Nitish Kumar";

    // cout << first::name;

    //typedef and using keywords used to give alies to pre-existing datatypes

    //typedef used to give another name to any datatype or anything hopefully
    // typedef std::vector<std::pair<std::string, double>> vectorPairList_t;   //dont know what this is not yeat
    // typedef int number_t;

    // int x = 5;
    // number_t y = 7;

    // std::cout << x << '\n';
    // std::cout << y << '\n';

    //using is used for same perpus
    // using text_u = std::string;

    // text_u name = "sahil kumar";
    // text_u name2 = "pravin kumar";
    // std::string nameFake = "nitish kumar";

    // std::cout << name << '\n';
    // std::cout << name2 << '\n';
    // std::cout << nameFake << '\n';

    //arthematic operation and operators + - * / %

    // int x = 2;
    // int y = 7;
    // int z = 22;

    // x = x + 1;
    // x+=1;
    // x++;
    // y = y - 1;
    // y-=1;
    // y--;
    // z = z * 2;
    // z *= 2;
    // z = z / 2;
    // z /= 2;
    // z = z % 3;


    // std::cout << x << '\n';
    // std::cout << y << '\n';
    // std::cout << z << '\n';

    //type conversion implesite and explesite
    //implesite 

    // char str = 100;  //int to char automatically according to ASCII table
    // int istr = 'd';  //char to int automatically according to ASCII table
    // int x = 3.13;  //only 3 will store so converted into int automatically

    // std::cout << str << '\n';
    // std::cout <<istr << std::endl;

    //explesite

    // double y = (int) 2.34;  //manually converting double into int and storing into double veriable
    // int answered = 9;
    // int totalQuestion = 10;
    // double score = (double) answered / totalQuestion * 100;

    // // std::cout << y << '\n';
    // std::cout << score << std::endl;

    // note that inplesite is build in by default and explesite one are user defined one you have to manully do it
    
    // std::string name;       //i am just checking my skills thats it noothing else here
    // int age;
    // char section;

    // std::cout << "Enter your name: ";
    // std::cin >> name;
    // std::cout << "Enter your age: ";
    // std::cin >> age;
    // std::cout << "Enter your section: ";
    // std::cin >> section;

    // std::cout << "my name is " << name << " and i am " << age << " years old and i'am in section " <<(int) section << "."<< std::endl;
    // std::cout << name << '\n';
    // std::cout << age << std::endl;
    // std::cout <<(int) section << '\n';

    //some basic math functions for more use standared c++ math libary  #include <cmath>

    // int x = 112;
    // int y = 32;
    // int z = 54;
    // int u = 89;
    // int w;

    // // w = std::min(x,y);   //problem with these is same as C it only accept 2 perimeter
    // // w = std::max(x,y);   //means you can only compare 2 values at a time

    // std::cout << std::min(x,y) << std::endl;    //print min
    // std::cout << std::max(x,y) << '\n';         //print max

    //ternary operator

    // std::string name = "pravin kumar";
    // std::string school = "vidya jyoti school";
    // int clas = 10;
    // int roll = 23;

    // //this is nested ternarty operator 
    // school == "vidya jyoti school" ? clas == 10 ? roll == 23 ? std::cout << name << std::endl : std::cout << "roll not found!" : std::cout << "class not found!" : std::cout << "school not found!" << std::endl;

    //logical operator (&& , || , !) and or not
    // int temp = -15456;

    // // if(temp < 40 && temp > 5){
    // //     std::cout << "temp is good" << std::endl;
    // // }else{
    // //     std::cout << "temp is bad" << std:: endl;
    // // }
    // if(temp > 50 || temp < 0){
    //     std::cout << "temperature is really bad!" << std::endl;
    // }else if(!temp){
    //     std::cout << "temp is empty!" << std::endl;
    // }else if(temp != 28){
    //     std::cout << "temp is not on room temperature 28" << std::endl;
    // }else{
    //     std::cout << "temperature is good" << std::endl;
    // }

    //while and do-while loop are exactly the same as C

    // std::string name;

    // //while loop
    // std::cout << "Enter your name: ";
    // std::getline(std::cin ,name);

    // while(name.empty()){
    //     std::cout << "Enter your name: ";
    //     std::getline(std::cin ,name);
    // }

    // //do-while loop
    // do{
    //     std::cout << "Enter your name: ";
    //     std::getline(std::cin , name);
    // }while(name.empty());

    // std::cout << "hello " << name << std::endl;

    //for loop

    // for(int i = 1;i<=100;i--){
    //     std::cout << i << ". fuck you!" << std::endl;
    // }

    //break and continue

    // for(int i = 1;i<=25;i++){
    //     if(i == 13 || i == 17){
    //         continue;
    //     }
    //     if(i == 20){
    //         break;
    //     }
    //     std::cout << i << std::endl;
    // }

    //nested loops

    // for(int i = 1;i<=10;i++){
    //     for(int j = 1;j<=10;j++){
    //         std::cout << j << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // //just drawing a rectangle with a char
    // int r,c;
    // char chr;
    // std::cout << "Enter a char for rect: ";
    // std::cin >> chr;
    // std::cout << "Enter #rows: ";
    // std::cin >> r;
    // std::cout << "Enter #columns: ";
    // std::cin >> c;

    // for(int i = 0;i<r;i++){
    //     for(int j = 0;j<c;j++){
    //         std::cout << chr << " ";
    //     }
    //     std::cout << std::endl;
    // }

    // random number (psudo-random) 
    //to do this first include ctime to accecss the current time for the seed for rand()
    //then create seed for the rand() using srand() and use time(0) as argument
    // srand(time(0));
    // srand(time(NULL));

    // int randNum1 = (rand()%(25-15+1))+15;
    // int randNum2 = (rand()%(25-15+1))+15;
    // int randNum3 = (rand()%(25-15+1))+15;

    // std::cout << randNum1 << std::endl;
    // std::cout << randNum2 << std::endl;
    // std::cout << randNum3 << std::endl;
    
    //random event generator in game i guess :|

    // srand(time(NULL));

    // for(int i = 0;i<10;i++){

    //     int randNum = (rand() % 10) + 1;

    //     switch(randNum){
    //         case 1:
    //         std::cout << "1.2x Exp multiplier Event starting." << std::endl;
    //         break;
    //         case 2:
    //         std::cout << "1.3x Exp multiplier Event starting." << std::endl;
    //         break;
    //         case 3:
    //         std::cout << "1.5x Exp multiplier Event starting." << std::endl;
    //         break;
    //         case 4:
    //         std::cout << "Zombi Event starting." << std::endl;
    //         break;
    //         case 5:
    //         std::cout << "Skeleton Event starting." << std::endl;
    //         break;
    //         case 6:
    //         std::cout << "creaper Event starting." << std::endl;
    //         break;
    //         case 7:
    //         std::cout << "villager Event starting." << std::endl;
    //         break;
    //         case 8:
    //         std::cout << "2x Exp multiplier Event starting." << std::endl;
    //         break;
    //         case 9:
    //         std::cout << "5x Exp multiplier Event starting." << std::endl;
    //         break;
    //         case 10:
    //         std::cout << "10x Exp multiplier Event starting." << std::endl;
    //         break;
    //         default:
    //         std::cout << "Something went Wrong!" << std::endl;
    //     }
    // }

    //decimal point precision for this include <iomanip>

    // double number = 23.543;
    // double number1 = 43;
    // int number2 = 34;
    // // you can setprecision or fixed first either way is fine and fixed dont need to be used every where just one place is fine
    // std::cout << "\nnumber = "<< std::fixed << std::setprecision(2) << number << std::endl;     //use it in first needed line 
    // std::cout << "number1 = " << std::setprecision(3) << std::fixed << number1 << std::endl;    //you need to set this but not needed everytime
    // std::cout << "number2 = " << number2 << std::endl;
    
    //Arrays in c++ its same as C 
    // initilization = declaring + assigning
    // std::string iLoveYou[] = {"suki","maji suki","dai suki","aishiteru"};
    // std::string iLoveYou = "aishiteru";
    // int size = sizeof(iLoveYou) / sizeof(iLoveYou[0]);
    
    // for(int i = 0;i<size;i++){
    //     std::cout << iLoveYou[i] << "   " ;
    // }
    // declaring but not assigning it yeat
    // std::string iLoveYou[4];
    // iLoveYou[0] = "suki";
    // iLoveYou[1] = "maji suki";
    // iLoveYou[2] = "dai suki";
    // iLoveYou[3] = "aishiteru";

    // std::cout << std::endl;

    // for(int i = 0;i<(sizeof(iLoveYou)/sizeof(iLoveYou[0]));i++){
    //     std::cout << iLoveYou[i] << "     ";
    // }
    // std::cout << std::endl;
    // std::cout << std::endl;

    //foreach loop(modefied for loop from Java)
    // std::string iLoveYou[] = {"suki","maji suki","dai suki","aishiteru"};

    // for(std::string love:iLoveYou){     //modefied for loop from Java
    //     std::cout << love << "\n";
    // }

    //fill() // this will allow you to fill any array and it has start finish and end
    // int size = 99;
    // int j = 1;
    // std::string name[size];

    // // fill(name,name + (size/3),"sahil kumar");
    // // fill(name + (size/3),name + ((size/3)*2),"Pravin kumar");
    // // fill(name + ((size/3)*2),name + size,"Nitish kumar");

    // // fill(name,name + (size/2),"sahdf");
    // // fill(name+(size/2),name + size,"kjjsdf");

    // for(std::string i:name){
    //     std::cout << j << " . " << i << std::endl;
    //     j++;
    // }

    //fill array with user input
    // std::string friends[5];
    // std::string temp;

    // for(int i = 0;i<5;i++){
    //     std::cout << "Enter your friends name or 'q' to quit: ";
    //     std::getline(std::cin,temp);
    //     if(temp == "q"){
    //         break;
    //     }else{
    //         friends[i] = temp;
    //     }
    // }
    // for(int i = 0;!friends[i].empty();i++){
    //     std::cout << friends[i] << std::endl;
    // }
    
    //2D Array it looks like metrix with rows and columns just like C

    // int r = 3;
    // int c = 3;

    // int metrix[r][c] = {
    //     {1,2,3},
    //     {4,5,6},
    //     {7,8,9}
    // };
    // metrix[0][1] = 20;
    // for(int ti = 0;ti<r;ti++){
    //     for(int tj = 0;tj<c;tj++){
    //         std::cout << "Enter a num for #" << ti+1 << " " << tj+1 << ": ";
    //         std::cin >> metrix[ti][tj];
    //     }
    // }

    // for(int i = 0;i<r;i++){
    //     for(int j = 0;j<c;j++){
    //         std::cout << metrix[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // int metrix[][4] = {
    //     {1,2,3,69},
    //     {4,5,6,65},
    //     {7,8,9,54},
    //     {10,11,12,23},
    //     {13,14,15,32}
    // };

    // int rows = sizeof(metrix)/sizeof(metrix[0]);
    // int columns = sizeof(metrix[0])/sizeof(metrix[0][0]);

    // std::cout << rows << std::endl << columns;
    
    // quiz game 
    // std::string questions[] = {"1. what is my name?","2. what is my official name?","3. what is my nick name given during school days?","4. what is my faverout food?"};
    // std::string answers[][4] = {
    //     {"A. gopal","B. bhushan","C. Nitish","D. sahil"},
    //     {"A. Pravin Kumar","B. Nitish Kumar","C. Anish Kumar","D. Golu Yadav"},
    //     {"A. natulla","B. bituna","C. tinia","D. sahil"},
    //     {"A. fried egg","B. chicken","C. noothing","D. spange"}
    // };
    // std::string correctAnswers[] = {"D","A","C","C"};
    // std::string choice;
    // int correctAns = 0;
    // int qSize = sizeof(questions) / sizeof(questions[0]);
    
    // std::cout << "\n***** Quiz Game in C++ *****\n";

    // for(int i = 0;i<qSize;i++){
    //     std::cout << "\n****************************\n";
    //     std::cout << questions[i] << std::endl;
    //     std::cout << "****************************\n";
    //     for(int j = 0;j<sizeof(answers[0])/sizeof(answers[0][0]);j++){
    //         std::cout << answers[i][j] << std::endl;
    //     }
    //     std::cout << "Enter your choice: ";
    //     std::cin >> choice;
    //     if(choice == correctAnswers[i]){
    //         correctAns++;
    //         std::cout << "Correct!" << std::endl;
    //     }else{
    //         std::cout << "Wrong!" << std::endl;
    //     }
    // }
    // std::cout << "\n****************************";
    // std::cout << "\n*          Result          *\n";
    // std::cout << "****************************\n";
    // std::cout << "correct: " << correctAns << "/" << qSize << "     Score: " << (correctAns /(double) qSize)*100 << "%";

    //bit wise operator ( & , | , ^ , << , >> )

    // int a = 2;
    // int b = 3;
    
    // std::cout << a << " ";
    // std::cout << b << std::endl;
    
    // // (XOR = ^)
    // a = a ^ b;
    // b = a ^ b;
    // a = a ^ b;

    // std::cout << a << " ";
    // std::cout << b << std::endl;

    //pass by reference and pass by values
    // pass by values
    // int a = 2,b = 3;

    // std::cout << "a = " << a << "  b = " << b << std::endl;
    // arrangeThem(a,b);

    //pass by reference
    // int a = 2,b = 3;

    // std::cout << "a = " << a << "  b = " << b << std::endl;
    // referencThem(a,b);    
    // std::cout << "a = " << a << "  b = " << b << std::endl;

    //swap any 2 veriable without 3rd even strings using std::swap(v_1,v_2);
    // std::swap(x,y);

    //string to int
    // std::string nums = "255";

    // int num = std::stoi(nums);

    // std::cout << "int num = " << num << std::endl;
    // std::cout << stoi(nums) << "   " << std::stoi(nums) << std::endl;

    //int to string

    // int nums = 2560;
    // std::string num = std::to_string(nums);
    // num += " 40";

    // std::cout << num << std::endl;

    // std::cout << pow(11,2) << std::endl;

    //Dynamic-memorry allocation (new , delete)
    // int size = 5;
    // int *pNum = nullptr;
    // pNum = new int[size];
    
    // for(int i =0;i<size;i++){
    //     pNum[i] = 25565 + i;
    // }

    // delete[] pNum;
    // // delete[] pNum;
    
    // std::cout << &pNum << " -> " << pNum << " = " << *pNum << std::endl;
    // std::cout << std::endl;

    // for(int i = 0;i<size;i++){
    //     std::cout << &pNum[i] << " = " << pNum[i] << std::endl;
    // }
    // delete pNum;    //1st time clear the memory but does not free the memory pointer is still pointing at the memory
    // delete pNum;    //2nd time free the memory and now pointer is not pointing at the memory
    // free(pNum);     //this one does the same thing but its a C thing not C++ but it still works

    // std::cout << pNum << std::endl;
    // std::cout << *pNum << std::endl;
    
    // just checking this dynamic memory allocation

    // int size = 5;
    // int *pNum = NULL;
    // pNum = new int;
    // delete pNum;
    // pNum = NULL;
    // if(pNum == nullptr){
    //     std::cout << "Fail to assign the memory to the pointer pNum" << std::endl;
    // }else{
    //     std::cout << "memory assigned successfully.\n" << &pNum << " -> " << pNum << " = " << *pNum << std::endl;
    // }

    //recursion vs iterative
    // its a concepy specific to only programming not bonded by any language not actual thing or keyword in c++ 

    //function template this is very similar to generic methods in Java (Thing can accept multiple data type input)
    //function template (template <typename Thing>) allows you have as many overloaded funtion as needed without creating new functions
    // this template defines typename Thing and this Thing can accept any data type as input and you can also have more 
    // template <typename Thing , typename Thing2> now this can accept 2 differrent data type
    // see the file C++funcTemplate.cpp

    // template <typename Thing> and also this is only for functions and you can have multiple Thing of datatype or name is whatever

    //struct (structure) same as C see file =  C++structANDvector.cpp (it also has vector)

    //enum = user-defined data type that can have some potential values, declared outside of main function
    // it support index value but not for itteration only for (int - value) pair 
    // see file = C++Enum.cpp

    //OOP in C++ see the file  C++OOP.cpp

    //getters and setters  see file C++GetSet.cpp
    // this is not a keyword or buildin function or object its a concept of accessing a private veriable by creating a function
    // in a class (object)

    //Inheritance in C++
    // see the file  C++Inherit.cpp
    // see for use case file  C++UseInherit.cpp

    //few very important concept of OOP in C++
    // Encapsulation    -   alrady done it in getter and setter
    // getter and setter    -   see file  C++GetSet.cpp
    // constructors     -   already dont it in getter and setter
    // Inheritance      -   already dont it see file  C++Inherit.cpp
    

    return 0;
}
// template <typename Thing>    //this added later shaperately has noothing to do with function
// void referencThem(Thing &a,Thing &b){
// void referencThem(int &a,int &b){
//     int temp = a;
//     a = b;
//     b = temp;

//     std::cout << "a = " << a << "  b = " << b << std::endl;

// }
// template <typename Thing1,typename thing2>    //you can have 2 thing data type for function template, you can have more
// void arrangeThem(Thing1 a,Thing2 b){
// void arrangeThem(int a,int b){
//     a = a ^ b;
//     b = a ^ b;
//     a = a ^ b;

//     std::cout << "a = " << a << "  b = " << b << std::endl;

// }