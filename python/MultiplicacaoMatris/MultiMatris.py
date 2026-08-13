#crie um programa que faca a multiplicacao de duas matrizes quadradas

def PrintMatris(matris,size):
    for i in range(size):
        print(matris[i])

def EscreverMatris(matris,size,nomeMatris):
    for i in range(size):
        #criando as linhas dentro do vetor para virar uma matris
        matris.append([])
        for j in range(size):
            valor = int(input(f"{nomeMatris} valor da posicao {i},{j} :"))
            #adicionando o valor dentro da linha para criar as colunas 
            matris[i].append(valor)

#Pedindo o valor da ordem da matris
SIZE = int(input("digite a ordem das matrizes quadradas"))

#Declarando a matris A
Amatris = []
EscreverMatris(Amatris,SIZE,"Matris A")
print("Matris A: ")
PrintMatris(Amatris,SIZE)

#Declarando a matris B
Bmatris = []
EscreverMatris(Bmatris,SIZE,"Matris B")
print("Matris B: ")
PrintMatris(Bmatris,SIZE)

#Multiplicar
#Declarando a matris Produto
Produto = []
for Va in range(SIZE):
    Produto.append([])
    for Vb in range(SIZE):
        valor = 0
        for s in range(SIZE):
            valor += Amatris[Va][s]*Bmatris[s][Vb]
        Produto[Va].append(valor)

print("O produto de A*B é ")
PrintMatris(Produto,SIZE)
