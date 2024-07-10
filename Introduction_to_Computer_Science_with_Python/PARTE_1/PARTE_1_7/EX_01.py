
def main():

    x = [3,2,7,2,3,8,4,3]
    print(x)
    x2 = remove_repetidos(x)
    print(x2)

   # print(remove_repetidos(x))
   # print(bubble_sort(x2))
   # print()
   # print(remove_repetivos_v2(x))
   # print(remove_repetivos_v3(x))


def remove_repetidos(lista):

    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    
    lista = lista_unica[:]

    for j in range(1, len(lista)):
    
        for i in range(len(lista)-j):

            if lista[i] > lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux

    return lista

            
def remove_repetivos_v2(lista):

    for item in lista:
        
        while lista.count(item) > 1:
            lista.remove(item)

    return lista


def remove_repetivos_v3(lista):

    i = 0

    while i < len(lista):
        if lista[i] in lista[:i]:
            del lista[i]
        else:
            i += 1

    return lista

def bubble_sort(lista):


    n = len(lista)
    
    for i in range(n):

        for j in range(n-1-i):
            
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux

    return lista


if __name__ == "__main__":
    main()