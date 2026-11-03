#Parte da questao(nao alterada)
#============================================================#
import statistics

# Escreva calcular_media, calcular_desvio_padrao, calcular_nota_necessaria,
# avaliar_consistencia, gerar_ranking_prioridade e analisar_desempenho
notas = []
for _ in range(7):
    notas += [float(x) for x in input().split(',') if x.strip()]
#============================================================#

def somatorio(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + somatorio(lista[1:]) 
    
def calcular_media(notas):
    medias = []
    for i in range(7):
        somasUni01 = somatorio(notas[7*i:(7*i+3)])
        somasUni02 = somatorio(notas[(7*i+3):(7*i+6)])
        medias += [somasUni01/3,somasUni02/3]
    return medias

def calcular_nota_necessaria(media1, media2):
    return 3 * 5.0 - (media1 + media2)

medias = calcular_media(notas)
terceiraUnidade = []
for i in range(7):
    terceiraUnidade.append(calcular_nota_necessaria(medias[2*i], medias[2*i+1]))
print(terceiraUnidade)
# Chame analisar_desempenho com as notas e as cinco funções
