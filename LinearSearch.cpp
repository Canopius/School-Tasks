
#include <iostream>
#define LEN  5

// Linear search
int LinearSearch(int ToFind) {
	int ToSearch[LEN] = {2,5,7,10,12};
	
	for (int i = 0; i < LEN; i++) {
		if (ToSearch[i] == ToFind) {
			return i;
		};
	};
	return false;
}

int main() {
	int Location = LinearSearch(7);
	std::cout << Location;
	return 0;
}
