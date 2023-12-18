#include <iostream>
using namespace std;

int main() 
{
    int n;
    string phrase;
    
    cout << "Введіть фразу: ";
    getline(cin, phrase);
    
    cout << "Скільки разів повторити фразу? ";
    cin >> n;

    for (int i = 0; i < n; i++) 
    {
        cout << phrase;
        if (i < n-1) 
        {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}