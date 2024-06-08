"""
Exercício 7

"""

x = int(input("Digite um valor: "))

# Par ou impar?
print("Par ou impar?\n")
if not(x%2):
    print("Valor digitado é PAR.\n")
else:
    print("Valor digitado é Impar.\n")

# O número digitado é divisível por 3? Caso contrário, imprima o mesmo número que foi dado na entrada.
print("Divisível por 3?\n")
if not(x%3):
    print("É divisível por 3.\n")
else:
    print(f"Não é divisível por 3. Valor digitado: {x}\n")

# O número digitado é divisível por 5? Caso contrário, imprima o mesmo número que foi dado na entrada.
if not(x%5):
    print("É divisível por 5.\n")
else:
    print(f"Não é divisível por 5. Valor digitado: {x}\n")

# O número digitado é divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
if not(x%5) and not(x%3):
    print("É divisível por 3 e 5.\n")
else:
    print(f"Não é divisível por 3 e 5. Valor digitado: {x}")

y = int(input("Digite um valor: "))
z = int(input("Digite mais um valor: "))


print("Ordenando de forma crescente os valores digitados:\n")
if x > y > z:
    print(z, y, x)

if x > z > y:
    print(y, z, x)

if y> x > z:
    print(z, x, y)

if y > z > x:
    print(x, z, y)

if z > x > y:
    print(y, x, z)

if z > y > x:
    print(x, y, z)
print()
