#include <iostream>

using namespace std;
#define MAX 20
void CoutMatris(int tam, int matris[MAX][MAX]){
    for (int i = 0 ; i< tam; i++){
        cout << "[ ";
        for (int j = 0 ; j < tam; j ++){
            cout << matris[i][j];
            if (j < tam-1){
                cout << " , ";
            }
        }
        cout << " ]" << endl;
    }
}

void EscreverMatris(int tam,int matris[MAX][MAX], char nomeMatris[]){
    for (int i = 0 ; i < tam; i++){
        for (int j = 0 ; j < tam; j++){
        //adicionando o valor dentro da linha para criar as colunas 
            cout << nomeMatris << " valor da posicao " << i << "," << j << " : "; 
            cin >> matris[i][j];
        }
    }
}

int main(){
    //ola mundo no C++
    int size;
    cout << "digite a ordem das matrizes quadradas: ";   
    cin >> size;

    int Amatris[MAX][MAX];
    //cin.ignore();
    EscreverMatris(size,Amatris,"Matris A");
    CoutMatris(size,Amatris);
    cout << "\n";
    int Bmatris[MAX][MAX];
    EscreverMatris(size,Bmatris,"Matris B");
    CoutMatris(size,Bmatris);
    cout << "\n";
    int Produto[MAX][MAX];
    int Va, Vb, s;
    for (Va = 0; Va< size; Va++){
        for(Vb = 0; Vb < size; Vb++){
            int valor = 0;
            for (s = 0; s < size; s++){
                valor += Amatris[Va][s]*Bmatris[s][Vb];
            }
            Produto[Va][Vb] = valor;
        }
    }
    cout << "O produto de A*B e: " << endl;
    CoutMatris(size,Produto);
    return 0;
}