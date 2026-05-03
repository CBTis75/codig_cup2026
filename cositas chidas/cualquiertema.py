n = int(input())
criticas = set(map(int, input().split()))
q = int(input())
buscar = list(map(int, input().split()))
contador = 0
for x in buscar:
    if x in criticas:
        contador += 1

print(contador)