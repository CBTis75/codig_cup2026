import sys

def main():
    dato = sys.stdin.read().strip()
    if not dato:
        return

    si = dato.count('7') + dato.count('3')
    no = dato.count('0')

    print(f"{si} {no}")

if __name__ == "__main__":
    main()