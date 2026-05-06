c1 = sum(map(int, input().split())) >= 2
c2 = sum(map(int, input().split())) >= 2
c3 = sum(map(int, input().split())) >= 2

if c1 and (c2 or c3):
    print("SI")
else:
    print("NO")