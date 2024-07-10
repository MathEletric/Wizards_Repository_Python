def main():

    lista_invertida()


def  lista_invertida():

    lista = []
    while True:
        num = coef_input()
        if not num:
            break
        else:
            lista.append(num)


    counter_1 = len(lista) - 1  
    counter_2 = 0
    lista_invertida = [99]*(len(lista))

    while counter_1 >= 0:
        lista_invertida[counter_2] = lista[counter_1]
        counter_1 -= 1
        counter_2 += 1

    for i in range(len(lista_invertida),):
        print(lista_invertida[i])


def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


if __name__ == "__main__":
    main()