// 9,10번 줄을 typing하고 <<endl대신 <<'\n'을 사용하여 연산 시간 최소화가능
#include <iostream>
using namespace std;



int main(){
cin.tie(NULL);
ios::sync_with_stdio(false);

int T;
cin >> T;
int num[2];
for(int i = 0; i < T; i++){
    cin >> num[0] >> num[1];
    cout << num[0] + num[1]<<'\n';
}
}
