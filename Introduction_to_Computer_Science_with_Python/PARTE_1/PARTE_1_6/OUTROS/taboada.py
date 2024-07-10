def main():

    valor = coef_input()
    taboada_ate_o_valor_10(valor)

    valor_ate_qual_taboada = coef_input()
    todas_as_taboadas_ate(valor_ate_qual_taboada)


def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def taboada_ate_o_valor_10(x):

    print(f"\nTaboada do {x}:\n")
    i = 1

    while i <= 10:

        print(f"{x} x {i} = {x*i}")
        i += 1


def todas_as_taboadas_ate(x):

    print(f"\nTaboada do 1 até {x}:\n")
    j = 1

    while j <= x:
        
        print(f"\nTaboada do {j}:\n")
        i = 1

        while i <= 10:

            print(f"{j} x {i} = {i*j}")
            i += 1
        
        j += 1


if __name__ == "__main__":
    main()