n = input("Digite um número inteiro: ")

soma = 0
digito = 0
counter = len(n)

while counter > 0:
    digito = (int(n) // 10**(len(n) - counter)) % 10
    soma = soma + digito
    counter -= 1

print(soma)

# Versão 2:

"""
x = input("Digite um valor: ")

soma = 0
i = 0
k = 10

while i <= len(x):

    recorte = int(x) % k
    recorte = recorte // (k/10)
    soma = soma + recorte

    k=k*10
    i= i+1
print(f"A soma dos digitos: {soma}\n")
"""

# Versão 3:

"""
x = input("Digite um valor: ")
soma = 0
numero = int(x)

while numero > 0:
    soma += numero % 10
    numero = numero // 10

print(f"A soma dos dígitos: {soma}")
"""







