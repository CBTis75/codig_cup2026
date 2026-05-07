import sys

def es_primo(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    p = 3
    while p * p <= num:
        if num % p == 0:
            return False
        p += 2
    return True

def principal():
    entrada = sys.stdin.readline().strip()
    if not entrada:
        return
        
    n = int(entrada)
    objetivo = n + 1
    
    while objetivo <= 999:
        if es_primo(objetivo):
            break
        objetivo += 1
        
    cadena = str(objetivo).zfill(3) if objetivo <= 999 else "000"
    
    fuente = {
        '0': ["***","* *","* *","* *","***"],
        '1': ["  *"," **","  *","  *","  *"],
        '2': ["***","  *","***","* ","***"],
        '3': ["***","  *","***","  *","***"],
        '4': ["* *","* *","***","  *","  *"],
        '5': ["***","* ","***","  *","***"],
        '6': ["***","* ","***","* *","***"],
        '7': ["***","  *","  *","  *","  *"],
        '8': ["***","* *","***","* *","***"],
        '9': ["***","* *","***","  *","***"]
    }
    
    for f in range(5):
        bloque = [fuente[d][f] for d in cadena]
        sys.stdout.write(" ".join(bloque) + "\n")

if __name__ == "__main__":
    principal()