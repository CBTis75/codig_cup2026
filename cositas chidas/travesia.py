E = int(input())
ruta = input().split()
distancia = 0
for paso in ruta:
    if paso == 'X':
        print("Ha llegado!")
        print(f"{distancia} unidades de distancia")
        print(f"{E} unidades de energia restante")
        break
    paso = int(paso)
    if paso == 0:
        E += 1
        distancia += 1
    elif paso > 0:
        if E < paso:
            print("Energía agotada :'(")
            print(f"{distancia} unidades de distancia")
            break
        E -= paso
    else:
        d = abs(paso)
        if d > 5:
            print("Caída peligrosa!")
            print(f"{distancia} unidades de distancia")
            break
        E -= d * d
        if E < 0:
            print("Energía agotada :'(")
            print(f"{distancia} unidades de distancia")
            break