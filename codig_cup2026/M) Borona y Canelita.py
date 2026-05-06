import sys
input = sys.stdin.readline

def generar_primos(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(n+1) if sieve[i]]

primos = generar_primos(200000)

t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    
    if data[0] == 0:
        a, b = data[1], data[2]
    else:
        x, y = data[1], data[2]
        a = primos[x-1]
        b = primos[y-1]

    n = a + b

    if n <= 1:
        print("0 0")
        continue

    canelita = min(n-1, 2 * min(a, b))
    borona = (n - 1) - canelita

    print(borona, canelita)