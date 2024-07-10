# Algumas estruturas de repetição.

animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]

for x in animais:
    print("--> " + x, end=" ")
print()
for x in range(len(animais)): print("->", animais[x], end=" ")
print()
for x in range(len(animais)):
    animais[x] = "gosto muito de " + animais[x]
    print("-->", animais[x], end=" ")
print()
for x in animais: 
    print("--->", x, end=" ")
print()
numeros = [1, 2, 3, 4, 5]
for x in numeros: print("-->", x-1, end=" ")
print()
for i in range(16,4,-3):
	print(i, end=" ")
print()

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

for x in pares:
    print(x, end=" ")
print()
for x in range(len(pares)):
    print(x, end=" ")
print()
for x in range(len(pares)):
    print(pares[x], end=" ")
print()
for x in range(5, 10):        
    print(pares[x], end=" ")
print()
for i in range(1, 10):
     print(i, end=" ")
print()
animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
print(animais)
print()
# Clonagem de listas:
# Note que ao atribuir uma lista a outra, a referencia é a mesma, ou seja, ao alterar lista 1 ou 2, "ambas" se modificam:
lista1 = ["rosa", "preto", "branco"]
lista2 = lista1
print(f"{lista1}\n{lista2}")
print()
lista2[0] = "AZUL"
print(f"{lista1}\n{lista2}")
print()

# Para clonar de fato, fazemos:
lista1 = ["rosa", "preto", "branco"]
lista2 = lista1[:]
print(f"{lista1}")
print()
lista2[0] = "AZUL"
print(f"{lista1}\n{lista2}")
print()

# Pertinência de listas:
lista_pertinencia = [1, 2, 3, "quatro", 3+1, "cin" + "co"]
print(lista_pertinencia)
print("quatro" in lista_pertinencia)
print("cinco" in lista_pertinencia)

# Concatenação de listas:
a = [1, 2, "três"]
b = ["quatro", 5, 6]
c= a+b
print(a + b, a, b, c)
print()
b = a.append("4") # Não funciona.
print(b, a)

# Multiplocando uma lista:
print(a*3)

# Apagando uma parte da lista:
print("Apagando uma parte da lista: ")
a = [1, 2, "três", "quatro", 5, 6]
print(f"A lista -> {a}")
del a[2:5]
print(f"A nova lista após del a[2:5] -> {a}")



# Para clonar uma lista:
def muda_lista(lista_fora):
    lista_dentro = lista_fora[:]  # Sem o "[:]", o print de muda_lista e de lista são iguais.
    lista_dentro.append(4)        # Trata-se de dois nomes de referencia para uma mesma lista quando não se coloca [:]
    return lista_dentro           


lista = [1, 2, 3]

print(muda_lista(lista))
print(lista)

# Teste de iteração:
lista = [1, 2, 3, 4, 5, 6]
for num in lista[1:3]:
     print(num, end=' ')

print()
print(f"{'*'*10}Teste iteração com rage{'*'*10}")
# Teste iteração com rage:
lista = [1, 2, 3, 4, 5, 6]
for i in range(len(lista)):
     print(lista[i])