def main():

    a = coef_input()
    b = coef_input()
    c = coef_input()

    calc_raizes(a, b, c)


def coef_input():
    coef = int(input("Digite o valor: "))
    return coef

def delta(a, b, c):
    return (b**2 - 4*a*c)

def ordenacao(a1, a2):
    if a1 > a2:
        print(f"as raízes da equação são {a2} e {a1}")
    else:
        print(f"as raízes da equação são {a1} e {a2}")

def calc_raizes(a, b, c):

    d = delta(a, b, c)

    if d < 0:
        print("Esta equação não possui raízes reais.")
    else:
        raiz1 = (-b + pow(d, 1/2))/2*a
        raiz2 = (-b - pow(d, 1/2))/2*a

    if raiz1 == raiz2:
        print(f"A raiz desta equação é {raiz1}.")
    else:
        ordenacao(raiz1, raiz2)
        
if __name__ == '__main__':
    main()