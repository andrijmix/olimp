#include <iostream>

using namespace std;

int main()
{
    int n;
    string str;
    std::cin >> n;
    std::cin >> str;
    for (int count = 0; count < n; ++count)
		std::cout << str << " ";
    return 0;
}