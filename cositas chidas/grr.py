n = int(input())
sonidos = {
    "Yum-yum!": "Frutas",
    "Crunch-crunch!": "Insectos",
    "Gulp-gulp!": "Peces",
    "Sniff-yom!": "Carnaza",
    "Munch-munch!": "Basura",
    "Crack-slurp!": "Huevos",
    "Ribbit-yom!": "Anfibios"
}
conteo = {
    "Frutas": 0,
    "Insectos": 0,
    "Peces": 0,
    "Carnaza": 0,
    "Basura": 0,
    "Huevos": 0,
    "Anfibios": 0
}

for _ in range(n):
    s = input().strip()
    if s in sonidos:
        alimento = sonidos[s]
        conteo[alimento] += 1

# Imprimir en el orden solicitado
print(f"Frutas: {conteo['Frutas']}")
print(f"Insectos: {conteo['Insectos']}")
print(f"Peces: {conteo['Peces']}")
print(f"Carnaza: {conteo['Carnaza']}")
print(f"Basura: {conteo['Basura']}")
print(f"Huevos: {conteo['Huevos']}")
print(f"Anfibios: {conteo['Anfibios']}")