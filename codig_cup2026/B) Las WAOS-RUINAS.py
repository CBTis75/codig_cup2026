n = int(input())
clave = input().strip()
numeros = list(map(int, input().split()))

resultado = ""

for i in range(n):
    num = numeros[i]
    letra_clave = clave[i % len(clave)]
    valor_ascii = ord(letra_clave)

    while num > 90:
        num -= valor_ascii

    resultado += chr(num)

print(resultado)