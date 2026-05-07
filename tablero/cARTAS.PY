import sys
import math

def calcular():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    ptr = 0
    tx, ty = int(entrada[ptr]), int(entrada[ptr+1])
    ax, ay = int(entrada[ptr+2]), int(entrada[ptr+3])
    mx, my = int(entrada[ptr+4]), int(entrada[ptr+5])
    n = int(entrada[ptr+6])
    ptr += 7

    acumulado = 0
    infinito = float('inf')
    
    top_a = [(-infinito, -1), (-infinito, -1)]
    top_m = [(-infinito, -1), (-infinito, -1)]

    for i in range(n):
        px, py = int(entrada[ptr]), int(entrada[ptr+1])
        ptr += 2
        
        d_t = math.hypot(tx - px, ty - py)
        acumulado += 2 * d_t
        
        ganancia_a = d_t - math.hypot(ax - px, ay - py)
        ganancia_m = d_t - math.hypot(mx - px, my - py)

        if ganancia_a > top_a[0][0]:
            top_a[1] = top_a[0]
            top_a[0] = (ganancia_a, i)
        elif ganancia_a > top_a[1][0]:
            top_a[1] = (ganancia_a, i)

        if ganancia_m > top_m[0][0]:
            top_m[1] = top_m[0]
            top_m[0] = (ganancia_m, i)
        elif ganancia_m > top_m[1][0]:
            top_m[1] = (ganancia_m, i)

    mejor_resultado = min(acumulado - top_a[0][0], acumulado - top_m[0][0])

    if top_a[0][1] != top_m[0][1]:
        mejor_resultado = min(mejor_resultado, acumulado - top_a[0][0] - top_m[0][0])
    else:
        mejor_resultado = min(mejor_resultado, 
                              acumulado - top_a[0][0] - top_m[1][0], 
                              acumulado - top_a[1][0] - top_m[0][0])

    sys.stdout.write(f"{mejor_resultado:.12f}\n")

if __name__ == "__main__":
    calcular()