def decimal_to_binary(numeroDec):
    if (numeroDec == 0): 
        return 0
    decimal_to_binary(int(numeroDec/2));
    print(int(numeroDec%2),end="")

def binary_to_decimal(numeroBin):
    tam = len(numeroBin)
    if (tam == 0):
        return 0
    soma = int(numeroBin[0])*(2**(tam-1)) + binary_to_decimal(numeroBin[1:])
    return soma
    
num = int(input())
print(num, "em binario eh",end=" ")
decimal_to_binary(num)
print("")

numBin = input("digite um numero em binario:")
print(numBin, "em Decimal eh",end=" ")
print(binary_to_decimal(numBin))