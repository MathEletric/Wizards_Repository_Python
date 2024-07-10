n = input("Digite um número inteiro: ")

counter = len(n)
i = False

while counter:
    if int(n) > 0:
        dig_atual     = (int(n) // 10**(counter    )) % 10
        dig_anterior  = (int(n) // 10**(counter - 1)) % 10
        if dig_atual == dig_anterior:
            i = True
    counter -= 1

if i:
    print("sim")
else:
    print("não")
   
# Versão 2:

"""
x = input("Digite um valor: ")

adjacente = False
atual = 0
anterior = 0
numero = int(x)

while numero > 0:
    atual = numero % 10
    
    if atual == anterior:
        adjacente = True


    anterior = atual
    numero = numero // 10

if adjacente:
    print("sim")
else:
    print("não")
"""


