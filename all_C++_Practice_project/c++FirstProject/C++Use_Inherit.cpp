#include <iostream>
#include <string>
#include <vector>

class Person{
    protected:
    std::string *first;
    std::string *last;
    public:
    Person() = default;
    Person(std::string &first,std::string &last):first(&first),last(&last) {    
        // std::cout << &first << " = " << first << "      " << &last << " = " << last << "\n";    
    }
    void setFirst(std::string &first){
        for(int i = 0;i<first.length()+1;++i){
            if(std::isdigit(first[i])){
                first.erase(i,1);
                i--;
                // this -> first = &first;
            }else if( (!std::islower(first[i]) || i == 0) && i != first.length() ){
                if(i != 0){
                    first[i] = std::tolower(first[i]);
                }
                first[0] = std::toupper(first[0]);
                std::cout << &first << " = " << first << "  - " << i << std::endl;
                // this -> first = &first;
            }else{
                std::cout << "else here - :" << i << std::endl;
                this -> first = &first;
            }
        }
    }
    void setLast(std::string &last){
        
        for(int i = 0;i<last.length()+1;++i){

            if(std::isdigit(last[i])){

                last.erase(i,1);
                i--;

                // this -> last = &last;
            }else if( (!std::islower(last[i]) || i == 0) && i != last.length() ){
                
                if(i != 0){
                    last[i] = std::tolower(last[i]);
                }
                last[0] = std::toupper(last[0]);

                std::cout << &last << " = " << last << "  - " << i << std::endl;
                
                // this -> last = &last;
            }else{
                std::cout << "else here - :" << i << std::endl;
                this -> last = &last;
            }
            
        }
    
    }
    std::string getName(){  return *first + " " + *last;    }
    void printFullName(){   std::cout << *first << " " << *last << "\n";    }
    virtual void printInfo(){
        std::cout << std::endl << first << " = " << *first << "      " << last << " = " << *last << "\n";
        // std::cout << "Name = " << getName() << "\n";
        // std::cout << "Department = " << *department << "\n\n";
    }
    static void vectorPrintInfo(std::vector <Person*> &people){
        // std::cout << "vector People = " << &people << "\n";
        for(auto people:people){
            people->printInfo();
        }
    }
};

class Employee:public Person{
    private:
    std::string *department;
    public:
    Employee(std::string &first,std::string &last,std::string &department):Person(first,last),department(&department) {
        // std::cout << &department << " = " << department << "\n";    
    }
    void printInfo() override{
        std::cout << std::endl << first << " = " << *first << "      " << last << " = " << *last << "\n";
        // std::cout << "Name = " << getName() << "\n";
        std::cout << department << " = " << *department << "\n\n";
    }
    std::string getDepartment(){
        std::cout << department << " = " << *department << "\n";    
        return *department;
    }
    void setDepartment(std::string &department){
        std::cout << &department << " = " << department << "\n";    
        this -> department = &department;
    }
};

void takeUserInput(std::string &first,std::string &last);

int main(){
    std::string first = "firstName",last = "lastName",department = "programmer";
    std::vector <Person*> people;

    // std::cout << &first << " = " << first << "      " << &last << " = " << last << "\n";
    // std::cout << &department << " = " << department << "\n\n";    
    // takeUserInput(first,last);
    // std::cout << &first << " = " << first << "      " << &last << " = " << last << "\n";

    Person p1(first,last);
    Employee p2(first,last,department);

    people.push_back(&p1);
    people.push_back(&p2);

    // std::cout << "vector People = " << &people << "\n";
    Person::vectorPrintInfo(people);
    Person::vectorPrintInfo(people);
    Person::vectorPrintInfo(people);

    // p1.printInfo();
    // p2.printInfo();
    
    // p2.setDepartment(department);
    // std::cout << "getDepartment = " << p2.getDepartment() << "\n";
    
    // std::cout << "getName = " << p2.getName() << "\n";
    // p2.printFullName();

    return 0;
}
void takeUserInput(std::string &first,std::string &last){

    std::cout << "Enter your First Name: ";
    std::cin >> first;
    std::cout << "Enter your Last Name: ";
    std::cin >> last;

    // std::cout << &first << " = ." << first << ".      " << &last << " = ." << last << ".\n";

}