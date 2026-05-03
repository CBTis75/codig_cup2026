import sys

sectores = list(map(int, sys.stdin.readline().strip().split()))
indice = int(sys.stdin.readline().strip())

print(sectores[indice - 1])