import sys

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return [p for p, prime in enumerate(is_prime) if prime]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    
    queries = []
    for _ in range(t):
        tipo = int(input_data[ptr])
        v1 = int(input_data[ptr+1])
        v2 = int(input_data[ptr+2])
        queries.append((tipo, v1, v2))
        ptr += 3

    prime_list = sieve(2000000)

    for op, val1, val2 in queries:
        if op == 0:
            x, y = val1, val2
        else:
            x = prime_list[val1 - 1]
            y = prime_list[val2 - 1]
        
        mayor = x if x > y else y
        menor = y if x > y else x
        
        sys.stdout.write(f"{mayor - 1} {menor}\n")

if __name__ == "__main__":
    solve()