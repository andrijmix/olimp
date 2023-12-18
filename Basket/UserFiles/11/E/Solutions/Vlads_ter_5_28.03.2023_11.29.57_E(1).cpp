#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

int main()
{
    int c=10,p=0;
    string n[1];
    cout<<"Ведіть вагу :"<<endl;
    cin>>n[0];
        for(int i=0; i<n[0].size()-3;i++){
            cout<<n[0][i];
        }
        cout<<" ";
    for(long j=n[0].size()-3; j<n[0].size();j++){
        cout<<n[0][j];
    }
    
  
    return 0;
}
