"""
Exercício 11

Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

"""

n = int(input("Digite um valor: "))
dig = n
while dig > 1:
    dig = dig - 1
    print(dig)
    n = n*dig

print(f"O fatorial: {n}")
