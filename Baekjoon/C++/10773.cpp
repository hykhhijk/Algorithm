//vector를 사용하면 자료구조 연산 매우간단

#include <iostream>
#include <vector>
using namespace std;

int main(){
    int cases,num, count = 0;
    vector <int> money;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cin >> num;
        if(num == 0){
            count -= money[money.size()-1];
            money.pop_back();
        }
        else{
            count += num;
            money.push_back(num);
        }
    }
    cout << count;
}