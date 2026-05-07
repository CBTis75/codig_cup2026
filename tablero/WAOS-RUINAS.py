import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    n = int(entrada[0])
    llave = entrada[1]
    valores = entrada[2:]
    
    final = ""
    tam_llave = len(llave)
    
    for i in range(n):
        actual = int(valores[i])
        char_llave = llave[i % tam_llave]
        resta = ord(char_llave)
        
        while actual > 90:
            actual -= resta
            
        final += chr(actual)
        
    sys.stdout.write(final + '\n')

if __name__ == '__main__':
    main()