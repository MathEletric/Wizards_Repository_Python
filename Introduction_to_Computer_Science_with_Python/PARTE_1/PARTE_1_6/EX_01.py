def main():

    L = coef_input()
    A = coef_input()

    desenho_retangulo(L, A)
 

def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def desenho_retangulo(x, y):

    aux_x = x

    while y:

        x = aux_x
        while x:

            print("#", end="")
            x -= 1

        print()
        y -= 1


if __name__ == "__main__":
    main()
