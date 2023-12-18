#include <iostream>

using namespace std;

int main() {
    int numbers[20];

    for (int i = 0; i < 20; ++i) {
        std::cin >> numbers[i];
    }

    int count = 0;
    for (int i = 0; i < 20; ++i) {
        if (numbers[i] % 7 == 0 && numbers[i] % 5 != 0) {
            cout << numbers[i] << " ";
            count++;
        }
    }

    return 0;
}