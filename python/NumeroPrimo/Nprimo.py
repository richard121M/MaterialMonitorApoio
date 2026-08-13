#As varias formas de descobrir se
#um numero eh primo
#O algoritimo mais Rapido

#O algoritimo mais Rapido
def EhPrimo03(num):
    if (num <= 1):
        return False
    n = 2
    while (n*n <= num):
        if num%n == 0:
            return False
        n += 1
    return True

def EhPrimo02(num):
    if (num <= 1):
        return False
    for n in range(2,num):
        if num%n == 0:
            return False
    return True
    
def EhPrimo01(num):
    numDivisao = 0
    for n in range(1,num+1):
        if num%n == 0:
            numDivisao += 1
    if (numDivisao == 2):
        return True
    return False

num = int(input("digite um numero: "))
print("Eh primo 01: ",end="")
print(EhPrimo01(num))
print("Eh primo 02: ",end="")
print(EhPrimo02(num))
print("Eh primo 03: ",end="")
print(EhPrimo03(num))
# -> 2147483647
# -> 2305843009213693951