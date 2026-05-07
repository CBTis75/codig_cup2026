import sys

def principal():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    referencia = set(map(int, data[1:n+1]))
    
    q_pos = n + 1
    if q_pos >= len(data):
        return
        
    objetivos = list(map(int, data[q_pos+1:]))
    
    total = 0
    for elemento in objetivos:
        if elemento in referencia:
            total += 1
            
    sys.stdout.write(f"{total}\n")

if __name__ == "__main__":
    principal()