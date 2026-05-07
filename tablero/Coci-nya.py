import sys

def resolver():
    # Lectura rápida de todos los datos
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    n = int(entrada[0])
    objetivo = int(entrada[1])
    valores = [int(x) for x in entrada[2:n+2]]
    
    # Mapa de frecuencias de sumas prefijas
    frecuencias = {0: 1}
    suma_acumulada = 0
    total_subarreglos = 0
    
    for v in valores:
        suma_acumulada += v
        
        # Si (suma_acumulada - objetivo) existe, encontramos subarreglos válidos
        diferencia = suma_acumulada - objetivo
        if diferencia in frecuencias:
            total_subarreglos += frecuencias[diferencia]
        
        # Actualizamos el conteo de la suma actual
        frecuencias[suma_acumulada] = frecuencias.get(suma_acumulada, 0) + 1

    sys.stdout.write(str(total_subarreglos) + '\n')

if __name__ == "__main__":
    resolver()