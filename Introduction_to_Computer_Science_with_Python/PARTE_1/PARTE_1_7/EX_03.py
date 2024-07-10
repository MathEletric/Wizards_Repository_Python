
def main():

    lista = [6, 2, 5]
    print(maior_elemento(lista))


def maior_elemento_v2(lista):

    return ordem_crescente(lista)[len(lista)-1]


def ordem_crescente(lista):

    for j in range(1, len(lista)):
    
        for i in range(len(lista)-j):

            if lista[i] > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux

    return lista


def maior_elemento(lista):

    maior = lista[0]
    for num in lista[1:]:
        if num > maior:
            maior = num

    return maior


if __name__ == "__main__":
    main()