n = int(input())
criticas = list(map(int, input().split()))

k = int(input())
buscadas = list(map(int, input().split()))

contador = 0

for x in buscadas:
    if x in criticas:
        contador += 1

print(contador)