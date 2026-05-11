from itertools import combinations

def colineales(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)

# Leer puntos
puntos = [tuple(map(int, input().split())) for _ in range(6)]

# Probar combinaciones de 3 puntos
for comb in combinations(range(6), 3):
    grupo1 = list(comb)
    grupo2 = [i for i in range(6) if i not in grupo1]

    # Verificar ambos grupos
    if colineales(puntos[grupo1[0]], puntos[grupo1[1]], puntos[grupo1[2]]) and \
       colineales(puntos[grupo2[0]], puntos[grupo2[1]], puntos[grupo2[2]]):

        # Crear respuesta
        res = [0]*6

        # Asegurar que el punto 0 esté en grupo 1
        if 0 in grupo2:
            grupo1, grupo2 = grupo2, grupo1

        for i in grupo1:
            res[i] = 1
        for i in grupo2:
            res[i] = 2

        print("SI")
        for x in res:
            print(x)
        exit()

print("NO")