// 9,10�� ���� typing�ϰ� <<endl��� <<'\n'�� ����Ͽ� ���� �ð� �ּ�ȭ����
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
