#include <iostream>
using namespace std;

int main(){

    // o objetivo dessa questao eh consegui inverter a ordem dos numero
    // de um numero interio sem usar string e sem converte para string
    // nao use o str()

    // exemplo: se o usuario digitar 2578, seu programa deve imprimir 8752

    int num;
    cin >> num;
    while(num > 0){
        cout << num%10;
        num /= 10;
    }
    
    return 0;
}