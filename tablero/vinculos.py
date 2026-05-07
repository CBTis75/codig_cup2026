import sys

def procesar():
    linea = sys.stdin.readline().strip()
    if not linea:
        return
        
    favoritos = linea.count('7') + linea.count('3')
    rechazo = linea.count('0')
    
    sys.stdout.write(f"{favoritos} {rechazo}\n")

if __name__ == "__main__":
    procesar()