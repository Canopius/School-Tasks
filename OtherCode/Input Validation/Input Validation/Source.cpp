#include <iostream>
#include <string>

class Response {
public:
    int age;
    std::string name;
    std::string emailAddress;
};

bool checkAge(int age) {
    if (age < 16 || age > 100) {
        std::cout << std::endl << "Age is not within the valid range!";
        return true;
    }
    else {
        return false;
    }
}

int requestAge() {
    int age;
    bool noAge = true;
    std::cout << "Please enter your age: ";
    std::cin >> age;
    noAge = checkAge(age);
    while (std::cin.fail() || (noAge)) {
        std::cout << std::endl << "Please enter your age: ";
        std::cin.clear();
        std::cin.ignore(256, '\n');
        std::cin >> age;
        noAge = checkAge(age);
    }
    return age;
}

int main() {
    
    Response newResponse;

    std::cout << "Please enter your name: ";
    std:: cin >> newResponse.name

    newResponse = requestAge()

    return 0;
}
