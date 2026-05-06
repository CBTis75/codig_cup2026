numero = input().strip()

favoritos = 0
odiado = 0

for digito in numero:
    if digito == '7' or digito == '3':
        favoritos += 1
    elif digito == '0':
        odiado += 1

print(favoritos, odiado)