from itertools import combinations
puntos = [tuple(map(int, input().split())) for _ in range(6)]
def colineales(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1)*(y3 - y1) == (x3 - x1)*(y2 - y1)
for comb in combinations(range(6), 3):
    i, j, k = comb
    if colineales(puntos[i], puntos[j], puntos[k]):
        resto = [x for x in range(6) if x not in comb]
        if colineales(puntos[resto[0]], puntos[resto[1]], puntos[resto[2]]):
            grupo = [0]*6
            for idx in comb:
                grupo[idx] = 1
            for idx in resto:
                grupo[idx] = 2
            if grupo[0] == 2:
                grupo = [1 if x == 2 else 2 for x in grupo]
            print("SI")
            for g in grupo:
                print(g)
            exit()
print("NO")