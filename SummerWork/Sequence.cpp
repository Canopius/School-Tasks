#include <iostream>

using namespace std; // Bad practice but does not matter here

int main() {
	string Name;
	cout << "Hello, what is your name?\n";
	cin >> Name;

	cout << "\nHello " + Name;
}
