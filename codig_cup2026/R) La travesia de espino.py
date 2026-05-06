E = int(input())
data = input().split()

energia = E
distancia = 0

for x in data:
    if x == 'X':
        break

    x = int(x)

    if x == 0:
        energia += 1
        distancia += 1

    elif x > 0:  # subida
        energia -= x
        if energia < 0:
            print("Energía agotada :'(")
            print(f"{distancia} unidades de distancia")
            exit()

    else:  # bajada
        h = abs(x)

        if h > 5:
            print("Caída peligrosa!")
            print(f"{distancia} unidades de distancia")
            exit()

        energia -= (2 ** h)

        if energia < 0:
            print("Energía agotada :'(")
            print(f"{distancia} unidades de distancia")
            exit()

print("Ha llegado!")
print(f"{distancia} unidades de distancia")
print(f"{energia} unidades de energia restante")