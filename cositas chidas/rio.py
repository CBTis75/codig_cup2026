import sys
for linea in sys.stdin:
    v, t = map(int, linea.split())
    print(v * t)