import sys

def main():
    lineas = sys.stdin.read().splitlines()
    if not lineas:
        return
    
    total = int(lineas[0])
    muestras = lineas[1:total+1]
    
    # Mapa de sonidos a categorías
    tabla = {
        "Yum-yum!": "Frutas",
        "Crunch-crunch!": "Insectos",
        "Gulp-gulp!": "Peces",
        "Sniff-yom!": "Carnaza",
        "Munch-munch!": "Basura",
        "Crack-slurp!": "Huevos",
        "Ribbit-yom!": "Anfibios"
    }
    
    # Registro de resultados
    resumen = {cat: 0 for cat in tabla.values()}
    
    for s in muestras:
        sonido = s.strip()
        if sonido in tabla:
            categoria = tabla[sonido]
            resumen[categoria] += 1

    # Salida organizada
    orden = ["Frutas", "Insectos", "Peces", "Carnaza", "Basura", "Huevos", "Anfibios"]
    for item in orden:
        print(f"{item}: {resumen[item]}")

if __name__ == "__main__":
    main()