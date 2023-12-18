// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<string>
using namespace std;

int main()
{
    char s[81];
    string ss;
    cin.getline(s,81);
    string s1 = s;
    size_t pos = 0;
    while ((pos = s1.find(' ')) != std::string::npos) {
        ss = s1.substr(0, pos);
        if (stoi(ss)%7==0)
            if (stoi(ss) % 5 != 0)
                cout << ss << " ";
        s1.erase(0, pos + 1);
    }
    if (stoi(s1) % 7 == 0)
        if (stoi(s1) % 5 != 0)
            cout << s1 << " ";

}
