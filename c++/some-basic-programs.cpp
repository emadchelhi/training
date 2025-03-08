#include <iostream>
using namespace std;

/*Program that only prints even numbers between 0 and 10*/
int main() {
    int i = 0;
    while (i <= 10) {
        cout << i << "\n";
        i += 2;
    }
    return 0;
}

/*Program that reverses a given number:*/
int main() {
    int number = 1234;
    int revnumber = 0;
    while (number) {
        revnumber = revnumber * 10 + number % 10;
        number /= 10;
    }
    cout << "Reversed numbers: " << revnumber << "\n";
    cin.get(); // For Linux/macOS users
    return 0;
}