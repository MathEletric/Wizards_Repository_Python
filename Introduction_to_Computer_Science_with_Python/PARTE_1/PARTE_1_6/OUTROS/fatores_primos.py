def main():

    n = coef_input()
    print(dec_fatores_primos(n))


def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def dec_fatores_primos(x):

    fator = 2
    multiplicidade = 0

    while x > 1:
        while x % fator ==  0:
            multiplicidade += 1
            x = x / fator

        counter = fator
        mem = 0
        primo = False

        while counter:

            if fator % counter == 0:
                mem += 1

            counter -= 1

        if mem == 2:
            primo = True
        else:
            primo = False

        if multiplicidade > 0:
            print("Fator", fator, "multiplicidade", multiplicidade, "Fator é primo -> ", primo)
        multiplicidade = 0
        fator = fator + 1



if __name__ == "__main__":
    main()