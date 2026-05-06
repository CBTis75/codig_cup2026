N = int(input())

Frutas = 0
Insectos = 0
Peces = 0
Carnaza = 0
Basura = 0
Huevos = 0
Anfibios = 0

for _ in range(N):
    sonido = input().strip()

    if sonido == "Yum-yum!":
        Frutas += 1
    elif sonido == "Crunch-crunch!":
        Insectos += 1
    elif sonido == "Gulp-gulp!":
        Peces += 1
    elif sonido == "Sniff-yom!":
        Carnaza += 1
    elif sonido == "Munch-munch!":
        Basura += 1
    elif sonido == "Crack-slurp!":
        Huevos += 1
    elif sonido == "Ribbit-yom!":
        Anfibios += 1

print("Frutas:", Frutas)
print("Insectos:", Insectos)
print("Peces:", Peces)
print("Carnaza:", Carnaza)
print("Basura:", Basura)
print("Huevos:", Huevos)
print("Anfibios:", Anfibios)