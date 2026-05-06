n = int(input())

def es_primo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

limite = 1000000  

primo = -1
for i in range(n+1, limite+1):
    if es_primo(i):
        primo = i
        break

if primo == -1:
    numero = "1000"
else:
    numero = str(primo)

digitos = {
    '0': [" ***","*  *","*  *","*  *"," ***"],
    '1': ["  * "," ** ","  * ","  * "," ***"],
    '2': [" ***","   *"," ***","*   "," ***"],
    '3': [" ***","   *"," ***","   *"," ***"],
    '4': ["*  *","*  *"," ***","   *","   *"],
    '5': [" ***","*   "," ***","   *"," ***"],
    '6': [" ***","*   "," ***","*  *"," ***"],
    '7': [" ***","   *","  * "," *  "," *  "],
    '8': [" ***","*  *"," ***","*  *"," ***"],
    '9': [" ***","*  *"," ***","   *"," ***"]
}

for fila in range(5):
    linea = []
    for d in numero:
        linea.append(digitos[d][fila])
    print(" ".join(linea))