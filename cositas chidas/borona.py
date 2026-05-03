import sys
input = sys.stdin.readline

def criba(n):
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False
    
    primos = []
    for i in range(2, n + 1):
        if es_primo[i]:
            primos.append(i)
    
    return primos

t = int(input())

consultas = []
max_k = 0

for _ in range(t):
    datos = list(map(int, input().split()))
    consultas.append(datos)
    
    if datos[0] == 1:
        max_k = max(max_k, datos[1], datos[2])

# límite seguro (ajustable)
limite = 2000000
primos = criba(limite)

for q in consultas:
    tipo = q[0]
    
    if tipo == 0:
        a, b = q[1], q[2]
    else:
        i, j = q[1], q[2]
        a = primos[i - 1]
        b = primos[j - 1]
    
    borona = max(a, b) - 1
    canelita = min(a, b)
    
    print(borona, canelita)