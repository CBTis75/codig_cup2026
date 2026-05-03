n = int(input())
s = input()
nums = list(map(int, input().split()))

resultado = ""

for i in range(n):
    num = nums[i]
    letra = s[i % len(s)]
    valor = ord(letra)
    
    while num > ord('Z'):
        num -= valor
    
    resultado += chr(num)

print(resultado)