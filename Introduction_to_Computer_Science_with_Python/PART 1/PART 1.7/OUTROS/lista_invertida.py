def main():

    lista_invertida()



def lista_invertida():

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



def coef_input():

    coef = int(input("Digite o valor: "))
    return coef





if __name__ == "__main__":
    main()