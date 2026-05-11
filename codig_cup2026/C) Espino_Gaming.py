t = int(input())
juegos = {}

for _ in range(t):
    datos = list(map(int, input().split()))

    if datos[0] == 1:
        _, id_juego, minutos = datos

        if id_juego not in juegos:
            juegos[id_juego] = 0

        juegos[id_juego] += minutos

    else:
        _, id_juego = datos

        total = juegos.get(id_juego, 0)

        horas = total // 60
        minutos = total % 60

        print(f"{horas}:{minutos:02d}")