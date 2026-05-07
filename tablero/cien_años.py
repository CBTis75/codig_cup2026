import sys

def cantar():
    linea = sys.stdin.readline().strip()
    if not linea:
        return
    
    repeticiones = int(linea)
    
    for k in range(repeticiones, 0, -1):
        estrofa = ["Ay"] + ["ay"] * (k - 1)
        print(", ".join(estrofa) + ".")
        
    print("Por los arrayanes")
    sys.stdout.write("se pasea nadie.\n")

if __name__ == "__main__":
    cantar()