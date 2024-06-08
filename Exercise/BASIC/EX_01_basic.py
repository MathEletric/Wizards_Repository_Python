"""
Exercício 1

Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima 
(saída de dados) seu perímetro e sua área. Observação: a saída deve estar no formato: "perímetro: x - área: y"

"""
x = float(input("Digite o valor em centímetros da aresta de um quadrado bidimensional: "))
print(f"A área: {x*x};\nO perímetro: {4*x};\n")
