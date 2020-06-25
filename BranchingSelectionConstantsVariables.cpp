#include <iostream>
#include <string>


#define A = 96 // Constant
const int b = 7; // Constant

int main() {
	int c = 100; // Integer var
	std::string str = "Hello world!"; // String var etc.

	// Selection
	if (b < c) {
		std::cout << b << " < " << c;
	} else if (b > c) {
		std::cout << b << " > " << c;
	} else {
		std::cout << b << " == " << c;
	};

	for (int i = 0; i < c; i++) {
		if (i == b) {
			continue; // Branching
		}else if(i == 67) {
			break; // Branching
		};
		std::cout << i;
	};

}
