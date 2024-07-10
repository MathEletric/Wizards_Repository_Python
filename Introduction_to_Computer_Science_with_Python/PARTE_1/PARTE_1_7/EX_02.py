def main():
    valores = [1, 4, 2, 9, 1, 10]
    print(soma_elementos(valores))






def soma_elementos(lista_valores):

    soma = 0    
    for i in range(len(lista_valores)):
        soma += lista_valores[i]
    
    return soma
    
    
if __name__ == "__main__":
    main()