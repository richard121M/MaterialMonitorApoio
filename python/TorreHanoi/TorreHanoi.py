n, origem, auxiliar, destino = [p.strip() for p in input().split(',')]

def torre_de_hanoi(n, origem, auxiliar, destino):
    if (n == 1):
        print(f"Mover disco de {origem} para {destino}")
    else:
        torre_de_hanoi(n-1, origem, destino,auxiliar)
        print(f"Mover disco de {origem} para {destino}")
        torre_de_hanoi(n-1,auxiliar , origem, destino)

torre_de_hanoi(int(n), origem, auxiliar, destino)