n = int(input())

for i in range(n, 0, -1):
    print(", ".join(["Ay"] + ["ay"] * (i - 1)) + ".")

print("Por los arrayanes")
print("se pasea nadie.")