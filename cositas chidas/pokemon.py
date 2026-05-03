import math
tx, ty = map(int, input().split())
ax, ay = map(int, input().split())
mx, my = map(int, input().split())
n = int(input())
def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)
total = 0
bestA = bestA2 = -float('inf')
bestM = bestM2 = -float('inf')
idxA = idxA2 = -1
idxM = idxM2 = -1
for i in range(n):
    x, y = map(int, input().split())
    d_t = dist(tx, ty, x, y)
    total += 2 * d_t
    ahorroA = d_t - dist(ax, ay, x, y)
    ahorroM = d_t - dist(mx, my, x, y)
    if ahorroA > bestA:
        bestA2, idxA2 = bestA, idxA
        bestA, idxA = ahorroA, i
    elif ahorroA > bestA2:
        bestA2, idxA2 = ahorroA, i
    if ahorroM > bestM:
        bestM2, idxM2 = bestM, idxM
        bestM, idxM = ahorroM, i
    elif ahorroM > bestM2:
        bestM2, idxM2 = ahorroM, i
res = total
res = min(res, total - bestA)
res = min(res, total - bestM)
if idxA != idxM:
    res = min(res, total - bestA - bestM)
else:
    res = min(res, total - bestA - bestM2)
    res = min(res, total - bestA2 - bestM)

print(f"{res:.9f}")