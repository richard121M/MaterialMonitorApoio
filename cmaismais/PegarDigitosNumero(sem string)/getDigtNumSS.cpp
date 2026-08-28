#include <iostream>
using namespace std;

int main(){

    // esse programa só considera numeros com 5 digitos
    // e nao utiliza loops, eh so para mostrar com pega os
    // digitos sem usar string
    int num;
    cin >> num;
    int e = num%10;
    num = num/10;
    int d = num%10;
    num = num/10;
    int c = num%10;
    num = num/10;
    int b = num%10;
    int a = num/10;

    cout << a << "  " << b << "  " << c << "  " << d << "  " << e << endl;
    
    return 0;
}