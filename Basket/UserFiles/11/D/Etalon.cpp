#include <iostream>
using namespace std;

int main()
{
	int g;
	cin >> g;
	int kg = g / 1000;
	g = g-(kg * 1000);
	cout << kg <<" " << g;
}