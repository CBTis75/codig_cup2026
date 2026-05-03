n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
conteo = {0: 1}  
suma = 0
resultado = 0
for num in arr:
    suma += num
    
    if (suma - k) in conteo:
        resultado += conteo[suma - k]
    
    conteo[suma] = conteo.get(suma, 0) + 1

print(resultado)