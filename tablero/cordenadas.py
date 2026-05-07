x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
base = abs(x2 - x1)
altura = abs(y1 - y4)
area = base * altura
print(area)