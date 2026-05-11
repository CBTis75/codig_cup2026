import math

tx, ty = map(int, input().split())
ax, ay = map(int, input().split())
mx, my = map(int, input().split())

n = int(input())

base = 0
mejorA = float('inf')
mejorM = float('inf')

for _ in range(n):
    x, y = map(int, input().split())
    
    dT = math.hypot(x - tx, y - ty)
    base += 2 * dT
    
    a = math.hypot(x - ax, y - ay) - dT
    m = math.hypot(x - mx, y - my) - dT
    
    mejorA = min(mejorA, a)
    mejorM = min(mejorM, m)

# opciones:
res = base
res = min(res, base + mejorA)
res = min(res, base + mejorM)
res = min(res, base + mejorA + mejorM)

print(res)