import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    juegos = {}
    output = []
    
    for _ in range(n):
        datos = input().split()
        
        if datos[0] == '1':
            id_juego = int(datos[1])
            minutos = int(datos[2])
            juegos[id_juego] = juegos.get(id_juego, 0) + minutos
        else:
            id_juego = int(datos[1])
            total = juegos.get(id_juego, 0)
            
            horas = total // 60
            mins = total % 60
            
            output.append(f"{horas}:{mins:02d}")
    
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()