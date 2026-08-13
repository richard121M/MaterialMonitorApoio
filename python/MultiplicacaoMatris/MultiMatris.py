#criar um programa que faca a multiplicacao de duas matrizes quadradas

size = int(input("digite a orde das matrizes quadradas"))
Amatris = []
for i in range(size):
    Amatris.append([])
    for j in range(size):
        valor = int(input(f"valor da posicao {i},{j} :"))
        Amatris[i].append(valor)

print("Matris A: ")
for i in range(size):
    print(Amatris[i])