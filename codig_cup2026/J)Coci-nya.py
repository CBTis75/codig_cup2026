n, k = map(int, input().split())

suma = 0
conteo = 0
vistos = {0: 1}

for _ in range(n):
    x = int(input())
    suma += x

    conteo += vistos.get(suma - k, 0)

    vistos[suma] = vistos.get(suma, 0) + 1

print(conteo)