#include <iostream>

#define LEN 5

int BubbleSort() {
	int ToSort[LEN] = {4,12,9,1,71};
	int Temp;
	bool Sorted = false;
	
	while (not Sorted) {
		Sorted = true;
		for (int i = 0; i <= LEN; i++) {
			for (int index = 0; i < LEN - 1 - i; i++) {
				if (ToSort[i] > ToSort[i + 1]) {
					Temp = ToSort[i];
					ToSort[i] = ToSort[i + 1];
					ToSort[i + 1] = Temp;
					Sorted = false;
				};
			};
		};
	};
	
	for (int i = 0; i < LEN; i++) {
		std::cout << ToSort[i] << std::endl;
	};

	return 1;
};

int main() {
	BubbleSort();
	return 0;
};
