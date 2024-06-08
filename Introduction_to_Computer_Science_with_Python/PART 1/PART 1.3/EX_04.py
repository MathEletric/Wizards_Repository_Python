n = int(input("Digite um número inteiro: "))

counter = n
i = 0

while counter > 0:
    if n % counter == 0:
        i += 1
    counter -= 1
if i <= 2:
    print("primo")
else:
    print("não primo")

# Versão 2:

"""
n = int(input("Digite um número: "))

num = n
primo = True

while num:
    if n % num == 0 and num != n and num != 1:
        primo = False
    num -= 1
if primo:
    print("É primo.\n")
else:
    print("Não é primo.\n")  
"""
