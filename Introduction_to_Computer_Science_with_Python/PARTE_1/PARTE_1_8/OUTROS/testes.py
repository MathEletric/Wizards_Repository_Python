

for i in range(6):
    if i ==3:
        indice_maior = i + 1
    
print(f"O autor do texto {indice_maior} está infectado com COH-PIAH")



lista1 = ["carro", "carro", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
print(lista1.count("carro"))
#lista3 = lista1 + lista2


lista3 = []
for item in lista2:
    lista1.append(item)

print(lista1)


A1 = [1, 2, 3]
B1 = [1, 2, 3]
print(A1 is B1)

A2 = '123'
B2 = '123'
print(A2 is B2)

A3 = ['1', '2', '3']
B3 = ['1', '2', '3']
print(A3 is B3)
print(A3[0] is B3[0])
B3 = ['1', '2', '1']
print(A3[0] is B3[2])

lista = [1, 2, 3]
print([lista]*3)
lista_maior = [lista]*3
lista[0] = 10
print(lista_maior)
print(lista)
nova_lista = lista*3
print(nova_lista)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista1.append(lista2)
print(lista1)


print(lista1 == lista2)

print("-"*10)

lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"

print(lista2)