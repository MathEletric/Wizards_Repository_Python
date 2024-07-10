n = int(input("Digite o valor de n: "))
cont = 0
num = 1
while cont < n:
    if num % 2 != 0:
        print(num)
        cont += 1
    num += 1
