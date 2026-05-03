import sys
input = sys.stdin.readline

n = int(input())

def es_primo(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

num = n + 1
while num <= 999:
    if es_primo(num):
        break
    num += 1

if num > 999:
    s = "000"
else:
    s = str(num).zfill(3)

digitos = {
    '0': ["***","* *","* *","* *","***"],
    '1': ["  *"," **","  *","  *","  *"],
    '2': ["***","  *","***","*  ","***"],
    '3': ["***","  *","***","  *","***"],
    '4': ["* *","* *","***","  *","  *"],
    '5': ["***","*  ","***","  *","***"],
    '6': ["***","*  ","***","* *","***"],
    '7': ["***","  *","  *","  *","  *"],
    '8': ["***","* *","***","* *","***"],
    '9': ["***","* *","***","  *","***"]
}

out = []
for fila in range(5):
    linea = digitos[s[0]][fila] + " " + digitos[s[1]][fila] + " " + digitos[s[2]][fila]
    out.append(linea)

sys.stdout.write("\n".join(out))