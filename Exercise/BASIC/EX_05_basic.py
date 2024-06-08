"""
Exercício 5

Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Entrada de Dados: 78615

Saída de Dados: O dígito das dezenas é 1

"""

x = int(input("Digite um número inteiro: "))

x = (x//10) % 10

print("A dígito das dezenas é ", x)
