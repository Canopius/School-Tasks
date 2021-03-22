#include <iostream>
#include <cmath>

class Triangle {
	int width, height;
	public:
		void set_values(int, int);
		float area() { return 0.5 * width * height;}
};

void Triangle::set_values (int x, int y){
	width = x;
	height = y;
};

class Circle {
	const double pi = atan(1)*4;
	int radius;
	public:
		void set_values(int);
		float area() {return pi * pow(radius,2);}
};

void Circle::set_values (int r){
	radius = r;
};

class Rectangle {
    int width, height;
  public:
    void set_values (int,int);
    int area() {return width*height;}
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}

int main () {
	Rectangle rect;
	rect.set_values (3,4);

	Circle cir;
	cir.set_values(9);

	Triangle tri;
	tri.set_values(2,5);

	std::cout << "Rectangle area: " << rect.area() << std::endl;
	std::cout << "Circle area: " << cir.area() << std::endl;
	std::cout << "Triangle area: " << tri.area() << std::endl;
	return 0;
}
