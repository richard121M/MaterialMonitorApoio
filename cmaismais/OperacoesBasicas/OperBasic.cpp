#include <iostream>
using namespace std;

int main(){

    float a, b;
    cout << "Digite dois numeros reais:" << endl;
    cin >> a >> b;
    
    float soma = a + b;
    cout << "(+) A Soma de " << a << " mais " << b << " eh : " << soma << endl;
    
    float subtracao = a - b;
    cout << "(-) A Subitracao de " << a << " menos " << b << " eh : " << subtracao << endl;
    
    float multiplicacao = a*b;
    cout << "(*) A Multiplicacao de " << a << " vezes " << b << " eh : " << multiplicacao << endl;
    
    float divisao = a/b;
    cout << "(/) A divisao de " << a << " dividido por " << b << " eh : " << divisao << endl;
    

    return 0;
}