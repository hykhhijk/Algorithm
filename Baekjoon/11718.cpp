// string�� ���� �������� ��¿����� cin.eof == true ���ƴ�
//getline, getchar, scanf�� ���� �Է��Լ��� while�� �ȿ� �־ ��� ��or == EOF �� ���� ���� ������


#include <iostream>
using namespace std;

int main(){
    int key;
    char a[101];
    while(1){       //getline()�� �־� �ڵ� ����ȭ ����
        key = getchar();
        if(key == EOF)
            break;
        putchar(key);
        
    }
}