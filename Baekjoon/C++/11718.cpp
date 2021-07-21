// string과 같은 연속적인 출력에서는 cin.eof == true 가아닌
//getline, getchar, scanf와 같은 입력함수를 while문 안에 넣어서 출력 값or == EOF 를 통해 루프 돌리기


#include <iostream>
using namespace std;

int main(){
    int key;
    char a[101];
    while(1){       //getline()를 넣어 코드 간소화 가능
        key = getchar();
        if(key == EOF)
            break;
        putchar(key);
        
    }
}