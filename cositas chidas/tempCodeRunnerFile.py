while True:
    try:
        v = int(input())
        inter = int(input())
        
        if v < 0 or inter < 0:
            print("Datos inválidos")
            continue
        
        break
    except:
        print("Ingresa números enteros válidos")

tiempo = v * inter
print(tiempo)