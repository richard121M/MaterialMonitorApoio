m = []
numLinhas = int(input('numero de linhas: '))
numColunas = int(input('numero de colunas: '))

for  i in range(numLinhas):
    m.append([])
    for _ in range(numColunas):
        vel = int(input())
        m[i].append(vel)

print('Sua Matris:')
for  i in range(numLinhas):
    print('[',end='')
    for j in range(numColunas):
        print(m[i][j],end='')
        if (j < numColunas-1):
            print(', ',end='')
    print(']')
