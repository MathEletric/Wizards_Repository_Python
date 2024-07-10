def main():

    x = coef_input()
    print(n_primos(x))


def coef_input():

    coef = int(input("Digite o valor: "))
    return coef


def n_primos(p_enesimo):
    
    primo = 0
    i = 0
    counter_primo = 0

    while p_enesimo >= 2:

        i = p_enesimo

        while i:

            if p_enesimo % i == 0:
                primo += 1

            i -= 1
        
        if primo == 2:
            counter_primo += 1

        primo = 0
        p_enesimo -= 1

    return counter_primo

if __name__ == "__main__":
    main()
