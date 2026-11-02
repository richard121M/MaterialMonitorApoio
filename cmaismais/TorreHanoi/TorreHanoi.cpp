#include <iostream>

using namespace std;

void torre_de_hanoi(int n,char origem,char auxiliar,char destino){
    if (n == 1){
        cout << "Mover disco de "<<origem<<" para "<< destino << endl;
    }else{
        torre_de_hanoi(n-1, origem, destino,auxiliar);
        cout << "Mover disco de "<<origem<<" para "<< destino << endl;
        torre_de_hanoi(n-1,auxiliar , origem, destino);
    }
}

int main(){
    int n;
    char ori, aux, dest;
    cin >> n;
    cin >> ori >> aux >> dest;
    torre_de_hanoi(n,ori,aux,dest);
    return 0;
}