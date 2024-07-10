def main():

    #escrita_invertida()
    lista_inverso()

def escrita_invertida():

    item = []
    counter = 0

    item.append(coef_input())

    while item[counter] != 0:
        counter += 1
        item.append(coef_input())

    item.pop()
    counter = len(item) - 1
    

    print(f"Em ordem:\n {item}")

    print("Em ordem inversa:\n")
    while counter >= 0:
        print(item[counter], end=" ")
        counter -= 1

def  lista_inverso():

    lista = []
    c = 0

    lista.append(coef_input())
    while lista[c]:
        lista.append(coef_input())
        c += 1

    lista.pop()
    print(f"{lista}")

    counter_1 = len(lista) - 1 
    counter_2 = 0
    lista_invertida = [0]*len(lista)

    while counter_1:
        lista_invertida[counter_2] = lista[counter_1]
        counter_1 -= 1
        counter_2 += 1

    print(f"{lista_invertida}")

def coef_input():

    coef = int(input("Digite o valor: "))
    return coef

if __name__ == "__main__":
    main()