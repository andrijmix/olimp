#include <iostream>
#include <string>

using namespace std;

int main()
{
    int count_of_repeats;

    cin >> count_of_repeats;

    string str;

    cin >> str;

    for (int i = 0; i < count_of_repeats; i++)
    {
        cout << str << " ";
    }

    return 0;
}