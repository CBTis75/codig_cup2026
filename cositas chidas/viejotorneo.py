combate1 = list(map(int, input().split()))
combate2 = list(map(int, input().split()))
combate3 = list(map(int, input().split()))
def gana(combate):
    return sum(combate) >= 2
g1 = gana(combate1)
g2 = gana(combate2)
g3 = gana(combate3)

if g1 and (g2 or g3):
    print("SI")
else:
    print("NO")