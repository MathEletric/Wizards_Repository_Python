"""
Exercício 4

Escreveva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a 
quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, 
c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.

"""

total_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

# Calcula quandos dias "cabem" dentro do total de segundos.
dias  = total_segundos // 86400

# Calcula quantos segundos restam quando retirado a quantidades de segundos que formam dias inteiros.
resto_segundos = total_segundos % 86400

# A partir de quantos segundos restam, depois de retirado os dias inteiros, podemos retirar a quantidade de horas.
horas = resto_segundos // 3600

# Tiramos os segundos restantes que não formam nenhuma hora.
resto_segundos = resto_segundos % 3600

# Calcula quantos minutos cabem dentro do restante de segundos que não formam uma única hora.
minutos = resto_segundos // 60

# Guarda a quantidade de segundos que não sequer formam um unico minuto.
resto_segundos = resto_segundos % 60

print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s), {resto_segundos} segundos")
