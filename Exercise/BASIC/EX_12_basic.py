"""
Exercício 12

Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. 
Para a saída, siga o formato do exemplo abaixo.

Digite o valor de n: 5
1
3
5
7
9

"""

n = int(input("Digite um número: "))
num = 0
while  n > 0:
    if num % 2 != 0:
        print(num)
        n = n - 1
    num = num + 1
    