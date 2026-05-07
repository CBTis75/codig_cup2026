import sys

def resolver():
    entrada = sys.stdin.read().split()
    
    if not entrada:
        return
        
    limite = int(entrada[0])
    total_equipos = int(entrada[1])
    detalles = entrada[2:]
    
    contador = 0

    for i in range(0, total_equipos * 3, 3):
        if i + 2 >= len(detalles):
            break
            
        costo = int(detalles[i])
        memoria = int(detalles[i+1])
        almacenamiento = int(detalles[i+2])
        
        filtro_precio = costo <= limite
        filtro_ram = memoria in [8, 16]
        filtro_disco = almacenamiento >= 500
        
        if filtro_precio and filtro_ram and filtro_disco:
            contador += 1
            
    sys.stdout.write(str(contador) + '\n')

if __name__ == "__main__":
    resolver()