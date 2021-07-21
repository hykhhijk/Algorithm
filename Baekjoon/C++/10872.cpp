#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if(n==0){
        cout << 1;
        return 0;
    }
    else{
        int fibo=1;
        for(int i = 2; i <= n; i++){
            fibo *= i;
        }
        cout << fibo;
    }
}