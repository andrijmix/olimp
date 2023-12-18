#include <iostream>
#include <string>

using namespace std;

int
main ()
{
  string a;
  int n;
  cout << "Enter n:";
  cin >> n;
  cout<<"Enter word:";
  getline(cin, a);
  cin>>a;
  for (int i=1; i<=n; i++)
  {
      cout<<a<<" ";
  }
  return 0;
}
