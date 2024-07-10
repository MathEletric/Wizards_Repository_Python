def main():

    var = coef_input()
    
    while var >= 0:
        print(fatorial(var))
        var = coef_input()


def fatorial(x):

    fat = 1
    while x > 1:
        fat = fat*x
        x -= 1
    return fat


def coef_input():
    coef = int(input("Digite o valor: "))
    return coef


if __name__ == "__main__":
    main()