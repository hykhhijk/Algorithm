// EOF�� ���� �Է����� ����
// https://takeknowledge.tistory.com/20

#include <iostream>
using namespace std;

int main(){
    int A,B;
    for(;true;){
        cin >> A >> B;
        if(cin.eof() == true)
            break;
    cout << A + B << "\n";
    }
}