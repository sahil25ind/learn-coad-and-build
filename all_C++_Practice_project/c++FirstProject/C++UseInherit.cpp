#include <iostream>
#include <cmath>

class shape{
	public:
		double area;
		double volume;
};
class cube:public shape{
	// private:
	public:
		double side;
	// public:
		cube(double side):side(side) {
			// this -> side = side;
            cubeArea();
            cubeVolume();
		}
		// cube(){	//this is a default constructor hoprfully	
			
		// }
		cube() = default;	// this is a default constructor i'am sure of it i think
		
		void cubeArea() {
			this -> area = 6 * (pow(side,2));
			// this -> area = 6 * side * side;
		}
		void cubeVolume() {
			this -> volume = pow(side,3);
			// this -> volume = side * side * side;
		}

};
class spheare:public shape{
	public:
		spheare(double radius){
			spheareArea(radius);
			spheareVolume(radius);
		}
		void spheareArea(double radius) {
			this -> area = 4 * 3.14159 * (radius * radius);
			// this -> area;
		}
		void spheareVolume(double radius) {
			this -> volume = 4/(double)3 * 3.14159 * (radius * radius * radius);
            // this -> volume = (4/(double)3) * 3.14159 * (radius * radius * radius);
		}
};

int main(){

	cube cube1(2.235);
	std::cout << "cube1 area = " << cube1.area  << "cm^2    cube1 volume = " << cube1.volume << "cm^3" << std::endl;

	spheare spheare1(1.289);
    std::cout << "spheare1 area = " << spheare1.area  << "cm^2    spheare1 volume = " << spheare1.volume << "cm^3" << std::endl;

    return 0;
}
