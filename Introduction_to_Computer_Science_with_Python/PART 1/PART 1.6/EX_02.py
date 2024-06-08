def main():

    L = coef_input()
    A = coef_input()

    desenho_retangulo(L, A)
 

def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def desenho_retangulo(x, y):
    
    altura = y
    largura = x

    while y:

        x = largura

        while x:

            if y < altura and y > 1:
                if x == largura or x == 1:
                    print("#", end="")
                else:
                    print(" ", end="")

            else:
                print("#", end="")

            x -= 1

        print()
        y -= 1

if __name__ == "__main__":
    main()
